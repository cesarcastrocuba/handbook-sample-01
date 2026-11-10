# Project status

This file is the only source of current status. Decisions live in [`DECISIONS.md`](DECISIONS.md); scope lives in the [editorial brief](docs/editorial/brief.md) and [outline](docs/editorial/outline.md).

## Phase

Published and in maintenance. Gates 1, 2 and 3 are approved. `v0.2.4` is the latest published release: Introduction, Chapters 1–8, Appendices A–C and References. It was published on 2026-11-10 by run `42810374270` from commit `cd99d7a`.

## Gates

| Gate | State | Evidence |
| --- | --- | --- |
| 1 — editorial brief | **Approved**, 2026-11-06 | [`docs/editorial/brief.md`](docs/editorial/brief.md) |
| 2 — outline | **Approved**, 2026-11-06 | [`docs/editorial/outline.md`](docs/editorial/outline.md) |
| 3 — pilot section | **Approved**, 2026-11-06 (delegated owner, `HUB-DEC-016`) | [`manuscript/chapters/ch02-editorial-contract.qmd`](manuscript/chapters/ch02-editorial-contract.qmd) and its [scope proposal](sdd/changes/0003-pilot-2-2/scope.md) |

Gate state is machine-readable in [`docs/editorial/gates.json`](docs/editorial/gates.json) and explained in [`docs/editorial/gates.md`](docs/editorial/gates.md). The owner statement and approved scope are in the [approval record](docs/editorial/approval-record.md). Gate 3 approves written work; it is not a precondition for writing the pilot. Gate values are a recorded assertion kept in step with owner decisions, not proof of authorization.

## Current state

- `v0.2.4` is the latest published release. It addresses the independent review findings on the `v0.2.0` front matter and appendices.
- `v0.2.2` is withdrawn. Its withdrawal is authorized by `DEC-020`, its tag is kept, and its release page and six assets are deleted by the coordinator after this change merges. It recorded the confirmed author and copyright holder, added third-party notices to the HTML edition and included the portable `mktemp` fix from PR #3.
- `v0.2.3` was withdrawn on 2026-11-10; its release page and assets were deleted and its tag stays at `7b835a5` (`DEC-019`).
- `v0.2.1` is superseded. Its release page and assets were deleted on 2026-11-09 and its tag stays, under hub decision `HUB-DEC-023`.
- Earlier editions `v0.1.0` to `v0.2.0` had their release pages and assets withdrawn; their tags stay (`DEC-016`).
- Reading site: <https://cesarcastrocuba.github.io/handbook-sample-01/>. The hub catalog is updated to a new release through a separate hub pull request.
- Toolkit `0.5.0` pinned at hub `4e006be3bb497a1f468235895ae7c79d6d176aaa`, with profile `1.0.0` and Quarto `1.11.9`.
- `make full` passes for the descriptor, reading order, references and all chapters and appendices.
- `main` is protected: changes arrive through a pull request with passing CI (`DEC-015`), and a branch must be up to date with `main` before merge (hub `HUB-DEC-026`).

## Open

- None. The independent content review of the `v0.2.0` front-matter and appendix changes and the visual review of the published `v0.2.2` PDF are completed and recorded in [`docs/editorial/reviews/v0.2.4-reviews.md`](docs/editorial/reviews/v0.2.4-reviews.md).

## Next step

Any further release needs owner authorization.

## Verification

Run from a clean checkout:

```sh
python3 -m pip install -r requirements.txt
make check
```

`make full` runs descriptor, reading-order, cross-reference and chapter-profile validation for every chapter and appendix and passes. It does not build artifacts. The build and release contract is in [`docs/build/pipeline-spec.md`](docs/build/pipeline-spec.md); the integration source and limits are in [`docs/integration/pinned-toolkit.md`](docs/integration/pinned-toolkit.md).
