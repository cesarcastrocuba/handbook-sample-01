#!/usr/bin/env python3
"""Book-local consistency checks for the sample handbook bootstrap.

Shared handbook-platform validation belongs to the pinned hub toolkit and is
intentionally not vendored here. This check uses only the Python standard
library so it can run on a clean clone.

The final check enforces the current gate: no manuscript prose exists until the
pilot is approved. When Gate 3 is approved, replace that check with the pinned
toolkit's content validation; do not delete it silently.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

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
    ".gitignore",
    ".github/workflows/check.yml",
    "docs/editorial/brief.md",
    "docs/editorial/outline.md",
    "docs/editorial/profile.md",
    "manuscript/README.md",
    "publishing/README.md",
    "publishing/metadata.yaml",
    "sdd/changes/0001-sample-bootstrap/proposal.md",
    "sdd/changes/0001-sample-bootstrap/tasks.md",
    "scripts/check_repo.py",
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


def check_editorial_status() -> None:
    for name in ("docs/editorial/brief.md", "docs/editorial/outline.md"):
        text = (ROOT / name).read_text(encoding="utf-8")
        if "**Proposed**" not in text:
            raise CheckError(f"{name} must carry a Proposed status during bootstrap")
        if "**Approved**" in text:
            raise CheckError(f"{name} claims approval; the owner must record it first")


def check_bootstrap_gate() -> None:
    prose = sorted(str(path.relative_to(ROOT)) for path in (ROOT / "manuscript").rglob("*.qmd"))
    if prose:
        raise CheckError(
            "Gate 3 is not approved, but manuscript prose exists:\n  "
            + "\n  ".join(prose)
            + "\nWrite the pilot only after the owner approves Gates 1 and 2."
        )


def main() -> int:
    checks = (
        ("required files", check_required_files),
        ("relative links", check_links),
        ("generated artifacts", check_generated_artifacts),
        ("environment paths", check_environment_paths),
        ("agent-neutral roles", check_roles),
        ("editorial status", check_editorial_status),
        ("bootstrap gate", check_bootstrap_gate),
    )
    try:
        for label, check in checks:
            result = check()
            detail = f" ({result} links)" if label == "relative links" else ""
            print(f"OK  {label}{detail}")
    except CheckError as error:
        print(f"FAIL  {error}", file=sys.stderr)
        return 1

    print("\nRepository is consistent with the bootstrap gate.")
    print("No chapter prose, build or release is present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
