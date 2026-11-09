# Changelog

All notable changes to this sample handbook are recorded here. The format follows Keep a Changelog; versions follow semantic versioning once releases begin.

## [Unreleased]

## [0.2.2] - 2026-11-09

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
