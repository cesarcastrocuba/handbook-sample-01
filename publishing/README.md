# Publishing

This directory holds the book-side Quarto configuration and publication metadata. Generated artifacts are never committed. Shared staging, packaging, manifest and checksum logic belongs to the Hub toolkit.

## Current state

- [`_quarto.yml`](_quarto.yml) is the book-side config consumed by the Hub build in an isolated staged workspace. It is not rendered directly from the repository root.
- [`metadata.yaml`](metadata.yaml) records provisional publication metadata.
- The full render contract, pinned toolchain, artifact names and current layout findings are in [`docs/build/pipeline-spec.md`](../docs/build/pipeline-spec.md).
- No release, Pages deployment, catalog entry, manifest or checksum file exists.

## Render boundary

The book repository owns book metadata, format selection, theme and numbering policy. The Hub toolkit owns staging, `index.qmd` and chapter-wrapper generation, one render invocation, packaging, the manifest and checksums.

Quarto `1.11.9` renders HTML, Typst PDF and DOCX from the staged workspace. The source bundle, manifest and `SHA256SUMS.txt` are Hub outputs, not book scripts.

## Constraints

- Generated artifacts are never committed; see [`.gitignore`](../.gitignore).
- The toolkit is installed from the Hub at a pinned version. Shared scripts are not copied into this repository.
- A release must identify the exact commit and the checksums of every artifact.
- Publication requires owner approval and a confirmed licensing/attribution record.
