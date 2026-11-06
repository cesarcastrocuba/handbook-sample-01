# Proposed outline — *Handbook Authoring and Publishing*

| Field | Value |
| --- | --- |
| Status | **Proposed** — owner approval pending (Gate 2) |
| Version | 0.1 |
| Date | 2026-11-06 |
| Depends on | [Editorial brief](brief.md) approval (Gate 1) |
| Pilot | Chapter 2, section 2.2 — **not written** |
| Related | [Content profile](profile.md) · [`AGENTS.md`](../../AGENTS.md) |

Approving this outline confirms the chapter structure, the profile coverage and the pilot candidate. It does not approve any chapter text. No chapter prose may be written until Gate 2 is approved, and no pilot or other chapter may be written until Gate 3 is approved.

## 1. Reading path

The book answers three questions in order:

| Part | Chapters | Question the reader is answering |
| --- | --- | --- |
| I — Define the contract | 1–3 | What are we making, for whom, and under which rules? |
| II — Produce evidence | 4–6 | How do we research, write and review content that can be trusted? |
| III — Publish and sustain | 7–8 | How do we release and maintain it without drift? |

The order is deliberate. A profile applied to an undefined audience produces consistent but useless pages; a build pipeline applied to unreviewed content produces polished but untrustworthy artifacts.

## 2. Chapter summary

| # | Chapter | Reader outcome | Profile emphasis |
| --- | --- | --- | --- |
| 1 | Why Handbooks Fail | Diagnose a failing handbook and decide whether to revise, narrow or retire it | Narrative lead, one worked failure, Decision & Trade-off |
| 2 | The Editorial Contract | Write a brief that constrains audience, scope, non-goals and ownership | Full standard profile; pilot section |
| 3 | Profiles and Exceptions | Apply the section profile and declare justified exceptions | Definition, What it includes, Example, Checklist |
| 4 | Research and Source Discipline | Build a source ledger and separate fact, recommendation and assumption | Example, Common Pitfall, Checklist |
| 5 | Writing a Section | Draft a section that satisfies the profile and teaches a decision | All section elements |
| 6 | Review as Evidence | Run an independent review and record a verdict with re-checked evidence | Decision & Trade-off, Checklist |
| 7 | Build, Verify, Release | Produce reproducible artifacts from an approved commit and release them unchanged | What it includes, Why it is needed, Checklist |
| 8 | Maintenance and Contribution | Set contribution, versioning, errata and retirement rules | Decision & Trade-off, Checklist |

## 3. Part I — Define the contract

### Chapter 1 — Why Handbooks Fail

**Purpose.** Show that handbook quality is an editorial and ownership problem before it is a tooling problem.

**Sections**

- 1.1 What a handbook is for, and when another artifact is a better fit.
- 1.2 Four failure modes: orphaned drafts, unbounded scope, missing ownership, unverifiable claims.
- 1.3 The lifecycle: brief, outline, pilot, expansion, release, maintenance, retirement.

**Exit evidence.** The reader can name the failure mode of a real handbook and choose a proportionate response.

### Chapter 2 — The Editorial Contract

**Purpose.** Turn an intention to write into a bounded, approved contract that later work can be judged against.

**Sections**

- 2.1 Reader, promise and non-goals.
- 2.2 The brief as a decision record. **Pilot candidate.**
- 2.3 Scope boundaries, ownership and change control.

**Exit evidence.** A brief that another person could use to reject out-of-scope work without asking the author.

### Chapter 3 — Profiles and Exceptions

**Purpose.** Make sections consistent without forcing every section into the same template.

**Sections**

- 3.1 The standard section profile and why each element exists.
- 3.2 Declaring exceptions without losing consistency.
- 3.3 Diagrams, tables and explicit cross-references.

**Exit evidence.** An annotated section that shows which profile elements are present and why any are omitted.

## 4. Part II — Produce evidence

### Chapter 4 — Research and Source Discipline

**Purpose.** Build a traceable path from a claim to a source, and make uncertainty visible.

**Sections**

- 4.1 Source hierarchy: primary sources, standards, practitioner accounts and internal evidence.
- 4.2 Claims, citations and assumptions.
- 4.3 Rights review and attribution.

**Exit evidence.** A source ledger for one section, including one claim marked unverified.

