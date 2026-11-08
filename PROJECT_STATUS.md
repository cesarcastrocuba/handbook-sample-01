# Project status

This file is the only source of current status. Decisions live in [`DECISIONS.md`](DECISIONS.md); scope lives in the [editorial brief](docs/editorial/brief.md) and [outline](docs/editorial/outline.md).

## Phase

Published and in maintenance. Gates 1, 2 and 3 are approved. The latest release is `v0.2.0`: Introduction, Chapters 1–8, Appendices A–C and References.

## Gates

| Gate | State | Evidence |
| --- | --- | --- |
| 1 — editorial brief | **Approved**, 2026-11-06 | [`docs/editorial/brief.md`](docs/editorial/brief.md) |
| 2 — outline | **Approved**, 2026-11-06 | [`docs/editorial/outline.md`](docs/editorial/outline.md) |
| 3 — pilot section | **Approved**, 2026-11-06 (delegated owner, `HUB-DEC-016`) | [`manuscript/chapters/ch02-editorial-contract.qmd`](manuscript/chapters/ch02-editorial-contract.qmd) and its [scope proposal](sdd/changes/0003-pilot-2-2/scope.md) |

Gate state is machine-readable in [`docs/editorial/gates.json`](docs/editorial/gates.json) and explained in [`docs/editorial/gates.md`](docs/editorial/gates.md). The owner statement and approved scope are in the [approval record](docs/editorial/approval-record.md). Gate 3 approves written work; it is not a precondition for writing the pilot. Gate values are a recorded assertion kept in step with owner decisions, not proof of authorization.

## Current state

- Releases: `v0.1.0` (2026-11-06), `v0.1.1`, `v0.1.2` and `v0.2.0` (2026-11-07). `v0.2.0` was built from `afa3d21`; its PDF has 50 pages.
- Reading site: <https://cesarcastrocuba.github.io/handbook-sample-01/>. The hub catalog lists `v0.2.0`.
- Toolkit pinned at hub `5f9620237b61c0a01803f6705604c1c738ccee10`, which reports `0.4.0`, with profile `1.0.0` and Quarto `1.11.9`.
- `make full` passes for the descriptor, reading order, references and all chapters and appendices.
- `main` is protected: changes arrive through a pull request with passing CI (`DEC-015`).

## Open

- Owner confirmation of `DEC-012` and `DEC-013`.
- Owner decision on the third-party fonts in published editions, tracked by the hub in `HUB-DEC-020`.
- Visual review of the published PDF, including section-number visibility.
- No independent review is on record for the front-matter and appendix changes released in `v0.2.0`.

## Next step

After hub change `0010-post-phase4-remediation` is merged, move the toolkit pin to `0.5.0` in its own pull request. A new release needs owner authorization.

## Verification

Run from a clean checkout:

```sh
python3 -m pip install -r requirements.txt
make check
```

`make full` runs descriptor, reading-order, cross-reference and chapter-profile validation for every chapter and appendix and passes. It does not build artifacts. The build and release contract is in [`docs/build/pipeline-spec.md`](docs/build/pipeline-spec.md); the integration source and limits are in [`docs/integration/pinned-toolkit.md`](docs/integration/pinned-toolkit.md).
