# Change 0002 — open the pilot gate window

| Field | Value |
| --- | --- |
| Status | **Proposed** — owner review |
| Date | 2026-11-06 |
| Repository | `handbook-sample-01` |
| Fixes | Blocking review finding on commit `69f1add` |
| Gates affected | None; no gate is approved by this change |

## Context

Review of `69f1add` found a circular gate:

- `AGENTS.md` forbade committing the pilot while Gate 3 was pending.
- `outline.md` said no pilot could be written until Gate 3 approval.
- `check_repo.py` rejected all manuscript prose until the pilot was approved.

Gate 3 was defined as the owner's approval of a written pilot. If writing the pilot required Gate 3, no pilot could ever exist to approve. The bootstrap therefore deadlocked before the first pilot.

## Decision

Separate **writing authority** from **approval authority**:

| Gate | Authorizes |
| --- | --- |
| Gate 1 — brief | Constrains audience, scope, non-goals, quality bar and licensing |
| Gate 2 — outline | Writes exactly the pilot at `pilot.path` while Gate 3 is `pending` |
| Gate 3 — pilot | Approves the written, reviewed pilot and authorizes expansion |

The sequence is:

```text
Gate 2 approved -> Gate 3 pending -> write exactly the pilot -> independent review
-> Gate 3 approved -> expansion
```

## Changes

- `AGENTS.md`, `docs/editorial/brief.md`, `docs/editorial/outline.md`, `PROJECT_STATUS.md`, `CONTRIBUTING.md`, `README.md`, `manuscript/README.md` and `publishing/README.md` now describe the same sequence.
- `docs/editorial/gates.json` is the machine-readable gate state and names the authorized pilot path.
- `docs/editorial/gates.md` defines the sequence, transitions and check behavior.
- `scripts/gate_policy.py` implements the state machine; `scripts/check_repo.py` applies it.
- `scripts/tests/test_gate_policy.py` covers every state, including the regression that a pending Gate 3 must allow the pilot.
- `make check` runs the tests before the repository check.

## Scope

This change corrects governance and validation. It does not write the pilot, approve a gate, build an artifact or publish anything.

## Verification

```sh
make check
```

Expected: all gate-policy tests pass, the repository check reports `0 prose files`, and both gate documents still carry Proposed status matching `gates.json`.

## Rollback boundary

Revert this commit. The repository returns to the contradictory bootstrap policy; the previously reviewed files remain unchanged in history.

## Next step

Independent review of this commit. The owner then decides Gate 1 and Gate 2. Only after Gate 2 sets `gate_3_pilot` to `pending` may a separate change write the pilot.
