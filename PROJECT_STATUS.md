# Project status

This file is the only source of current status. Decisions live in [`DECISIONS.md`](DECISIONS.md); scope lives in the [editorial brief](docs/editorial/brief.md) and [outline](docs/editorial/outline.md).

## Phase

Sample book expansion and release preparation (platform phases 3–4). Gates 1, 2 and 3 are approved. The complete draft — Chapters 1–8, front matter, references and appendices — is written. A local `0.1.0-rc.1` six-file release candidate was built and inspected outside the repository; no release, tag or Pages deployment exists.

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
- Complete draft manuscript written: Chapters 1–8, front matter, references and appendices.
- Local `0.1.0-rc.1` release candidate built with toolkit `0.4.0`, profile `1.0.0` and Quarto `1.11.9`: six files, 57-page PDF, manifest and checksums verified outside the repository. No artifact is committed.
- Lightweight SDD proposal and task record created.
- Dependency-free repository check, gate-state policy and state-machine tests added and documented.
- Toolkit repinned to public hub main `7820172c8810ececc550d5a3604ea4045687fefd` (`0.4.0`) with profile `1.0.0`; `make full` runs descriptor, reading order, references and all chapter and appendix validators against the descriptor pin.
- Pilot 2.2 approved and retained inside Chapter 2; Chapters 1–8 complete the draft.
- CI installs the pinned toolkit and runs the fast `validate-book` check on `main`, `feat/**`, pull requests and `workflow_dispatch`.
- Content and code licensing recorded as a proposal.

## Not done, by design

- No independent review of Parts II–III or of the release pipeline.
- Toolkit `0.4.0` sets the Typst brand primary to white to suppress the chapter-title overflow; visual review shows section numbers and the note-callout border are also white in the PDF. This is a renderer-side blocker for release, not a manuscript defect.
- No committed artifact, release tag, GitHub Release, Pages deployment or catalog entry exists.
- The manual release workflow exists but has not been executed; it requires an owner dispatch and Pages configured to use GitHub Actions.
- `make full` passes descriptor, reading-order, reference and chapter validation; `git diff --check` is clean.
- GitHub repository exists and the integration changes are on `main`; no deployment, catalog entry or release has occurred.
- No change to the hub or to the existing handbook.

## Next step

Fix the toolkit `0.4.0` white-primary regression so PDF section numbers and note-callout borders remain visible, then rebuild and review the release pipeline and local release candidate. After approval, the owner may dispatch the release workflow. No merge, tag or release is authorized by this branch.

## Verification

Run from a clean checkout:

```sh
python3 -m pip install -r requirements.txt
make check
```

`make full` runs descriptor, reading-order, cross-reference and chapter-profile validation for every chapter and appendix and passes. It does not build artifacts. The build and release contract is in [`docs/build/pipeline-spec.md`](docs/build/pipeline-spec.md); the integration source and limits are in [`docs/integration/pinned-toolkit.md`](docs/integration/pinned-toolkit.md).
