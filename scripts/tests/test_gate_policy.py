"""Tests for the gate-sequence policy.

The regression under test: Gate 3 approves a written pilot, so it must not
block writing the pilot. Gates 1 and 2 authorize exactly the pilot; Gate 3
authorizes expansion.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from gate_policy import validate_gate_state, validate_manuscript_prose  # noqa: E402

PILOT = "manuscript/chapters/ch02-editorial-contract.qmd"
OTHER = "manuscript/chapters/ch01-why-handbooks-fail.qmd"


def state(
    gate_1: str = "approved",
    gate_2: str = "approved",
    gate_3: str = "pending",
    path: str = PILOT,
) -> dict[str, object]:
    return {
        "gate_1_brief": gate_1,
        "gate_2_outline": gate_2,
        "gate_3_pilot": gate_3,
        "pilot": {"path": path},
    }


class GateStateTests(unittest.TestCase):
    def test_bootstrap_state_is_valid(self) -> None:
        self.assertEqual(
            validate_gate_state(state(gate_1="proposed", gate_2="proposed", gate_3="blocked")),
            [],
        )

    def test_outline_cannot_pass_brief(self) -> None:
        errors = validate_gate_state(
            state(gate_1="proposed", gate_2="approved", gate_3="blocked")
        )
        self.assertTrue(any("cannot be approved before" in error for error in errors))

    def test_pilot_window_requires_both_earlier_gates(self) -> None:
        errors = validate_gate_state(
            state(gate_1="approved", gate_2="proposed", gate_3="pending")
        )
        self.assertTrue(any("before Gates 1 and 2" in error for error in errors))

    def test_pilot_path_must_be_manuscript_qmd(self) -> None:
        errors = validate_gate_state(state(path="../outside.qmd"))
        self.assertTrue(any("inside the repository" in error for error in errors))

    def test_pilot_path_must_live_under_manuscript(self) -> None:
        errors = validate_gate_state(state(path="publishing/pilot.qmd"))
        self.assertTrue(any("under manuscript/" in error for error in errors))


class ProseTests(unittest.TestCase):
    def test_bootstrap_allows_no_prose(self) -> None:
        bootstrap = state(gate_1="proposed", gate_2="proposed", gate_3="blocked")
        self.assertEqual(validate_manuscript_prose(bootstrap, []), [])

    def test_bootstrap_rejects_any_prose(self) -> None:
        bootstrap = state(gate_1="proposed", gate_2="proposed", gate_3="blocked")
        errors = validate_manuscript_prose(bootstrap, [PILOT])
        self.assertTrue(any("No manuscript prose" in error for error in errors))

    def test_approved_gates_before_pilot_window_still_reject_prose(self) -> None:
        blocked = state(gate_3="blocked")
        errors = validate_manuscript_prose(blocked, [PILOT])
        self.assertTrue(any("No manuscript prose" in error for error in errors))

    def test_pending_gate_three_allows_exactly_the_pilot(self) -> None:
        pending = state(gate_3="pending")
        self.assertEqual(validate_manuscript_prose(pending, []), [])
        self.assertEqual(validate_manuscript_prose(pending, [PILOT]), [])

    def test_pending_gate_three_rejects_expansion(self) -> None:
        pending = state(gate_3="pending")
        errors = validate_manuscript_prose(pending, [PILOT, OTHER])
        self.assertTrue(any(OTHER in error for error in errors))

    def test_pending_gate_three_rejects_other_chapter_without_pilot(self) -> None:
        pending = state(gate_3="pending")
        errors = validate_manuscript_prose(pending, [OTHER])
        self.assertTrue(any(OTHER in error for error in errors))

    def test_gate_three_approval_allows_expansion(self) -> None:
        approved = state(gate_3="approved")
        self.assertEqual(validate_manuscript_prose(approved, [PILOT, OTHER]), [])

    def test_gate_three_approval_requires_the_pilot(self) -> None:
        approved = state(gate_3="approved")
        errors = validate_manuscript_prose(approved, [OTHER])
        self.assertTrue(any("reviewed pilot is missing" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
