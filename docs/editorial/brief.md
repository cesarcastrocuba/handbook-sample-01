# Editorial brief — *Handbook Authoring and Publishing*

| Field | Value |
| --- | --- |
| Status | **Approved** — Gate 1, 2026-11-06 |
| Version | 0.1 |
| Date | 2026-11-06 |
| Approval evidence | [Owner approval record](approval-record.md) |
| Repository | `handbook-sample-01` |
| Decision owner | Project owner |
| Related documents | [Outline](outline.md) · [Content profile](profile.md) · [`AGENTS.md`](../../AGENTS.md) |

## 1. Approval status

This brief was approved at Gate 1 on 2026-11-06. The approval also records the broad technical/software audience, the full eight-chapter goal and the standard `0.2.0` direction. See the [owner approval record](approval-record.md). It does not approve Gate 3, the pilot or any chapter text.

## 2. Purpose

Teams produce handbooks to preserve decisions, reduce repeated explanation and give new contributors a reliable path into a body of work. Many handbooks fail for editorial reasons rather than technical ones: nobody owns them, the scope grows without limit, examples cannot be verified, and publishing is a manual event that cannot be repeated.

This book is a practical, vendor-neutral guide to authoring and publishing a maintainable technical handbook. It uses the handbook platform as a worked example, but teaches transferable practice: define the contract, write evidence, review independently, publish reproducibly and maintain what was published.

## 3. Reader and reader promise

**Primary readers**

- anyone who wants to write a useful, trustworthy technical handbook, initially focused on technology and software;
- practitioners sharing knowledge about software development, operations, architecture, security, data or other technical subjects;
- documentation maintainers and editors responsible for structure and quality;
- reviewers and owners who approve scope, content and releases;
- teams introducing AI-assisted writing who need explicit roles, gates and evidence.

Readers need knowledge of the subject they want to explain, but no architecture role, editorial background or prior experience with the publishing toolchain is required. Writing principles are broadly reusable; the initial examples and publishing workflow focus on technology and software.

**After reading, the reader can**

1. decide whether a handbook is the right artifact and who it serves;
2. write an editorial brief and outline that constrain the work;
3. produce a section that follows a declared content profile;
4. review content independently and record evidence rather than opinion;
5. build, verify and release artifacts from an approved commit;
6. maintain contributions, versions and retirement without losing trust.

**Reader promise.** *This book teaches how to make a handbook that a stranger can trust, review and maintain — not merely how to produce pages.*

## 4. Scope

**In scope**

- the editorial contract: audience, promise, scope, non-goals and ownership;
- section profiles and justified exceptions;
- research, source discipline, examples and rights review;
- independent review, finding severity and review evidence;
- reproducible build, artifact verification, release and catalog integration;
- contribution, versioning, errata and retirement.

**Out of scope**

- product comparisons or recommendations for authoring tools;
- an exhaustive grammar or house-style manual;
- legal advice on licensing or third-party rights;
- migration of the existing Solutions Architecture Handbook;
- operational runbooks for the hub portal;
- publication of this sample book during the bootstrap.

## 5. Editorial stance

- **Vendor-neutral.** Describe roles, decisions and evidence; name a product only when the name is necessary to make the example checkable.
- **Decision-oriented.** Explain what a choice buys, what it costs and when the opposite choice is reasonable.
- **Evidence over assertion.** Use worked examples, checklists and review records. Never invent a source, measurement, build result or approval.
- **Proportional.** Prefer the shortest form that preserves meaning. Tables and diagrams earn their space by clarifying a relationship, not by decorating a page.
- **Explicit.** Cross-reference a specific section when it helps; do not turn every repeated term into a link.

Every chapter follows the [content profile](profile.md) and records exceptions in an owner-approved `sdd/changes/<id>/profile-exceptions.md` record. Chapter front matter may reference that record; it does not replace it.

## 6. Structure and length

The intended deliverable is the complete handbook: three parts and eight chapters, plus front matter, references and appendices. The pilot is one section used to evaluate the writing approach before expanding the remaining chapters; it does not replace the complete book. The full chapter and section outline is in [`outline.md`](outline.md).

