# Project status

This file is the only source of current status. Decisions live in [`DECISIONS.md`](DECISIONS.md); scope lives in the [editorial brief](docs/editorial/brief.md) and [outline](docs/editorial/outline.md).

## Phase

Sample book bootstrap (platform phase 3). Gates 1 and 2 are approved; Gate 3 is pending. Pilot section 2.2 is written and independently reviewed; awaiting owner approval. No other manuscript prose exists.

## Gates

| Gate | State | Evidence |
| --- | --- | --- |
| 1 — editorial brief | **Approved**, 2026-11-06 | [`docs/editorial/brief.md`](docs/editorial/brief.md) |
| 2 — outline | **Approved**, 2026-11-06 | [`docs/editorial/outline.md`](docs/editorial/outline.md) |
| 3 — pilot section | **Pending**, not approved; pilot 2.2 written, awaiting review | [`manuscript/chapters/ch02-editorial-contract.qmd`](manuscript/chapters/ch02-editorial-contract.qmd) and its [scope proposal](sdd/changes/0003-pilot-2-2/scope.md) |

Gate state is machine-readable in [`docs/editorial/gates.json`](docs/editorial/gates.json) and explained in [`docs/editorial/gates.md`](docs/editorial/gates.md). The owner statement and approved scope are in the [approval record](docs/editorial/approval-record.md). Gate 3 approves written work; it is not a precondition for writing the pilot. Gate values are a recorded assertion kept in step with owner decisions, not proof of authorization.

## Completed in this bootstrap

- Local Git repository initialized on `main`.
- Agent-neutral roles and workflow defined in [`AGENTS.md`](AGENTS.md).
- Editorial brief and outline approved at Gates 1 and 2 on 2026-11-06, including the broad technical/software audience, full eight-chapter goal and standard `0.2.0` direction.
- Manuscript and publishing layouts established; only the pilot section contains prose. No artifact build is claimed.
- Lightweight SDD proposal and task record created.
- Dependency-free repository check, gate-state policy and state-machine tests added and documented.
- Pinned public-hub toolkit integration: `requirements.txt` uses a direct Git requirement at full SHA `0e8d897acae67d55eb09bf06a6e890d07d187779` with `#subdirectory=tools`; `book.yaml` and `manuscript/book.yml` are draft metadata, and the reading order now lists only the pilot.
- Pilot section 2.2 written at `manuscript/chapters/ch02-editorial-contract.qmd`; chapter-level pilot scope is proposed, not owner-approved.
- CI installs the pinned toolkit and runs the fast `validate-book` check on `main`, `feat/**`, pull requests and `workflow_dispatch`.
- Content and code licensing recorded as a proposal.

## Not done, by design

- Pilot not approved; no other chapter prose exists.
- No Quarto configuration or build; Quarto is not installed in the bootstrap environment.
- No artifact validation yet. `make full` is a current-scope incomplete artifact gate: the descriptor/reading-order check passes, but no artifact manifest or checksums exist. This is not a descriptor failure.
- No HTML, PDF, DOCX, site output or release.
- GitHub repository exists and the integration branch is pushed; the reviewed integration and onboarding changes are integrated into `main`; no deployment, catalog entry or release has occurred.
- No change to the hub or to the existing handbook.

## Next step

The owner reviews pilot section 2.2 and the independent review record. Gate 3 remains pending until owner approval. Expansion is not authorized.

## Verification

Run from a clean checkout:

```sh
python3 -m pip install -r requirements.txt
make check
```

`make full` intentionally fails and states which full-manuscript and artifact checks are unavailable. It is a current-scope incomplete gate, not a descriptor failure. The integration source and limits are in [`docs/integration/pinned-toolkit.md`](docs/integration/pinned-toolkit.md).
