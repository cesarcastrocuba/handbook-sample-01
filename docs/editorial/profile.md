# Content profile

| Field | Value |
| --- | --- |
| Status | **Proposed** — owner approval pending with the outline (Gate 2) |
| Version | 0.1 |
| Date | 2026-11-06 |
| Applies to | Every chapter and appendix in this book |

This profile defines the reusable shape of a section. It is deliberately small: enough structure to make chapters consistent and reviewable without turning every page into a form.

## 1. Chapter-level elements

Every chapter opens with:

1. a short lead that states the problem and why it matters;
2. **When to Use This Chapter** — a callout with three to five concrete situations;
3. **Key Takeaway** — one paragraph stating the durable idea.

```markdown
::: {.callout-note appearance="simple" icon=false title="When to Use This Chapter"}
- Situation one.
- Situation two.
:::

::: {.callout-tip appearance="simple" icon=false title="Key Takeaway"}
One paragraph.
:::
```

## 2. Section-level elements

| Element | Requirement | Form |
| --- | --- | --- |
| **Definition** | Required when the section introduces a concept | Bold lead-in; one or two sentences that state what the thing is and what it is not |
| **Purpose** | Required for a concept or practice | Why the reader needs it; the decision or action it enables |
| **What it includes** | Required for a concept or practice | Concrete contents, fields or steps; name the minimum useful set |
| **Why it is needed** | Required for a concept or practice | Consequence of omitting it, with a failure mode |
| **Example** | Required unless an exception is declared | Worked, labeled example; fictional details marked as illustrative |
| **Common Pitfall** | Required unless an exception is declared | One specific failure, its symptom and its correction |
| **Decision & Trade-off** | Required for decision-oriented sections | The choice, what it buys, what it costs, and when the alternative is reasonable |
| **Checklist** | Required when the reader must act | Short, observable items; no vague aspirations |
| **Further Reading** | Required when sources exist | Real, checkable sources with a note on why each is relevant |

Not every section needs every element. A narrative history section may legitimately use only Definition, Example and Common Pitfall. The exception must be declared, not left implicit.

## 3. Ordering

Use this order unless the argument requires otherwise:

`Definition → Purpose → What it includes → Why it is needed → Example → Common Pitfall → Decision & Trade-off → Checklist → Further Reading`

The order moves from meaning to use, then to failure and choice, then to action and evidence.

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

- Use a table when readers must compare rows across the same columns.
- Keep cells short enough to wrap without hiding the comparison.
- Allow adaptive widths in the published format; do not force a fixed width that clips content.
- Put the caption below the table and make it describe the comparison, not repeat the header.

### 4.4 Diagrams

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

A chapter that omits a required element or changes the order declares it in YAML front matter:

```yaml
---
title: "Chapter title"
profile: standard
profile-exceptions:
  - element: Further Reading
    reason: "The chapter teaches an internal workflow and cites no external sources."
---
```

The reviewer checks that every declared exception has a reason. An undeclared omission is a finding. Exceptions are per chapter, not a silent global change to this profile.

## 6. Review checklist

- [ ] The chapter opens with When to Use This Chapter and Key Takeaway.
- [ ] Required elements are present or exceptions are declared with reasons.
- [ ] The reader outcome is visible in the section, not only in the outline.
- [ ] Examples are labeled and teach a decision.
- [ ] Tables compare like with like; captions describe the comparison.
- [ ] Diagrams keep their aspect ratio and remain readable when published.
- [ ] Cross-references name a specific locator.
- [ ] Sources are real and checkable; assumptions are labeled.
- [ ] No third-party material lacks a rights review.
- [ ] The section adds something the outline promised and nothing unrelated.