| Part | Chapters | Question |
| --- | --- | --- |
| I — Define the contract | 1–3 | What are we making, for whom, and under which rules? |
| II — Produce evidence | 4–6 | How do we research, write and review content that can be trusted? |
| III — Publish and sustain | 7–8 | How do we release and maintain it without drift? |

Proposed targets: 2,000–3,500 words per chapter, 1,200–1,800 words for the pilot section. Targets are confirmed after the pilot; they are planning bounds, not publication quotas.

## 7. Evidence and quality bar

A section is ready for review only when:

- its reader outcome and scope are identifiable;
- every required profile element is present, or an owner-approved exception record is referenced;
- examples are labeled illustrative or supported by a checkable source;
- claims about tools, standards or measurements can be verified;
- tables and diagrams are readable at their published size;
- cross-references point to a named section, not to a vague related topic;
- licensing and attribution are clear.

A chapter is ready for owner approval only when a different agent or person has reviewed the exact commit, re-run the applicable checks and posted a verdict. Critical and Major findings block approval.

## 8. Production and publication

- Canonical sources are Quarto `.qmd` files in `manuscript/`, using the platform content profile.
- The build uses the hub toolkit at a pinned version. Shared validators are not copied into this repository.
- Target reading format is HTML; download artifacts are PDF, DOCX, a source bundle, a manifest and checksums.
- Artifacts are built once from an approved commit, verified, and published unchanged. Generated artifacts are never committed.
- The sample book may later be listed in the hub catalog after an approved release. No catalog entry, deployment or release is part of this bootstrap.

## 9. Licensing and attribution

- Handbook content and repository documentation: CC BY-SA 4.0.
- Scripts and build configuration: MIT.
- Third-party material requires a documented rights review before inclusion.

The owner confirmed the licensing in `DEC-012` and the attribution in `DEC-017` on 2026-11-09. See [`NOTICE.md`](../../NOTICE.md).

## 10. Success criteria and gates

| Gate | Success criterion | Evidence |
| --- | --- | --- |
| 1 — brief | Owner approves audience, scope, non-goals, quality bar and licensing | Signed decision in this file, `PROJECT_STATUS.md` and `gates.json` |
| 2 — outline | Owner approves chapter structure, profile coverage, pilot candidate and pilot file path | Approved `outline.md` and a recorded decision; `gate_3_pilot` becomes `pending` |
| 3 — pilot | Owner approves the pilot file that was written after Gate 2 and independently reviewed for section scope and quality | Reviewed section at an exact commit; review verdict; `gate_3_pilot` becomes `approved` |
| Expansion | Each chapter meets the quality bar and is independently reviewed | Chapter review records and owner approval |
| Release | Artifacts are reproducible from an approved commit and licensing is confirmed | Manifest, checksums and release approval |

Gate 3 is an approval of written work, not a precondition for writing it. Gates 1 and 2 authorize the pilot file; the check enforces the file boundary, while the reviewer confirms the file contains only section 2.2. Gate 3 authorizes expansion. Gate values are recorded assertions, not proof of authorization. The state machine is defined in [`gates.md`](gates.md).

## 11. Assumptions and open questions

**Assumptions**

- The pinned `handbook-toolkit` `0.6.0` is installed from the public hub commit recorded in `requirements.txt`; manuscript, reference and artifact validation are available.
- The content profile is aligned with hub `standard` `1.0.0`, which preserves the approved `0.2.0` rules and is packaged on hub `main` at `7820172`.
- The sample book is a demonstration, not a replacement for the existing handbook.
- English is the publication language.
- The owner confirmed the public attribution on 2026-11-09 (`DEC-017`).

**Remaining owner item before release**

No attribution question remains: the owner confirmed Franz César Castro Cuba as author and copyright holder on 2026-11-09 (`DEC-017`).

Chapter-length bounds remain planning bounds and are confirmed after the pilot.

## Approval

| Field | Value |
| --- | --- |
| Owner | Project owner |
| Decision | Approved — Gate 1 |
| Date | 2026-11-06 |
| Notes | Broad technical/software audience, full eight-chapter goal and standard `0.2.0` direction recorded in the [approval record](approval-record.md). Gate 3 remains pending; attribution was confirmed later on 2026-11-09 (`DEC-017`). |
