# Owner approval record

| Field | Value |
| --- | --- |
| Date | 2026-11-06 |
| Owner statement | **“Dale con todo... continúa.”** |
| Context | Owner response after the concrete Gate 1/Gate 2 approval question and the audience clarification |
| Gates approved | Gate 1 — brief; Gate 2 — outline |
| Direction approved | Broad technical/software handbook audience, standard `0.2.0` direction, full eight-chapter target |
| Gate not approved | Gate 3 — pilot |
| Current machine state | [`gates.json`](gates.json): `approved / approved / pending` |

## Approved scope

- The [editorial brief](brief.md) as the editorial contract, including the broad audience of anyone writing a useful, trustworthy technology or software handbook, with architecture as one example rather than a requirement.
- The [outline](outline.md): three parts, eight chapters, front matter, references and appendices.
- The direction of hub `standard` `0.2.0`, approved and integrated on hub `main` at `8ee28a081399155a250ea8bc45d8492245ab2377`.
- The pilot candidate remains Chapter 2, section 2.2, but **Gate 3 is not approved**. Approval of Gates 1 and 2 opens the pilot window; it does not accept a pilot that has not been written or reviewed.

## Explicitly not approved

- Gate 3 and the pilot content.
- Chapter expansion beyond the pilot.
- Any release or publication.
- Public attribution was not approved at Gate 1; the owner confirmed it later on 2026-11-09 (`DEC-017`).

## Integration authorization

The owner authorized integrating the reviewed foundation and integration branches in the same instruction. That authorization covers integration only. It does not approve a pilot, chapter expansion or a release, and root integration does not by itself authorize those steps.

The hub profile is approved and integrated at hub `main` `8ee28a0`; this book's `0.2.0` direction was approved at Gate 2. The current descriptor pins `standard` `1.0.0` at hub `7820172`, which preserves every approved `0.2.0` rule and adds the validation classification.

## Limitations

This record is a recorded owner assertion, not proof of identity or authorization. An independent reviewer must verify the approval evidence against the owner's statement before integration. The local check can enforce gate ordering and the pilot file boundary; it cannot authenticate the approval.

## Gate 3 approval (pilot 2.2)

On 2026-11-06 the owner delegated owner decisions for platform Phases 1-4 to the root coordinator
(hub decision `HUB-DEC-016`). Acting under that delegation, the root reviewer approved Gate 3 for
pilot section 2.2 at source commit `69e4bf8`, after reading the section and the independent
assessment in [`pilot-review.md`](pilot-review.md). Chapter expansion is authorized in small,
independently reviewed batches. The pilot contains no figure; figures are optional under the
approved standard profile `0.2.0`, so this is not a profile exception. Release remains a separate
decision under the same delegation.
