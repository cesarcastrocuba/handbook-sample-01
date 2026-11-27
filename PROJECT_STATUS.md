# Project status

This file is the only source of current status. Decisions live in [`DECISIONS.md`](DECISIONS.md); scope lives in the [editorial brief](docs/editorial/brief.md) and [outline](docs/editorial/outline.md).

## Phase

Published and in maintenance. Gates 1, 2 and 3 are approved. `v0.5.2` is the latest published release: Introduction, Chapters 1–8, Appendices A–C and References. It was published on 2026-11-15 by run `43741672481` from commit `bc31c8f`, with seven assets, and the hub catalog lists it. Edition `0.6.0` is prepared for review, not published (`DEC-032`, Proposed).

## Gates

| Gate | State | Evidence |
| --- | --- | --- |
| 1 — editorial brief | **Approved**, 2026-11-06 | [`docs/editorial/brief.md`](docs/editorial/brief.md) |
| 2 — outline | **Approved**, 2026-11-06 | [`docs/editorial/outline.md`](docs/editorial/outline.md) |
| 3 — pilot section | **Approved**, 2026-11-06 (delegated owner, `HUB-DEC-016`) | [`manuscript/chapters/ch02-editorial-contract.qmd`](manuscript/chapters/ch02-editorial-contract.qmd) and its [scope proposal](sdd/changes/0003-pilot-2-2/scope.md) |

Gate state is machine-readable in [`docs/editorial/gates.json`](docs/editorial/gates.json) and explained in [`docs/editorial/gates.md`](docs/editorial/gates.md). The owner statement and approved scope are in the [approval record](docs/editorial/approval-record.md). Gate 3 approves written work; it is not a precondition for writing the pilot. Gate values are a recorded assertion kept in step with owner decisions, not proof of authorization.

## Current state

- `0.6.0` is prepared, not published. It pins toolkit `0.16.1` at hub release candidate `aebcaae076b09a4e43f46ab863c51f9870922a16` and standard profile `1.1.0`, and moves every edition to Inter, the 85% print figure scale with whole callout boxes, and the build-time GitHub star link. The book-owned Document Control table gains the required `Version` row; publication metadata states `Prepared — not published`. The edition needs the Owner's desktop Word check and tag approval (`DEC-032`, Proposed). No release workflow has been dispatched.
- `v0.5.2` is the latest published release. It pins toolkit `0.11.0` at `d4bef53af4c70f86fecdb13d1924c79353dde32f`, with uniform surface table rows and cream rules in every edition, no page transition, compact reading-site scale and rounder controls. The release checked the deployed site's assets. No manuscript content change (`DEC-031`). The Owner inspected the CI-built `book.docx` in desktop Word and approved the tag on 2026-11-15.

- `v0.5.1` remains published as the previous edition. It upgrades to toolkit `0.10.3`: in desktop Word, Contents, the List of Tables and the List of Figures open with their entries and page numbers and can be updated with F9, and captioned tables show alternate-row banding; `v0.4.2` and `v0.5.0` showed those indexes empty until the reader pressed F9. The reading site serves its stylesheets and fonts from a path that current Pages actions publish. No manuscript content change (`DEC-030`).
- `v0.5.0` remains published. It upgrades to toolkit `0.10.1` with the reading-experience redesign, and it is the first published edition with a figure, Figure 1.1 in section 1.3, and a List of Figures (`DEC-028`, `DEC-029`).
- `v0.4.2` remains published. It upgrades to toolkit `0.9.2`, which defines each Word callout style once, makes Contents and the List of Tables native Word fields with visible cached entries, takes table banding from the table style, declares fallback fonts and removes the duplicate rule from the reading site's List of Tables page; no manuscript content change (`DEC-027`). `v0.4.1` and every older published edition remain available (hub `HUB-DEC-031`).
- `v0.2.5` remains published as the previous edition. It upgrades to toolkit `0.6.0`, which adds the Markdown edition `book.md` as a seventh release asset; manuscript content is unchanged apart from the revision history.
- `v0.2.4` remains published as the previous edition. It addresses the independent review findings on the `v0.2.0` front matter and appendices.
- `v0.2.2` was withdrawn on 2026-11-10; its release page and six assets were deleted and its tag stays at `c148518` (`DEC-020`). It had recorded the confirmed author and copyright holder, added third-party notices to the HTML edition and included the portable `mktemp` fix from PR #3.
- `v0.2.3` was withdrawn on 2026-11-10; its release page and assets were deleted and its tag stays at `7b835a5` (`DEC-019`).
- `v0.2.1` is superseded. Its release page and assets were deleted on 2026-11-09 and its tag stays, under hub decision `HUB-DEC-023`.
- Earlier editions `v0.1.0` to `v0.2.0` had their release pages and assets withdrawn; their tags stay (`DEC-016`).
- Reading site: <https://cesarcastrocuba.github.io/handbook-sample-01/>. The hub catalog is updated to a new release through a separate hub pull request.
- Toolkit `0.16.1` pinned at hub release candidate `aebcaae076b09a4e43f46ab863c51f9870922a16`, with profile `1.1.0`, Quarto `1.11.9`, qpdf 11 or later and Inter in the PDF and Word editions.
- `make full` passes for the descriptor, reading order, references and all chapters and appendices.
- `main` is protected: changes arrive through a pull request with passing CI (`DEC-015`), and a branch must be up to date with `main` before merge (hub `HUB-DEC-026`).

## Open

- Owner desktop Word acceptance of the CI-built `0.6.0` DOCX is pending before tagging; `DEC-032` is Proposed.
- The six-file description is corrected and published in `v0.2.6`; the unified design is published in `v0.2.7`; the independent review is recorded in [`docs/editorial/reviews/v0.2.6-reviews.md`](docs/editorial/reviews/v0.2.6-reviews.md). The independent content review of the `v0.2.0` front-matter and appendix changes and the visual review of the published `v0.2.2` PDF are recorded in [`docs/editorial/reviews/v0.2.4-reviews.md`](docs/editorial/reviews/v0.2.4-reviews.md).

## Next step

Complete independent review and CI, then obtain the Owner’s desktop Word acceptance of the CI-built `0.6.0` `book.docx` before tagging. The release workflow has not been dispatched.

## Verification

Run from a clean checkout:

```sh
python3 -m pip install -r requirements.txt
make check
```

`make full` runs descriptor, reading-order, cross-reference and chapter-profile validation for every chapter and appendix and passes. It does not build artifacts. The build and release contract is in [`docs/build/pipeline-spec.md`](docs/build/pipeline-spec.md); the integration source and limits are in [`docs/integration/pinned-toolkit.md`](docs/integration/pinned-toolkit.md).
