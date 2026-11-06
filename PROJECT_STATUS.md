# Project status

This file is the only source of current status. Decisions live in [`DECISIONS.md`](DECISIONS.md); scope lives in the [editorial brief](docs/editorial/brief.md) and [outline](docs/editorial/outline.md).

## Phase

Sample book bootstrap (platform phase 3). The repository scaffold, editorial brief and proposed outline are ready for independent review. No manuscript prose exists.

## Gates

| Gate | State | Evidence |
| --- | --- | --- |
| 1 — editorial brief | **Proposed**, awaiting owner approval | [`docs/editorial/brief.md`](docs/editorial/brief.md) |
| 2 — outline | **Proposed**, awaiting owner approval | [`docs/editorial/outline.md`](docs/editorial/outline.md) |
| 3 — pilot section | **Blocked**, not started | After Gates 1 and 2 are approved, exactly the pilot file at `pilot.path` may be committed and reviewed while Gate 3 is pending. The check enforces that file boundary; a reviewer confirms the file contains only section 2.2. Gate 3 approval then authorizes expansion. |

Gate state is machine-readable in [`docs/editorial/gates.json`](docs/editorial/gates.json) and explained in [`docs/editorial/gates.md`](docs/editorial/gates.md). Gate 3 approves written work; it is not a precondition for writing the pilot. Gate values are a recorded assertion kept in step with owner decisions, not proof of authorization.

## Completed in this bootstrap

- Local Git repository initialized on `main`.
- Agent-neutral roles and workflow defined in [`AGENTS.md`](AGENTS.md).
- Editorial brief, proposed outline and content profile drafted.
- Manuscript and publishing layouts reserved without prose or build claims.
- Lightweight SDD proposal and task record created.
- Dependency-free repository check, gate-state policy and state-machine tests added and documented.
- Pinned public-hub toolkit integration: `requirements.txt` uses a direct Git requirement at full SHA `0e8d897acae67d55eb09bf06a6e890d07d187779` with `#subdirectory=tools`; `book.yaml` and the empty `manuscript/book.yml` reading order are draft metadata only.
- CI installs the pinned toolkit and runs the fast `validate-book` check on `main`, `feat/**`, pull requests and `workflow_dispatch`.
- Content and code licensing recorded as a proposal.

## Not done, by design

- No pilot section and no chapter prose.
- No Quarto configuration or build; Quarto is not installed in the bootstrap environment.
- No full manuscript or artifact validation yet. `make full` is a current-scope incomplete gate: it passes the fast descriptor check, then fails because no pilot exists for `validate-book --full` and no artifact manifest exists. This is not a descriptor failure.
- No HTML, PDF, DOCX, site output or release.
- No GitHub repository, deployment, catalog entry or release.
- No change to the hub or to the existing handbook.

## Next step

The owner reviews the [brief](docs/editorial/brief.md) and [outline](docs/editorial/outline.md). On approval, both gates are recorded here and in `gates.json`; Gate 2 sets `gate_3_pilot` to `pending`. A separate scoped task then writes only the pilot file, and a reviewer confirms it contains only section 2.2. Gate 3 is decided after that independent review, and only then may expansion begin.

## Verification

Run from a clean checkout:

```sh
python3 -m pip install -r requirements.txt
make check
```

`make full` intentionally fails and states which full-manuscript and artifact checks are unavailable. It is a current-scope incomplete gate, not a descriptor failure. The integration source and limits are in [`docs/integration/pinned-toolkit.md`](docs/integration/pinned-toolkit.md).
