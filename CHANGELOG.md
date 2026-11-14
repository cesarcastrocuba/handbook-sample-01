# Changelog

All notable changes to this sample handbook are recorded here. The format follows Keep a Changelog; versions follow semantic versioning once releases begin.

## [Unreleased]

## [0.5.0] - 2026-11-14

### Added

- Figure 1.1, an original lifecycle diagram in section 1.3, so the figure path is exercised in every edition: a figures page on the reading site, a List of Figures in PDF and Word, and the caption in the Markdown edition.

### Changed

- Reading site: a cover page with the edition and a "Start reading" link; the sidebar groups the book into parts; every page carries an edition footer; list pages (tables, figures) are ordinary pages with search and navigation; favicon and social metadata; subtle motion that is disabled when the reader prefers reduced motion. The book theme is generated from the design tokens.
- Word and PDF: a List of Figures when the book has figures.
- Built with hub toolkit `0.10.0` at commit `dcfd8c8`; the dark web theme moves to `cosmo`, as the toolkit upgrade note requires.

## [0.4.2] - 2026-11-14

### Changed

- Word callout titles are bold and coloured, because each callout style is now defined once.
- Contents and the List of Tables are real Word fields that update, and they show their entries in viewers that do not update fields.
- Table banding comes from the table style, and the document declares fallback fonts.
- The List of Tables page on the reading site shows one rule under its title instead of two.
- Built with hub toolkit `0.9.2` at commit `2e29438`, which fixes the Word style definitions, replaces the static List of Tables with native contents and caption fields, and removes the duplicate title rule.
- No manuscript content change.

## [0.4.1] - 2026-11-13

### Changed

- Section 2.2 closing callouts now use the warning and important roles, matching the rest of the book.
- Every Review Checklist callout carries the neutral review role, rendered grey in HTML, PDF and DOCX.
- The List of Tables link moved from the top navigation to the book sidebar below Document Control.
- Built with hub toolkit `0.9.1` at commit `298d703`, which aligns the hub and book width and rebuilds the Word callouts, table alignment and licence blocks.

## [0.4.0] - 2026-11-13

Published 2026-11-13 by run `43428501092` from commit `12f8d46`. Built with hub toolkit `0.9.0` at commit `e6c18d0`.

### Changed

- The hub and book web chrome now share the compact scale, 1040 px navigation, Pages library link and a dedicated List of Tables page.
- Callouts use one palette across HTML, PDF and DOCX; PDF callouts never split and Word boxes keep together.
- PDF and Word use the cream canvas and alternating table rows; Word captions are centered and the outer table border is gone. Word has a static List of Tables.
- No manuscript content change.

## [0.3.0] - 2026-11-13

Published 2026-11-13 by run `43342066827` from commit `3322411`. Built with hub toolkit `0.8.0` at commit `9921dbe`.

### Changed

- Editorial type system upgraded to Source Sans 3 for text and Source Serif 4 for headings across
  HTML, PDF and DOCX.
- Reading site gains the generated book chrome and a List of Tables; PDF captions and table
  numbering are chapter-based and the List of Tables is present.
- DOCX gains Contents, page breaks, teal table headers, callout styles and a List of Tables field.
- No manuscript content change.


## [0.2.7] - 2026-11-12

Published 2026-11-12 by run `43290998984` from commit `49f2209`. Built with hub toolkit `0.7.0` at commit `e34ec02` (tag `toolkit-v0.7.0`).

### Changed

- Reading site and downloads upgraded to the unified design: Liberation Sans as the brand typeface,
  self-hosted WOFF2 with OFL notices, a generated light/dark theme, full-book search, a report-an-issue
  action, and source and downloads links in the navigation.
- PDF and DOCX editions use the same token palette; the DOCX names Arial as the metric-compatible
  family and JetBrains Mono for code.
- No manuscript content change: the edition carries the same Introduction, Chapters 1-8, Appendices
  A-C and References as `v0.2.6`.

## [0.2.6] - 2026-11-11

Published 2026-11-11 by run `43063144576` from commit `1d73db9`. Built with hub toolkit `0.6.0` at commit `c200fd2`.

### Fixed

- Corrected the description of a release to seven files, including the Markdown edition, in Chapter 7, Appendix B and Appendix C.

## [0.2.5] - 2026-11-11

Published 2026-11-11 by run `42989074637` from commit `c8c8703`. Built with hub toolkit `0.6.0` at commit `c200fd2`.

### Changed

- Built with toolkit 0.6.0; adds the Markdown edition (`book.md`) to the release. No manuscript content change other than the revision history.

## [0.2.4] - 2026-11-10

Published 2026-11-10 by run `42810374270` from commit `cd99d7a`. Built with hub toolkit `0.5.0` at commit `4e006be`.

### Added

- Added reusable gate checklists for Brief, Outline, Pilot, and Release gates to Appendix B (B.1).
- Added an Approval record block to both the brief and outline templates in Appendix A (A.1).
- Added glossary definitions for "Release" and "Verified artifact set" to Appendix C (C.1).

### Changed

