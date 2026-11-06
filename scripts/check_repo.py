#!/usr/bin/env python3
"""Book-local consistency checks for the sample handbook bootstrap.

Shared handbook-platform validation belongs to the pinned hub toolkit and is
intentionally not vendored here. This check uses only the Python standard
library so it can run on a clean clone.

The gate check enforces the sequence, not a blanket "no prose" rule: Gates 1
and 2 authorize exactly one pilot file; Gate 3 approves the written, reviewed
pilot and authorizes expansion. This is a file-boundary check: it does not read
`.qmd` contents, verify that the pilot is limited to section 2.2, or
authenticate gate approvals. When the pinned toolkit provides content
validation, keep the gate policy and replace only the content checks.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import gate_policy

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "README.md",
    "AGENTS.md",
    "CONTRIBUTING.md",
    "DECISIONS.md",
    "PROJECT_STATUS.md",
    "NOTICE.md",
    "LICENSE",
    "LICENSE-CODE",
    "Makefile",
    "requirements.txt",
    "book.yaml",
    ".gitignore",
    ".github/workflows/check.yml",
    "docs/editorial/brief.md",
    "docs/editorial/outline.md",
    "docs/editorial/profile.md",
    "docs/editorial/gates.md",
    "docs/editorial/gates.json",
    "docs/editorial/approval-record.md",
    "docs/integration/pinned-toolkit.md",
    "manuscript/README.md",
    "manuscript/book.yml",
    "publishing/README.md",
    "publishing/metadata.yaml",
    "sdd/changes/0001-sample-bootstrap/proposal.md",
    "sdd/changes/0001-sample-bootstrap/tasks.md",
    "sdd/changes/0002-pilot-gate-window/proposal.md",
    "scripts/check_repo.py",
    "scripts/gate_policy.py",
    "scripts/tests/test_gate_policy.py",
)

FORBIDDEN_DIRECTORY_NAMES = {
    "_site",
    "_build",
    ".quarto",
    "__pycache__",
    ".pytest_cache",
    ".venv",
    "node_modules",
}

FORBIDDEN_SUFFIXES = {".pdf", ".docx", ".epub", ".html"}

TEXT_SUFFIXES = {".md", ".qmd", ".yml", ".yaml", ".py", ".sh", ".toml"}
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)")
SKIP_SCHEMES = ("http://", "https://", "mailto:", "tel:", "data:")
HOME_PREFIX = "/" + "home/"


class CheckError(Exception):
    """Raised when a repository check fails."""


def iter_files() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.relative_to(ROOT).parts
    ]


def check_required_files() -> None:
    missing = [name for name in REQUIRED_FILES if not (ROOT / name).is_file()]
    if missing:
        raise CheckError("missing required files: " + ", ".join(missing))


def check_links() -> int:
    checked = 0
    broken: list[str] = []
    for path in iter_files():
        if path.suffix.lower() not in {".md", ".qmd"}:
            continue
        text = path.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = match.group(1).strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            if not target or target.startswith("#") or target.startswith(SKIP_SCHEMES):
                continue
            target = target.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                broken.append(f"{path.relative_to(ROOT)} -> {target} (outside repository)")
                continue
            checked += 1
            if not resolved.exists():
                broken.append(f"{path.relative_to(ROOT)} -> {target}")
    if broken:
        raise CheckError("broken relative links:\n  " + "\n  ".join(broken))
    return checked


def check_generated_artifacts() -> None:
    found: list[str] = []
    for path in iter_files():
        parts = path.relative_to(ROOT).parts
        if any(part in FORBIDDEN_DIRECTORY_NAMES for part in parts[:-1]):
            found.append(str(path.relative_to(ROOT)))
        elif path.suffix.lower() in FORBIDDEN_SUFFIXES:
            found.append(str(path.relative_to(ROOT)))
    if found:
        raise CheckError("generated artifacts or caches found:\n  " + "\n  ".join(sorted(found)))


def check_environment_paths() -> None:
    leaks: list[str] = []
    for path in iter_files():
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if HOME_PREFIX in text:
            leaks.append(str(path.relative_to(ROOT)))
    if leaks:
        raise CheckError("environment-specific absolute paths found in: " + ", ".join(sorted(leaks)))


def check_roles() -> None:
    text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    missing = [role for role in ("Owner", "Implementer", "Reviewer") if role not in text]
    if missing:
        raise CheckError("AGENTS.md is missing agent-neutral roles: " + ", ".join(missing))
    if "not products" not in text:
        raise CheckError("AGENTS.md must state that roles are not products")


def load_gate_state() -> dict[str, object]:
    path = ROOT / "docs/editorial/gates.json"
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise CheckError(f"cannot read {path.relative_to(ROOT)}: {error}") from error
    if not isinstance(state, dict):
        raise CheckError("docs/editorial/gates.json must contain a JSON object")
    return state


def check_gate_state() -> None:
    errors = gate_policy.validate_gate_state(load_gate_state())
    if errors:
        raise CheckError("invalid gate state:\n  " + "\n  ".join(errors))


def check_editorial_status() -> None:
    state = load_gate_state()
    for key, name in (
        (gate_policy.GATE_1, "docs/editorial/brief.md"),
        (gate_policy.GATE_2, "docs/editorial/outline.md"),
    ):
        status = state.get(key)
        text = (ROOT / name).read_text(encoding="utf-8")
        expected = "**Proposed**" if status == "proposed" else "**Approved**"
        other = "**Approved**" if status == "proposed" else "**Proposed**"
        if expected not in text:
            raise CheckError(
                f"{name} must carry {expected} to match {key}={status} in gates.json"
            )
        if other in text:
            raise CheckError(
                f"{name} carries {other} but {key}={status} in gates.json"
            )
        if status == "approved" and "| Owner | *Pending* |" in text:
            raise CheckError(
                f"{name} is approved in gates.json but its approval block is still pending"
            )


def check_manuscript_gate() -> int:
    state = load_gate_state()
    prose = sorted(
        path.relative_to(ROOT).as_posix()
        for path in (ROOT / "manuscript").rglob("*.qmd")
    )
    try:
        errors = gate_policy.validate_manuscript_prose(state, prose)
    except ValueError as error:
        raise CheckError(str(error)) from error
    if errors:
        raise CheckError("gate policy violation:\n  " + "\n  ".join(errors))
    return len(prose)


def main() -> int:
    checks = (
        ("required files", check_required_files),
        ("relative links", check_links),
        ("generated artifacts", check_generated_artifacts),
        ("environment paths", check_environment_paths),
        ("agent-neutral roles", check_roles),
        ("gate state", check_gate_state),
        ("editorial status", check_editorial_status),
        ("manuscript gate", check_manuscript_gate),
    )
    try:
        for label, check in checks:
            result = check()
            detail = ""
            if label == "relative links":
                detail = f" ({result} links)"
            elif label == "manuscript gate":
                detail = f" ({result} prose files)"
            print(f"OK  {label}{detail}")
    except CheckError as error:
        print(f"FAIL  {error}", file=sys.stderr)
        return 1

    print("\nRepository is consistent with the gate sequence at file level.")
    print("Pilot window: only the pilot file at pilot.path is allowed; section scope is reviewed.")
    print("Gate values are recorded assertions; owner authorization is reviewed separately.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
