"""Gate-sequence policy for the sample handbook.

The sequence has one deliberate asymmetry: Gates 1 and 2 authorize *writing*
exactly one pilot file; Gate 3 approves that written, reviewed pilot and
authorizes expansion. Gate 3 therefore cannot be a precondition for writing
the pilot.

This module is pure and dependency-free so the policy can be tested without a
repository or a build toolchain. `scripts/check_repo.py` applies it to the real
working tree; `scripts/tests/test_gate_policy.py` covers every state.

The policy is file-level only. It cannot verify that the pilot file contains
only section 2.2, and it does not authenticate gate approvals; both remain
editorial-review responsibilities.
"""

from __future__ import annotations

from pathlib import PurePosixPath
from typing import Iterable, Mapping

GATE_1 = "gate_1_brief"
GATE_2 = "gate_2_outline"
GATE_3 = "gate_3_pilot"

GATE_12_STATES = {"proposed", "approved"}
GATE_3_STATES = {"blocked", "pending", "approved"}


def _pilot_path(state: Mapping[str, object]) -> str:
    pilot = state.get("pilot")
    if not isinstance(pilot, Mapping):
        raise ValueError("gate state must contain a 'pilot' object")

    path = pilot.get("path")
    if not isinstance(path, str) or not path:
        raise ValueError("pilot.path must be a non-empty repository-relative path")

    pure = PurePosixPath(path)
    if pure.is_absolute() or ".." in pure.parts:
        raise ValueError("pilot.path must stay inside the repository")
    if pure.suffix != ".qmd":
        raise ValueError("pilot.path must be a .qmd file")
    if not pure.parts or pure.parts[0] != "manuscript":
        raise ValueError("pilot.path must live under manuscript/")
    return path


def validate_gate_state(state: Mapping[str, object]) -> list[str]:
    """Validate gate values and their ordering. Return human-readable errors."""
    errors: list[str] = []

    gate_1 = state.get(GATE_1)
    gate_2 = state.get(GATE_2)
    gate_3 = state.get(GATE_3)

    if gate_1 not in GATE_12_STATES:
        errors.append(f"{GATE_1} must be one of {sorted(GATE_12_STATES)}")
    if gate_2 not in GATE_12_STATES:
        errors.append(f"{GATE_2} must be one of {sorted(GATE_12_STATES)}")
    if gate_3 not in GATE_3_STATES:
        errors.append(f"{GATE_3} must be one of {sorted(GATE_3_STATES)}")

    if errors:
        return errors

    try:
        _pilot_path(state)
    except ValueError as error:
        errors.append(str(error))
        return errors

    if gate_1 != "approved" and gate_2 == "approved":
        errors.append(f"{GATE_2} cannot be approved before {GATE_1}")

    if gate_3 in {"pending", "approved"} and (
        gate_1 != "approved" or gate_2 != "approved"
    ):
        errors.append(f"{GATE_3} cannot be {gate_3} before Gates 1 and 2 are approved")

    return errors


def validate_manuscript_prose(
    state: Mapping[str, object], prose_paths: Iterable[str]
) -> list[str]:
    """Return the gate violations for the manuscript files present.

    - Gate 1 or 2 not approved, or Gate 3 blocked: no prose at all.
    - Gates 1 and 2 approved, Gate 3 pending: exactly the pilot file may exist.
    - Gate 3 approved: expansion is allowed; the pilot must still be present.

    This is a file-boundary check only. It does not read file contents, confirm
    that the pilot is limited to section 2.2, or authenticate gate approvals.
    """
    errors = validate_gate_state(state)
    if errors:
        return errors

    gate_1 = state[GATE_1]
    gate_2 = state[GATE_2]
    gate_3 = state[GATE_3]
    pilot = _pilot_path(state)
    prose = sorted({PurePosixPath(path).as_posix() for path in prose_paths})

    if gate_3 == "approved":
        if pilot not in prose:
            errors.append(
                f"Gate 3 is approved but the reviewed pilot is missing: {pilot}"
            )
        return errors

    if gate_1 != "approved" or gate_2 != "approved" or gate_3 == "blocked":
        if prose:
            errors.append(
                "No manuscript prose is allowed before Gates 1 and 2 are approved "
                "and the pilot window is open; found: " + ", ".join(prose)
            )
        return errors

    # Gate 3 pending with Gates 1 and 2 approved: the pilot window.
    extras = [path for path in prose if path != pilot]
    if extras:
        errors.append(
            "While Gate 3 is pending, only the authorized pilot file may exist: "
            f"{pilot}. Found extra prose: " + ", ".join(extras)
        )
    return errors