- Updated Appendix C.2 worked example to use the refined definitions of release and verified artifact set.
- Clarified product-name convention in Introduction to distinguish checkable toolchain prerequisites and citations from illustrative examples.

### Fixed

- Clarified Appendix B.1 example to base changes-requested verdict on insufficient claim support rather than secondary-source tier alone.
- Removed premature claims in Chapter 7 that the book has not been released or deployed, resolving conflict with Document Control version history.

### Verified

- Recorded independent reviews in [`docs/editorial/reviews/v0.2.4-reviews.md`](docs/editorial/reviews/v0.2.4-reviews.md): the content review of v0.2.0 front matter and appendices (verdict CHANGES_REQUESTED, resolved in PR #8) and the visual review of the published v0.2.2 PDF (all 55 pages compared with HTML edition; verdict APPROVE with no defects and section numbers visible).

## [0.2.3] - 2026-11-10

Withdrawn 2026-11-10. Built by mistake from `7b835a5` before the corrections merged; it carried the v0.2.2 manuscript under the 0.2.3 label. The release page and assets were deleted and the tag stays (`DEC-019`).

## [0.2.2] - 2026-11-09

Withdrawn 2026-11-10 (`DEC-020`). The release page and assets are deleted and the tag stays.

Published 2026-11-09 by run `42621799383` from commit `c148518`. Built with hub toolkit `0.5.0` at commit `4e006be`.

### Changed

- Named Franz César Castro Cuba as author and copyright holder, replacing the placeholder attribution.
- Added a Third-Party Notices page to the HTML edition, listing the Quarto `site_libs` libraries with their versions, copyright lines and licenses, and reproducing the full MIT and Apache-2.0 texts.
- `v0.2.1` is superseded; its release page and assets were deleted on 2026-11-09 and its tag stays (`HUB-DEC-023`).

### Fixed

- Made the `full` target's temporary profile file portable across GNU and BSD/macOS `mktemp`, removed the rename race and cleaned up the temporary directory on exit and termination (PR #3).

## [0.2.1] - 2026-11-08

Built with hub toolkit `0.5.0` at commit `4e006be`.

### Changed

- JetBrains Mono replaces Cascadia Code, Liberation Sans is supplied by the toolkit and the DOCX template is regenerated.
- Brought the status, decision log, notice and descriptor in line with the published releases.

### Removed

- Withdrew the release pages and assets of `v0.1.0` to `v0.2.0`. Their tags remain.

## [0.2.0] - 2026-11-07

Built from `afa3d21` with hub toolkit commit `5f96202`.

### Changed

- Replaced the Preface and Reading Paths with an Introduction chapter and reworked Document Control.
- Numbered appendix subsections consecutively after the first section.
- Print layout updated through the toolkit pin; removed a link that left the book.

## [0.1.2] - 2026-11-07

Built from `ea8d6a5` with hub toolkit commit `62e37ab`.

### Changed

- Bundled Selawik and Cascadia Code fonts and black headings, through the toolkit pin.

## [0.1.1] - 2026-11-07

Built from `f0a508e` with hub toolkit commit `988773c`.

### Fixed

- Heading and table-of-contents rendering, through the toolkit pin and the Typst table-of-contents depth.

## [0.1.0] - 2026-11-06

First published edition, built from `2009966` with hub toolkit commit `7820172`. The entries below record the work before it.

### Added

- Bootstrap scaffold for the sample handbook *Handbook Authoring and Publishing*.
- Agent-neutral roles, editorial gates and contribution workflow.
- Proposed editorial brief, outline and content profile.
- Lightweight SDD proposal for the bootstrap.
- Dependency-free repository consistency check.

### Changed

- Replaced the separate Preface and Reading Paths with a single Introduction chapter covering purpose, objectives, scope, audience, structure, task-based routes and conventions.
- Reworked Document Control to keep only human-maintained ownership, version history, maintenance and licensing; generated edition fields are supplied by the toolkit at build time.
- Numbered appendix subsections consecutively after the first section (`A.2`–`A.3`, `B.2`–`B.3`, `C.2`–`C.3`) to match chapter numbering, without touching headings inside template code blocks.

### Fixed

- Removed the Gate 3 deadlock: Gates 1 and 2 now authorize the pilot file while Gate 3 is pending; Gate 3 approves the reviewed pilot and authorizes expansion.
- The check enforces only the pilot file boundary and gate ordering; section 2.2 scope and owner authorization remain review responsibilities.
- Corrected documentation and check output that overstated file-level enforcement as section-level or proof of owner authorization.
- Gate state is machine-readable in `docs/editorial/gates.json`, explained in `docs/editorial/gates.md`, and enforced by state-machine tests.
- Pinned public-hub toolkit integration via direct Git requirement at full SHA `0e8d897acae67d55eb09bf06a6e890d07d187779` with `#subdirectory=tools`.
- Draft `book.yaml` and empty `manuscript/book.yml`; profile reference is `standard` `0.2.0`, contingent on hub branch approval.
- CI installs the pinned toolkit and runs the fast `validate-book` check; `make full` fails explicitly until pilot, content validation and artifacts exist.
