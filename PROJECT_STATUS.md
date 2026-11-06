# Project status

This file is the only source of current status. Decisions live in [`DECISIONS.md`](DECISIONS.md); scope lives in the [editorial brief](docs/editorial/brief.md) and [outline](docs/editorial/outline.md).

## Phase

Sample book expansion (platform phase 3). Gates 1, 2 and 3 are approved. Part I — Chapters 1–3 — is drafted; later parts remain separate reviewed batches.

## Gates

| Gate | State | Evidence |
| --- | --- | --- |
| 1 — editorial brief | **Approved**, 2026-11-06 | [`docs/editorial/brief.md`](docs/editorial/brief.md) |
| 2 — outline | **Approved**, 2026-11-06 | [`docs/editorial/outline.md`](docs/editorial/outline.md) |
| 3 — pilot section | **Approved**, 2026-11-06 (delegated owner, `HUB-DEC-016`) | [`manuscript/chapters/ch02-editorial-contract.qmd`](manuscript/chapters/ch02-editorial-contract.qmd) and its [scope proposal](sdd/changes/0003-pilot-2-2/scope.md) |

Gate state is machine-readable in [`docs/editorial/gates.json`](docs/editorial/gates.json) and explained in [`docs/editorial/gates.md`](docs/editorial/gates.md). The owner statement and approved scope are in the [approval record](docs/editorial/approval-record.md). Gate 3 approves written work; it is not a precondition for writing the pilot. Gate values are a recorded assertion kept in step with owner decisions, not proof of authorization.

## Completed in this bootstrap

- Local Git repository initialized on `main`.
- Agent-neutral roles and workflow defined in [`AGENTS.md`](AGENTS.md).
- Editorial brief and outline approved at Gates 1 and 2 on 2026-11-06, including the broad technical/software audience, full eight-chapter goal and standard `0.2.0` direction.
- Part I manuscript drafted: Chapter 1, the full Chapter 2 around the approved 2.2 pilot, and Chapter 3. No artifact build is claimed.
- Lightweight SDD proposal and task record created.
- Dependency-free repository check, gate-state policy and state-machine tests added and documented.
- Toolkit repinned to public hub main `477d7042faa385eee677ad2db5198ebcf5dd1fee`; `make full` runs descriptor, reading order, references and all chapter validators.
- Pilot 2.2 approved and retained inside Chapter 2; Chapters 1 and 3 complete Part I.
- CI installs the pinned toolkit and runs the fast `validate-book` check on `main`, `feat/**`, pull requests and `workflow_dispatch`.
- Content and code licensing recorded as a proposal.

## Not done, by design

- Part II and Part III are not written.
- No Quarto configuration or build; Quarto is not installed in the bootstrap environment.
- No artifact build or validation yet. `make full` passes descriptor, reading-order, reference and chapter validation; no artifact manifest or checksums exist.
- No HTML, PDF, DOCX, site output or release.
- GitHub repository exists and the integration branch is pushed; the reviewed integration and onboarding changes are integrated into `main`; no deployment, catalog entry or release has occurred.
- No change to the hub or to the existing handbook.

## Next step

Part I is ready for independent review. Part II follows on a separate branch after review.

## Verification

Run from a clean checkout:

```sh
python3 -m pip install -r requirements.txt
make check
```

`make full` runs descriptor, reading-order, cross-reference and chapter-profile validation and passes. It does not build artifacts. The integration source and limits are in [`docs/integration/pinned-toolkit.md`](docs/integration/pinned-toolkit.md).
