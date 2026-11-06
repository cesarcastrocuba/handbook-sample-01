# Change 0001 — bootstrap the sample handbook repository

| Field | Value |
| --- | --- |
| Status | **Proposed** — owner review |
| Date | 2026-11-06 |
| Repository | `handbook-sample-01` |
| Gates affected | Gate 1 and Gate 2 proposals; Gate 3 explicitly blocked |

## Context

The platform needs a sample book that demonstrates the editorial contract and the gate workflow without borrowing content from the existing handbook. The repository starts empty. The hub toolkit is not yet available, so the bootstrap must not depend on a parent checkout, copied validators or a build that cannot be reproduced.

## Decision

Create a minimal, independently reviewable book repository containing:

- agent-neutral roles and a gate sequence;
- a proposed editorial brief and outline;
- a proposed content profile;
- reserved manuscript and publishing layouts with no prose and no build claims;
- a dependency-free book-local consistency check;
- decision, status and change records.

The pilot section is deliberately not written. The outline names it, defines its approval criteria and provides its exact path, but Gate 3 remains blocked until Gates 1 and 2 are approved. Gate 2 opens the pilot window; Gate 3 approves the written, reviewed pilot and authorizes expansion.

## Scope

**Included:** governance, editorial proposals, repository layout, local checks, licensing proposal, minimal CI.

**Excluded:** chapter or pilot prose, Quarto configuration, builds, artifacts, deployment, GitHub repository creation, catalog entries, releases and changes to the hub or existing handbook.

## Assumptions

- The hub toolkit version and command names are unknown; publication is deferred.
- The owner will confirm attribution and licensing before release.
- English is the publication language.
- A book-local check may inspect repository consistency but must not duplicate shared platform validators.

## Risks and mitigations

| Risk | Mitigation |
| --- | --- |
| The brief or outline is treated as approved without the owner | Every document carries an explicit Proposed status; the check verifies the bootstrap gate and the absence of `.qmd` prose. |
| The sample accidentally becomes a fork of the existing handbook | No content is copied; only standard license texts are included; the outline is original. |
| A local check drifts into a second toolkit | The check is dependency-free and limited to file, link and gate consistency; shared validation is explicitly deferred to the pinned toolkit. |
| Attribution is assumed | `NOTICE.md` and the brief mark attribution as an owner decision. |

## Verification

```sh
make check
git diff --check
```

The change is ready for review when both commands pass on the commit under review.

## Rollback boundary

Remove this change's files and revert the bootstrap commit. No external system, publication or manuscript content depends on it.

## Next step

Independent review of the commit. The owner then decides Gate 1 (brief) and Gate 2 (outline). Gate 2 approval sets `gate_3_pilot` to `pending`; a separate change may then write exactly the pilot. Gate 3 is decided after independent review, and expansion waits for it.
