# Manuscript

This directory holds the canonical Quarto sources. It currently contains only pilot section 2.2 at `chapters/ch02-editorial-contract.qmd`; Gate 3 is pending.

## Planned layout

| Path | Content |
| --- | --- |
| `front-matter/` | Title page, document control, preface and reading paths |
| `chapters/` | Chapters 1–8, named `chNN-slug.qmd` |
| `appendices/` | Appendices A–C |
| `back-matter/` | References |

## Rules

- Gates 1 and 2 are approved; only the pilot file may exist while Gate 3 is pending. That file contains only section 2.2, not the rest of the chapter.
- The check enforces the file boundary only; it does not read the file. A reviewer confirms that the file contains only section 2.2 and follows the content profile.
- No other chapter, appendix or front-matter `.qmd` may be added until Gate 3 is approved.
- Every chapter declares its profile exceptions in YAML front matter; a pilot scope interpretation is proposed in [`sdd/changes/0003-pilot-2-2/scope.md`](../sdd/changes/0003-pilot-2-2/scope.md).
- The reading order is declared in `manuscript/book.yml` and currently lists only the pilot.
- Do not add diagrams, tables or examples that have no rights review.

The repository check enforces this sequence. Do not bypass it; when the pinned toolkit provides content validation, keep the gate policy and replace only the content checks.
