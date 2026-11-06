# Content profile

| Field | Value |
| --- | --- |
| Status | **Proposed** — owner approval pending with the outline (Gate 2) |
| Document revision | 0.2 |
| Date | 2026-11-06 |
| Hub profile reference | `standard` `0.2.0` — **Proposed** on hub branch `feat/topic-neutral-profile`; contingent on hub branch approval |
| Applies to | Every chapter and appendix in this book |

This profile defines the reusable shape of a section. It is deliberately small: enough structure to make chapters consistent and reviewable without turning every page into a form. It is not an approved hub profile and does not make `0.2.0` available.

## 1. Chapter-level elements

Every chapter has, in this order:

1. a short lead that states the problem and why it matters;
2. **When to Use This Chapter** — a callout with three to five concrete situations;
3. **Key Takeaway** — one paragraph stating the durable idea;
4. numbered sections `N.1 … N.k`;
5. **Worked Example** — a required section, last before the checklist; it begins with `*In practice:*` and may use numbered steps, a figure or a table;
6. **Review Checklist** — a required, topic-neutral callout at the end of the Worked Example;
7. **Further Reading** — a required last numbered section.

```markdown
::: {.callout-note appearance="simple" icon=false title="When to Use This Chapter"}
- Situation one.
- Situation two.
:::

::: {.callout-tip appearance="simple" icon=false title="Key Takeaway"}
One paragraph.
:::

::: {.callout-note appearance="simple" icon=false title="Review Checklist"}
- Observable review item one.
- Observable review item two.
:::
```

The Review Checklist is generic to the chapter's topic. It is not an “Architecture Review Checklist” unless the chapter is actually about architecture.

## 2. Section-level elements

| Element | Requirement | Form |
| --- | --- | --- |
| **Definition** | Required for a concept or practice unit | Bold lead-in; one or two sentences that state what the thing is and what it is not |
| **Purpose** | Required for a concept or practice unit | Why the reader needs it; the decision or action it enables |
| **What it includes** | Required for a concept or practice unit | Concrete contents, fields or steps; name the minimum useful set |
| **Why it is needed** | Required for a concept or practice unit | Consequence of omitting it, with a failure mode |
| **Example** | Required section closure | Worked, labeled example; fictional details marked as illustrative |
| **Common Pitfall** | Required section closure | One specific failure, its symptom and its correction |
| **Decision & Trade-off** | Required section closure | The choice, what it buys, what it costs, and when the alternative is reasonable |

A concept or practice unit uses the four labelled paragraphs in the order Definition, Purpose, What it includes and Why it is needed. Every topic section closes with Example, Common Pitfall and Decision & Trade-off, in that order. The Worked Example follows its own shape and ends with the Review Checklist. A section either has no numbered subsections or at least two; a single subsection is a defect.

Omission of a required element needs the owner-approved exception record described in section 5. Visuals are optional; see sections 4.3 and 4.4.

## 3. Ordering

Use this order unless an approved exception says otherwise:

`Definition → Purpose → What it includes → Why it is needed → Example → Common Pitfall → Decision & Trade-off`

The order moves from meaning to use, then to failure and choice. The chapter then closes with its Worked Example, Review Checklist and Further Reading.

## 4. Writing rules

### 4.1 Definitions

- State the category and the boundary: what it is, what it is not.
- Prefer a testable statement over a slogan.
- Define a term once; do not redefine it in every chapter.

### 4.2 Examples

- Label illustrative examples, including fictional organizations and numbers.
- Show the decision, not only the artifact. A template without the reasoning that fills it teaches copying.
- Keep one example per point. A second example is justified only when it tests a different condition.

### 4.3 Tables

Tables are optional and are never required for profile conformance.

- Use a table when readers must compare rows across the same columns.
- Keep cells short enough to wrap without hiding the comparison.
- Allow adaptive widths in the published format; do not force a fixed width that clips content.
- Put the caption below the table and make it describe the comparison, not repeat the header.

### 4.4 Diagrams

Diagrams are optional and are never required for profile conformance.

- Use a diagram only when relationships are harder to express in prose.
- Keep the aspect ratio. Do not enlarge a small diagram to fill the text column.
- Body text inside a diagram must remain readable at the published size; the platform floor is 10 pt effective size.
- Label every edge that carries meaning. An unlabeled arrow is decoration.
- Provide alt text that states the relationship, not the shapes.

### 4.5 Cross-references

- Reference a specific section, figure or table when the reader needs it: "see 2.2 for the brief template".
- Do not link every repeated term. A link is a navigation decision, not emphasis.
- Never use "as mentioned above" as the only locator; name the section.

### 4.6 Sources and claims

- Cite a source that a reader can check. Never invent a title, author, URL, standard number or measurement.
- Distinguish a fact, a recommendation and an assumption.
- If evidence is missing, say so. "Not verified" is an acceptable statement; a fabricated citation is not.
- Quote sparingly and within the source's terms. Reproducing a table or figure requires a rights review.

### 4.7 Length

- One idea per subsection. Split when a subsection needs two Key Takeaways.
- Prefer a short section that completes an argument to a long section that lists everything known.
- The pilot confirms the working length; do not pad to a quota.

## 5. Declaring exceptions

An exception is valid only when the owner approves it and the rationale is recorded in `sdd/changes/<id>/profile-exceptions.md`. The record states:

- the profile element and version;
- why the default does not fit;
- what replaces it;
- the scope (book, chapter or section);
- the owner approval reference;
- the expiry or review trigger.

A chapter front matter entry may reference that record, but it does not replace it:

```yaml
---
title: "Chapter title"
profile: standard
profile-exceptions:
  record: sdd/changes/<id>/profile-exceptions.md
---
```

An undeclared omission is a finding. An exception without an owner-approved record is also a finding. A book-wide alternative profile is a new profile version, not a list of exceptions.

## 6. Review checklist

- [ ] The chapter opens with When to Use This Chapter and Key Takeaway.
- [ ] The chapter has a Worked Example section beginning with `*In practice:*`.
- [ ] The Worked Example ends with a generic Review Checklist callout.
- [ ] Further Reading is the last numbered section.
- [ ] Each concept unit uses Definition, Purpose, What it includes and Why it is needed.
- [ ] Each topic section closes with Example, Common Pitfall and Decision & Trade-off in that order.
- [ ] No single numbered subsection exists.
- [ ] Tables and diagrams appear only when they improve understanding; if present, they are readable when published.
- [ ] Any omission references an owner-approved `sdd/changes/<id>/profile-exceptions.md` record.
- [ ] Cross-references name a specific locator.
- [ ] Sources are real and checkable; assumptions are labeled.
- [ ] No third-party material lacks a rights review.
- [ ] The section adds something the outline promised and nothing unrelated.
