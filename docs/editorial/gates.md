# Gate sequence and state

| Field | Value |
| --- | --- |
| Status | **Proposed** — owner approvals pending |
| Date | 2026-11-06 |
| Machine-readable state | [`gates.json`](gates.json) |
| File-level checks | `scripts/check_repo.py` using `scripts/gate_policy.py` |

This page exists because the gate sequence has one easily inverted dependency: **Gate 3 approves a written pilot, so Gate 3 cannot be a precondition for writing it.** Gates 1 and 2 authorize the pilot file; Gate 3 authorizes expansion.

## 1. Sequence

| Point in time | Gate 1 brief | Gate 2 outline | Gate 3 pilot | Manuscript files allowed |
| --- | --- | --- | --- | --- |
| Bootstrap | Proposed | Proposed | Blocked | None |
| After brief approval | Approved | Proposed | Blocked | None |
| After outline approval | Approved | Approved | Pending | Exactly `pilot.path` (file boundary only) |
| Pilot submitted for review | Approved | Approved | Pending | Exactly `pilot.path` (file boundary only) |
| After pilot approval | Approved | Approved | Approved | Expansion, chapter by chapter |

Gate 3 has three values:

- **blocked** — the pilot file is not authorized; no `.qmd` may exist.
- **pending** — Gates 1 and 2 are approved; exactly the authorized pilot file may be committed and reviewed. Its contents are checked by editorial review, not by `make check`.
- **approved** — the owner has approved the reviewed pilot; chapter expansion may begin.

## 2. What each gate decides

| Gate | Decision | Does it authorize writing? |
| --- | --- | --- |
| 1 — brief | Audience, scope, non-goals, quality bar, licensing | No. It constrains the work. |
| 2 — outline | Structure, profile coverage, pilot candidate and file path | Yes, the pilot file, once Gate 3 is set to `pending`. |
| 3 — pilot | The written pilot is acceptable | Yes, expansion after approval. |
| Chapter review | Each subsequent chapter is acceptable | No; it follows the Gate 3 expansion decision. |

The pilot is deliberately the only manuscript file written before the gate that approves it. The owner cannot approve a section that does not exist, and the author should not write the whole book before the first approval.

## 3. State transitions

1. **Owner approves the brief.** Update the brief status and approval block, `PROJECT_STATUS.md`, and `gates.json`: `gate_1_brief` becomes `approved`.
2. **Owner approves the outline.** Update the outline status and approval block, `PROJECT_STATUS.md`, and `gates.json`: `gate_2_outline` becomes `approved` and `gate_3_pilot` becomes `pending`. This records the pilot write authorization.
3. **Implementer writes only the pilot file.** The file must be exactly `pilot.path`, and it must contain only section 2.2. No other `.qmd` file may be added.
4. **A different agent or person reviews the pilot.** The review records the exact HEAD and verdict, and confirms that the file contains only section 2.2 and follows the content profile.
5. **Owner decides Gate 3.** Update `PROJECT_STATUS.md` and `gates.json`: `gate_3_pilot` becomes `approved`. Expansion is now allowed.
6. **Chapter-by-chapter expansion.** Each chapter is reviewed independently; the owner still approves each chapter.

Gate approvals are recorded by the owner, never by an implementer or reviewer. This bootstrap records none of them.

## 4. What the check does and does not prove

The check enforces a **file boundary** and gate ordering. While Gate 3 is `pending`, it rejects any `.qmd` other than `pilot.path`; it never reads the file's contents. Section scope, profile conformance and editorial quality are confirmed by independent review.

The gate values in `gates.json` are a **recorded assertion**, kept in step with the owner's decision. The check validates their values, ordering and consistency with the brief and outline statuses. It does not authenticate the owner or prove that authorization occurred; reviewers verify the approval record.

## 5. Check behavior

`make check` fails when:

- a gate value is unknown or out of order;
- `pilot.path` is not a repository-relative `.qmd` file under `manuscript/`;
- a `.qmd` file exists before Gate 2 approval or while Gate 3 is `blocked`;
- any `.qmd` other than `pilot.path` exists while Gate 3 is `pending`;
- Gate 3 is `approved` but the pilot file is missing;
- a gate status in `gates.json` disagrees with the matching brief or outline status.

The policy has unit tests in `scripts/tests/test_gate_policy.py` for every state, including the deadlock regression: a pending Gate 3 must allow the pilot file. No test or check asserts section 2.2 scope.
