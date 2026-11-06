# Manuscript

This directory is reserved for the canonical Quarto sources. It contains **no prose** during bootstrap: Gates 1 and 2 are pending, and Gate 3 has not started.

## Planned layout

| Path | Content |
| --- | --- |
| `front-matter/` | Title page, document control, preface and reading paths |
| `chapters/` | Chapters 1–8, named `chNN-slug.qmd` |
| `appendices/` | Appendices A–C |
| `back-matter/` | References |

## Rules

- Chapter files are added only after the outline is approved and only for the section or chapter authorized by the current gate.
- One chapter per file; no generated content and no copied third-party text.
- Every chapter declares its profile exceptions in YAML front matter.
- The reading order will be declared in `publishing/` once the pilot is approved.
- Do not add diagrams, tables or examples that have no rights review.

The repository check fails while `manuscript/` contains `.qmd` files during the bootstrap gate. Update the check when Gate 3 is approved; do not bypass it.
