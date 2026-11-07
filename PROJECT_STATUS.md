# Project status

This file is the only source of current status. Decisions live in [`DECISIONS.md`](DECISIONS.md); scope lives in the [editorial brief](docs/editorial/brief.md) and [outline](docs/editorial/outline.md).

## Phase

Sample book maintenance. Gates 1, 2 and 3 are approved. The book is published from this repository: Introduction, Chapters 1–8, Appendices A–C and References. This branch reworks the front matter and appendix subsection numbering; it does not create a release.

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
- Complete book written: Introduction, Chapters 1–8, Appendices A–C and References.
- Front matter consolidated into an Introduction chapter; Document Control now carries only human-maintained ownership, version history, maintenance and licensing. Appendix subsections use consecutive numbering.
- Local `0.1.0-rc.1` release candidate built with toolkit `0.4.0`, profile `1.0.0` and Quarto `1.11.9`: six files, 57-page PDF, manifest and checksums verified outside the repository. Published editions are built from approved commits.
- Lightweight SDD proposal and task record created.
- Dependency-free repository check, gate-state policy and state-machine tests added and documented.
- Toolkit pinned from public hub main `62e37ab6ac381a914ca7839c759405c87655dcef` (`0.4.0`) with profile `1.0.0`; `make full` runs descriptor, reading order, references and all chapter and appendix validators against the descriptor pin.
- Pilot 2.2 approved and retained inside Chapter 2; Chapters 1–8 complete the draft.
- CI installs the pinned toolkit and runs the fast `validate-book` check on `main`, `feat/**`, pull requests and `workflow_dispatch`.
- Content and code licensing recorded as a proposal.

## Not done, by design

- No independent review of this front matter change.
- Visual review of the current PDF renderer, including section-number visibility, remains open.
- No release is created by this branch.
- The manual release workflow remains the release path; this branch does not run it.
- `make full` passes the descriptor, reading order, references and chapters. The pinned validator rejects the letter-prefixed appendix headings (`A.2`, `B.2`, `C.2`), reporting 17 problems per appendix; the numbering is retained and the validator fix is an open gap. `git diff --check` is clean.
- No change to the hub or to the existing handbook.

## Next step

Fix the toolkit validator so it strips letter-prefixed appendix numbers (`A.2`, `B.2`, `C.2`) like it strips numeric chapter numbers, then review the Introduction, Document Control and appendix numbering change. No merge or release is authorized by this branch.

## Verification

Run from a clean checkout:

```sh
python3 -m pip install -r requirements.txt
make check
```

`make full` runs descriptor, reading-order, cross-reference and chapter-profile validation for every chapter and appendix and passes. It does not build artifacts. The build and release contract is in [`docs/build/pipeline-spec.md`](docs/build/pipeline-spec.md); the integration source and limits are in [`docs/integration/pinned-toolkit.md`](docs/integration/pinned-toolkit.md).
