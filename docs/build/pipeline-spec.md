# Phase 4 build and render contract

| Field | Value |
| --- | --- |
| Status | Technical preparation — no publication |
| Scope | Platform phases 1–4; phases 5–6 deferred by owner |
| Book config | [`publishing/_quarto.yml`](../../publishing/_quarto.yml) |
| Quarto | `1.11.9` |
| Pandoc | `3.10.0` (bundled) |
| Typst | `0.15.1` (bundled) |
| Dart Sass | `1.101.0` (bundled) |
| Deno | `2.9.8` (bundled) |
| Python | `3.12` |
| Toolkit | `0.1.0`, pinned from public hub |

This document defines the minimal book-side contract and the Hub-side render steps. It does not claim a published release. Shared staging, packaging, manifest and checksum code belongs to the Hub toolkit, not this repository.

## 1. Ownership boundary

**Book repository owns**

- `publishing/_quarto.yml`: book metadata, format selection, theme and numbering policy.
- `manuscript/` sources, `manuscript/book.yml` reading order and `book.yaml` descriptor.
- Any book-specific style or reference document added later.

**Hub toolkit owns**

- staging a temporary build workspace;
- generating `index.qmd` and chapter wrappers from the descriptor and reading order;
- copying the book config and sources without copying shared scripts;
- invoking Quarto once for all formats;
- normalizing the source bundle, manifest and checksums;
- verifying artifact presence, captions, links and checksums;
- release and catalog publication, which remain owner-gated.

No manifest, checksum, zip or packaging script is added to this repository.

## 2. Verified toolchain

Installed and verified locally:

```text
quarto 1.11.9
pandoc 3.10.0
typst 0.15.1
Dart Sass 1.101.0
Deno 2.9.8
python 3.12
```

Official references:

- Quarto 1.11.9 release: <https://github.com/quarto-dev/quarto-cli/releases/tag/v1.11.9>
- Book structure and required `index.qmd`: <https://quarto.org/docs/books/book-structure.html>
- Render command and `--output-dir`/`--to`: <https://quarto.org/docs/cli/render.html>
- PDF and Typst options: <https://quarto.org/docs/reference/formats/pdf.html>
- DOCX options: <https://quarto.org/docs/reference/formats/docx.html>

Install the pinned Linux arm64 package and verify it before use:

```sh
curl -fLO https://github.com/quarto-dev/quarto-cli/releases/download/v1.11.9/quarto-1.11.9-linux-arm64.deb
curl -fLO https://github.com/quarto-dev/quarto-cli/releases/download/v1.11.9/quarto-1.11.9-checksums.txt
# Verify the arm64.deb line before installing.
grep 'quarto-1.11.9-linux-arm64.deb' quarto-1.11.9-checksums.txt
sha256sum --check --ignore-missing quarto-1.11.9-checksums.txt
sudo dpkg -i quarto-1.11.9-linux-arm64.deb
quarto --version
quarto check
```

Do not use a floating latest Quarto. CI should install the same pinned release and verify its checksum.

## 3. Staged workspace

The Hub build creates a temporary directory, for example:

```text
build/
  _quarto.yml          # copied from publishing/_quarto.yml
  index.qmd            # generated title page, no chapter prose
  chapters/
    02-editorial-contract.qmd
  manuscript/          # copied sources as needed
```

Rules:

- `index.qmd` is generated from `book.yaml` title metadata because Quarto books require a home page.
- Chapter wrappers provide the chapter heading and assembly boundary; source section files remain unchanged.
- For standalone pilot preview, the staged copy replaces front-matter `title` with `pagetitle` so the visible H2 is not duplicated by a metadata title block.
- For the assembled book, the chapter wrapper owns the chapter title; section headings keep their manual `N.M` numbers.
- `number-sections: false` is intentional. Manual numbers are the only numbering source; the renderer must not add a second chapter or section number.
- If a chapter wrapper is used, mark its H1 `.unnumbered` until the numbering policy is proven in all three formats.

## 4. Render commands

From the staged workspace, with the approved commit timestamp:

