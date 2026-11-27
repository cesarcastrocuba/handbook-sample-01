# Prepare sample v0.6.0

Prepare the next edition with toolkit 0.16.1, standard profile 1.1.0 and edition 0.6.0 under
`DEC-032` (Proposed). Preparation only: no tag, release or deployment.

## Applied upgrade steps (0.11.0 to 0.16.1)

- `book.yaml`: toolkit `0.16.1`, profile `1.1.0`; `requirements.txt` pins the hub toolkit 0.16.1
  tag `toolkit-v0.16.1` at `0c89c38c9375d39cc9f2747469f545ee5dd7b561`.
- Adopted the template release workflow: one `version` input, qpdf 11 PDF compaction, the
  build-time repository star count (`HANDBOOK_STAR_COUNTS`), the optional book-owned
  `release-assets` path, pre-release handling and the deployed-site check.
- Replaced `check.yml` with the template `ci.yml` (job `Fast checks`) and kept the sample-specific
  steps: the `publishing/_quarto.yml` syntax contract, `make full` for every chapter and appendix,
  and the review-only `edition-preview` artifact. The template `ci.yml` runs only `make check`.
- Added the template `build` target to the Makefile. `full` stays editorial-only (no Quarto
  needed); an artifact build is explicit, as the book documents.
- 0.14.0 Document Control rule: the book-owned `| Field | Value |` table gains
  `| Version | 0.6.0 |`, which both the preview (`0.6.0-preview` validates as `0.6.0`) and the
  final `0.6.0` build accept. This is the only forced manuscript edit.
- 0.12.0 numbering: unnumbered front matter now numbers from `0`. The Introduction's
  reading-routes table is `Table 0.1` instead of `Table 1` in the List of Tables and cross
  references; no source text changes.
- 0.16.0 typeface: every edition uses Inter and the PDF body is 9.5 pt; the Word edition embeds
  Inter and JetBrains Mono. `NOTICE.md` is updated from the Selawik/Liberation Sans/Source
  families.
- Current-state documents updated: `README.md`, `PROJECT_STATUS.md`, `docs/setup.md`,
  `docs/integration/pinned-toolkit.md`, `docs/build/pipeline-spec.md`, the editorial brief,
  outline, profile, approval record and `publishing/README.md`.
- Edition 0.6.0 metadata: `publishing/metadata.yaml` version `0.6.0`, status
  `Prepared — not published`, `build_status: prepared`; `CHANGELOG.md` and `DECISIONS.md`
  (`DEC-032`, Proposed) updated.

## Forced manuscript changes

1. `manuscript/front-matter/title.qmd`: the Document Control table gains `| Version | 0.6.0 |`
   (0.14.0 build rule). No prose changes.
2. The Introduction's reading-routes table is now labelled `Table 0.1` (0.12.0 numbering rule);
   the source caption is unchanged.

## Checks

- `make check` with the pinned toolkit in a sibling venv: 16 tests OK, repository check OK,
  `validate-book` OK.
- `make full`: descriptor, reading order, references and all eight chapters and three appendices
  OK.
- `make build OUTPUT=/tmp/opencode/sample-build`: see the pull request for PDF pages, DOCX size and
  the `pdffonts` Inter check.

## Out of scope

No tag, release or Pages deployment. `DEC-032` remains Proposed until the Owner checks the
CI-built DOCX in desktop Word and approves the tag.
