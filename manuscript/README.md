# Manuscript

This directory is reserved for the canonical Quarto sources. It contains **no prose** during bootstrap: Gates 1 and 2 are pending, so the pilot window is not open.

## Planned layout

| Path | Content |
| --- | --- |
| `front-matter/` | Title page, document control, preface and reading paths |
| `chapters/` | Chapters 1–8, named `chNN-slug.qmd` |
| `appendices/` | Appendices A–C |
| `back-matter/` | References |

## Rules

- No prose before Gates 1 and 2 are approved.
- Once both are approved, **exactly one file** may be committed while Gate 3 is pending: the pilot at `pilot.path` in [`docs/editorial/gates.json`](../docs/editorial/gates.json). That file must contain only section 2.2, not the rest of the chapter.
- The check enforces the file boundary only; it does not read the file. A reviewer confirms that the file contains only section 2.2 and follows the content profile.
- No other chapter, appendix or front-matter `.qmd` may be added until Gate 3 is approved.
- Every chapter declares its profile exceptions in YAML front matter.
- The reading order will be declared in `publishing/` once the pilot is approved.
- Do not add diagrams, tables or examples that have no rights review.

The repository check enforces this sequence. Do not bypass it; when the pinned toolkit provides content validation, keep the gate policy and replace only the content checks.
