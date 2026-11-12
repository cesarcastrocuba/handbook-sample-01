# Build and release contract

| Field | Value |
| --- | --- |
| Status | Current — build and release contract |
| Scope | Platform phase 4; publication remains owner-gated |
| Book config | [`publishing/_quarto.yml`](../../publishing/_quarto.yml) |
| Release workflow | [`.github/workflows/release.yml`](../../.github/workflows/release.yml) |
| Toolkit | `0.7.0`, pinned from public hub `e34ec0272b696e7f1249ee5112124726777b75cd` |
| Profile | `standard` `1.0.0` |
| Quarto | `1.11.9` |
| Pandoc | `3.10` (bundled) |
| Typst | `0.15.1` (bundled) |
| Python | `3.12` |

This document defines the book-side contract and the Hub-side build and release flow. Current release state is in [`PROJECT_STATUS.md`](../../PROJECT_STATUS.md). Shared staging, packaging, manifest and checksum code belongs to the Hub toolkit, not this repository.

## 1. Ownership boundary

**Book repository owns**

- `publishing/_quarto.yml`: book metadata, format selection and theme.
- `manuscript/` sources, `manuscript/book.yml` reading order and `book.yaml` descriptor.
- The manual release workflow that invokes the pinned toolkit.
- Any book-specific style or reference document added later.

**Hub toolkit owns**

- staging a temporary build workspace from the exact commit;
- generating `index.qmd`, chapter wrappers and explicit table captions;
- copying the book config and sources without copying shared scripts;
- invoking Quarto once for HTML, Typst PDF and DOCX;
- inspecting each payload and normalizing the source bundle;
- writing and verifying the manifest and checksums;
- atomically exposing the complete output directory.

No manifest, checksum, zip or packaging script is added to this repository.

## 2. Toolchain

The toolkit is installed from `requirements.txt` as a non-editable package:

```text
handbook-toolkit @ git+https://github.com/cesarcastrocuba/handbooks-hub.git@e34ec0272b696e7f1249ee5112124726777b75cd#subdirectory=tools
```

`book.yaml` declares toolkit `0.7.0` and profile `standard` `1.0.0`. Toolkit `0.7.0` packages both the `0.2.0` and `1.0.0` snapshots and includes the Markdown payload introduced in `0.6.0` as a fifth artifact; `1.0.0` preserves every approved `0.2.0` rule and adds the validation classification. The toolkit resolves the packaged profile and stages its render resources: the table-layout filter, the task-checkbox filter and the breakable-callout Typst include. `publication.formats` still lists only `html`, `pdf` and `docx`: the Markdown edition is implicit, like the source bundle.

Quarto supplies its bundled Pandoc and Typst. The repository validators do not require Quarto; only `build-book` does.

## 3. Build command

Run from a clean checkout of the exact commit, with the output outside the repository:

```sh
handbook-toolkit build-book \
  --repo . \
  --commit <full-commit-sha> \
  --output /outside/repo/release-<version> \
  --version <version> \
  --mode chapter \
  --quarto "$(command -v quarto)"
```

The build refuses a dirty tree, a commit that is not the requested `HEAD`, an existing output directory and an output inside the repository. It performs one render and then inspects the produced bytes.

The verified directory contains exactly seven files:

```text
book-html.zip
book.md
book.pdf
book.docx
book-source.zip
publication-manifest.json
SHA256SUMS.txt
```

`publication-manifest.json` records the book id, version, commit, toolchain versions, source epoch, normalized build command and every payload hash. It writes manifest schema `1.1`, which lists five artifacts (`html`, `pdf`, `docx`, `markdown`, `source`). `SHA256SUMS.txt` covers the five payloads plus the manifest.

## 4. Numbering and captions

- Front matter and appendices use unnumbered H1 headings; Quarto does not add chapter numbers to them.
- Chapters are numbered by the renderer after the toolkit strips manual `N.` prefixes from staged headings.
- Table captions use Pandoc's `Table:` caption form so Quarto numbers them against the rendered chapter. The Chapter 2 brief renders as `Table 2.1`, not a position-based number.
- The toolkit converts legacy `: caption` lines into explicit bold captions for compatibility. New tables should use the Pandoc form and an explicit `{#tbl-...}` label when cross-referencing is needed.

## 5. Release workflow

[`.github/workflows/release.yml`](../../.github/workflows/release.yml) is manual (`workflow_dispatch`) and takes two inputs: `version` and `tag`. It produces every published release.

The build job:

1. checks out `github.sha` with full history and verifies the tree is clean;
2. refuses an existing tag and records the exact source commit;
3. installs Quarto `1.11.9` and verifies the version;
4. installs the pinned toolkit, then runs `make full`;
5. runs `build-book` once against the recorded commit;
6. verifies the exact seven-file membership, checksums, manifest identity and payload list, HTML and source archives, DOCX document part, Markdown edition and PDF page count;
7. creates a GitHub Release at the recorded commit with exactly those seven files;
8. extracts `book-html.zip` and uploads the result as the Pages artifact.

The deploy job uses `actions/deploy-pages` with the `github-pages` environment. The deployed HTML is extracted from the same ZIP bytes attached to the release; no second render occurs.

Prerequisites outside the repository: GitHub Pages must use the GitHub Actions source, and the owner must dispatch the workflow. The workflow does not approve editorial scope or licensing.

## 6. Release-candidate inspection

This section records the `0.1.0-rc.1` inspection and is kept as history. Current release state is in [`PROJECT_STATUS.md`](../../PROJECT_STATUS.md).

A local `0.1.0-rc.1` chapter-mode build with toolkit `0.4.0` and profile `1.0.0` produced a 57-page PDF and the six-file set outside the repository. The earlier layout fixes remain in place:

- the front matter starts with an unnumbered document-control page, with no duplicate title or subtitle;
- the Chapter 2 brief renders as `Table 2.1`;
- appendices render unnumbered with `A.1`/`B.1`/`C.1` headings.

Toolkit `0.4.0` removes the overflowing orange-book chapter-title block by setting the Typst brand primary to white. The same change makes primary-colored text and borders white: section numbers are present in the PDF text layer but invisible on the page, and the note-callout border disappears. HTML and DOCX keep visible section numbers. This is a renderer-side defect to fix in the toolkit before publication; it is not a manuscript or profile failure. The breakable-callout page split also remains. Table rows and callouts are otherwise readable, and relative HTML links resolve.

## 7. Reproducibility

- Pin Quarto, the toolkit and the profile; never use ranges or floating latest.
- Use the exact commit timestamp as `SOURCE_DATE_EPOCH`.
- Build once; publish the verified bytes without a second render.
- PDF and DOCX may contain generator metadata. Do not claim bit-identical rebuilds without a recorded second build and comparison.

## 8. Local verification

```sh
python3 -m pip install -r requirements.txt
make full
git diff --check
```

`make full` validates the descriptor, reading order, references and every chapter and appendix. It does not build artifacts. The release workflow repeats the full gates before `build-book`.