```sh
export SOURCE_DATE_EPOCH="$(git -C /path/to/book show -s --format=%ct <approved-commit>)"
quarto check
quarto render --no-execute
```

`quarto render` uses all formats in `_quarto.yml`, producing:

| Artifact | Source |
| --- | --- |
| HTML book site | `_output/index.html` and assets |
| PDF | `_output/Handbook-Authoring-and-Publishing.pdf` via Typst |
| DOCX | `_output/Handbook-Authoring-and-Publishing.docx` |
| Source bundle | Hub-generated archive of the approved commit and build inputs |
| Manifest | Hub-generated `publication-manifest.json` |
| Checksums | Hub-generated `SHA256SUMS.txt` |

Individual formats may be checked with `quarto render --no-execute --to html`, `--to typst` and `--to docx`. `--to typst` is the PDF path; `format: pdf` with a bare `pdf-engine: typst` failed locally because the bundled Typst binary is not on `PATH`.

## 5. Artifact naming and manifest

Proposed release asset names:

```text
handbook-authoring-and-publishing-<version>-html.zip
handbook-authoring-and-publishing-<version>.pdf
handbook-authoring-and-publishing-<version>.docx
handbook-authoring-and-publishing-<version>-source.zip
publication-manifest.json
SHA256SUMS.txt
```

The manifest follows the Hub publication contract and records:

- book id, version and approved commit SHA;
- toolkit `0.1.0`, profile `standard` `0.2.0`;
- Quarto `1.11.9`, Pandoc `3.10.0`, Typst `0.15.1`, Dart Sass `1.101.0`, Deno `2.9.8`, Python `3.12`;
- `SOURCE_DATE_EPOCH` and exact render command;
- every artifact path, byte size, media type and SHA-256;
- which artifacts are bit-identical across rebuilds and which are semantically verified only.

`SHA256SUMS.txt` covers the four artifacts plus `publication-manifest.json`. The manifest does not hash itself.

## 6. Reproducibility

- Pin Quarto and toolkit versions; never use ranges or floating latest.
- Use the approved commit timestamp for `SOURCE_DATE_EPOCH`.
- Build once; package and publish the same bytes.
- Normalize archive entry order and timestamps in the Hub source-bundle step.
- PDF and DOCX may contain generator metadata; run a second build and record bit-identical versus semantic equivalence. Do not claim bit-for-bit identity without evidence.

## 7. Layout findings from the pilot preview

These are render-contract findings, not Gate 3 text rejection:

1. **Duplicate visible title.** A section source with front-matter `title` plus an H2 duplicates the title in standalone/book renders. Staging must map the section title to `pagetitle` for preview, or let the chapter wrapper own the title. No pilot prose change is required.
2. **Manual plus automatic numbering.** Quarto book defaults add chapter/section numbers even when headings already contain `N.M`. The renderer must enforce one numbering source; `number-sections: false` plus unnumbered chapter H1 is the candidate policy and must be tested in HTML/PDF/DOCX.
3. **Table widths.** The brief table renders 50/50, cramping the decision column. The shared renderer should apply content-aware widths, for example an explicit `[20, 80]` policy for two-column key/value tables, or a documented per-table width attribute. No per-book filter is added here.
4. **Table caption.** The caption exists in HTML but is absent in the Typst PDF text extraction. The shared renderer must verify the actual PDF caption and provide a workaround if Typst continues to drop it.
5. **Callout pagination.** Common Pitfall and Decision & Trade-off blocks leave large blank areas because a callout is unbreakable. The shared renderer must configure or test breakable callouts; do not accept half-empty pages.
6. **Checkbox glyphs.** The PDF preview shows a boxed mark rather than a clearly empty checkbox for `- [ ]` items. The shared renderer must verify readable empty-box glyphs or substitute an accessible marker.

## 8. Limits

- No semantic manuscript validator or profile-conformance validator exists in toolkit `0.1.0`.
- No artifact manifest, checksum file or source bundle is produced by this branch.
- No publication, Pages deployment, release or catalog entry is authorized.
- No chapter beyond the reviewed pilot is written.
