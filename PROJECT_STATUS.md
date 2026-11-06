# Project status

This file is the only source of current status. Decisions live in [`DECISIONS.md`](DECISIONS.md); scope lives in the [editorial brief](docs/editorial/brief.md) and [outline](docs/editorial/outline.md).

## Phase

Sample book bootstrap (platform phase 3). The repository scaffold, editorial brief and proposed outline are ready for independent review. No manuscript prose exists.

## Gates

| Gate | State | Evidence |
| --- | --- | --- |
| 1 — editorial brief | **Proposed**, awaiting owner approval | [`docs/editorial/brief.md`](docs/editorial/brief.md) |
| 2 — outline | **Proposed**, awaiting owner approval | [`docs/editorial/outline.md`](docs/editorial/outline.md) |
| 3 — pilot section | **Blocked**, not started | Gate 1 and Gate 2 must be approved first |

## Completed in this bootstrap

- Local Git repository initialized on `main`.
- Agent-neutral roles and workflow defined in [`AGENTS.md`](AGENTS.md).
- Editorial brief, proposed outline and content profile drafted.
- Manuscript and publishing layouts reserved without prose or build claims.
- Lightweight SDD proposal and task record created.
- Dependency-free repository check added and documented.
- Content and code licensing recorded as a proposal.

## Not done, by design

- No pilot section and no chapter prose.
- No Quarto configuration or build; Quarto is not installed in the bootstrap environment.
- No HTML, PDF, DOCX, site output or release.
- No GitHub repository, deployment, catalog entry or release.
- No change to the hub or to the existing handbook.

## Next step

The owner reviews the [brief](docs/editorial/brief.md) and [outline](docs/editorial/outline.md). On approval, Gate 1 and Gate 2 are recorded here and a separate scoped task writes the pilot section. Nothing else should be written before that decision.

## Verification

Run from a clean checkout:

```sh
make check
```

The check is book-local and uses only the Python standard library. Shared platform checks are deferred to the pinned hub toolkit.