### Chapter 5 — Writing a Section

**Purpose.** Convert research into a section that teaches a decision and survives review.

**Sections**

- 5.1 Definition, purpose and what the section includes.
- 5.2 Worked examples and common pitfalls.
- 5.3 Decisions, trade-offs and action checklists.

**Exit evidence.** One section that passes the profile checklist and names its reader outcome.

### Chapter 6 — Review as Evidence

**Purpose.** Replace "looks good to me" with an independent verdict tied to an exact commit.

**Sections**

- 6.1 Separation of duties and the limits of self-review.
- 6.2 Finding severity and merge-blocking verdicts.
- 6.3 Re-checks, review records and closure.

**Exit evidence.** A review record with the reviewed HEAD, re-run commands, findings by severity and a verdict.

## 5. Part III — Publish and sustain

### Chapter 7 — Build, Verify, Release

**Purpose.** Make publication repeatable and make the published artifact verifiably the reviewed one.

**Sections**

- 7.1 Pin the toolchain and declare the source of truth.
- 7.2 Build once, verify deterministically, record a manifest and checksums.
- 7.3 Release gates, catalog integration and artifact retention.

**Exit evidence.** A release checklist and a manifest that identifies the approved commit and every published artifact.

### Chapter 8 — Maintenance and Contribution

**Purpose.** Keep the handbook trustworthy after the first release.

**Sections**

- 8.1 Community contributions and scoped review.
- 8.2 Versioning, errata and deprecation.
- 8.3 Periodic review and retirement.

**Exit evidence.** A maintenance policy with an owner, a review cadence and a retirement path.

## 6. Front matter, back matter and appendices

| Location | Content | Status |
| --- | --- | --- |
| Front matter | Title page and document control | Proposed |
| Front matter | Preface: how to use this book | Proposed |
| Front matter | Reading paths for authors, reviewers and maintainers | Proposed |
| Back matter | References | Proposed |
| Appendix A | Brief and outline templates | Proposed |
| Appendix B | Gate and review checklists | Proposed |
| Appendix C | Glossary | Proposed |

Appendix A may reproduce the templates used in the book. It must not reproduce third-party templates without a rights review.

## 7. Pilot proposal

**Candidate:** Chapter 2, section 2.2, *The Brief as a Decision Record*.

**Why this section**

- It exercises the full content profile, including Definition, Purpose, What it includes, Why it is needed, Example, Common Pitfall, Decision & Trade-off, Checklist and Further Reading.
- It tests the gate process at the smallest useful unit before chapter expansion.
- It produces a reusable artifact, the brief template, that later chapters depend on.
- Its quality can be judged without a build pipeline, which is not yet available.

**Scope**

- 1,200–1,800 words.
- One worked example of a brief decision.
- One table, if it improves comparison; otherwise prose.
- At most one diagram; none is currently planned.
- Explicit cross-references to 2.1 and 2.3, without linking every term.

**Approval criteria**

1. Every profile element is present, or an exception is declared with a reason.
2. The section states what a brief decides, not merely what it contains.
3. The example is labeled and shows a trade-off.
4. The checklist is observable and short.
5. Sources are real and checkable; none are invented.
6. A different agent or person reviews the exact commit and posts a verdict.

**Not included:** the rest of Chapter 2, any other chapter, Quarto configuration, a build or a release.

## 8. Sequence after approval

1. **Gate 3:** write and approve the pilot section only.
2. Revise this outline if the pilot exposes a structural problem; record the change.
3. Write Chapters 1 and 3 to complete Part I.
4. Write Part II, then Part III, reviewing each chapter independently.
5. Write front matter, references and appendices after the chapter structure is stable.
6. Build and release only after the owner approves the complete manuscript and licensing.

## 9. Approval criteria for this outline

- Every chapter has a distinct reader outcome and exit evidence.
- The profile is applied without making every chapter structurally identical.
- The pilot is small enough to review completely and broad enough to test the profile.
- Dependencies are explicit: no chapter depends on an unwritten artifact without saying so.
- Scope remains consistent with the [editorial brief](brief.md).

## Approval

| Field | Value |
| --- | --- |
| Owner | *Pending* |
| Decision | *Pending* |
| Date | *Pending* |
| Notes | *Pending* |
