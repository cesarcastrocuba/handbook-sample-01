# Agent instructions

These rules apply to every contributor, human or AI, whatever tool they use. They describe **roles, not products**. Any agent may take any role, subject to the separation-of-duties rule. Current status lives only in [`PROJECT_STATUS.md`](PROJECT_STATUS.md); technical and editorial decisions live in [`DECISIONS.md`](DECISIONS.md); editorial scope lives in the [brief](docs/editorial/brief.md) and [outline](docs/editorial/outline.md).

## Mission

Produce the sample handbook *Handbook Authoring and Publishing* as a worked example of the handbook platform: an independent book repository with canonical sources, an approved editorial contract, and reproducible, independently reviewed publication.

## Roles

| Role | Responsibility |
| --- | --- |
| **Owner** | Approves the editorial brief, outline, pilot section, chapter expansion, licensing and every release. Merges to `main`. |
| **Implementer** | Makes one scoped change on a branch, runs the applicable checks, and opens a pull request with evidence. |
| **Reviewer** | A *different* agent or person. Reviews the exact pull-request HEAD, re-runs the checks, and posts a verdict. Editorial review is a Reviewer responsibility; the owner may assign a dedicated editor. |

No role is tied to a named product, model or vendor. An agent may implement in one change and review another, but never the same change.

## Workflow

1. Read `PROJECT_STATUS.md`, `DECISIONS.md`, the editorial brief and the approved outline before changing content.
2. Branch from `main` using `<type>/<topic>`, for example `docs/editorial-brief`.
3. Keep the change scoped and reversible. One writer per file at a time.
4. Run `make check` and any additional check named by the change. Report only commands actually run.
5. Open a pull request describing the change, the gate it serves and the evidence.
6. A different agent or person reviews the exact HEAD. Critical and Major findings block the merge; Minor and Optional findings are fixed or recorded as issues.
7. The owner merges and, when a gate is reached, records the approval in `PROJECT_STATUS.md`.
8. Never self-review, never merge your own change, and never publish or release without owner approval.

## Editorial gates

The order is mandatory:

1. **Gate 1 — brief.** The owner approves the audience, scope, non-goals, quality bar and licensing.
2. **Gate 2 — outline.** The owner approves chapter structure, profile coverage and the pilot candidate.
3. **Gate 3 — pilot.** The owner approves one written pilot section. No other chapter prose may be written before this gate.
4. **Expansion.** Remaining chapters are written and reviewed chapter by chapter.

While Gate 1 or Gate 2 is pending, `manuscript/` must contain no chapter prose. While Gate 3 is pending, no pilot or chapter `.qmd` file may be committed.

## Content rules

- English for handbook content and repository documentation.
- Vendor-neutral, decision- and trade-off-oriented. Prefer explicit evidence over broad claims.
- Follow the [content profile](docs/editorial/profile.md). Declare every exception explicitly.
- No fabricated sources, standards, measurements, build results or review verdicts. Label illustrative examples as illustrative.
- No secrets, personal data, caches or third-party material without a rights review.
- Content is CC BY-SA 4.0; code and build configuration are MIT. See [`NOTICE.md`](NOTICE.md).
- Do not commit generated HTML, PDF, DOCX, site output or dependency caches.

## Source of truth

- `manuscript/` will hold canonical Quarto sources once the gates allow content.
- `publishing/` will hold pinned build configuration and metadata. The shared toolkit is installed from the hub at a pinned version; do not vendor or copy it here.
- `docs/editorial/` holds the brief, outline and content profile.
- `sdd/changes/` records substantial proposals, decisions and evidence.
- Generated artifacts are built from an approved commit and attached to a release; they are never committed.
