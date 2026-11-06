# Pilot 2.2 scope interpretation

| Field | Value |
| --- | --- |
| Status | **Proposed scoped interpretation — not an owner-approved exception** |
| Date | 2026-11-06 |
| Section | Chapter 2, section 2.2, “The Brief as a Decision Record” |
| Gate | Gate 3 remains pending |

## 1. Scope of this change

This change writes only section 2.2 at `manuscript/chapters/ch02-editorial-contract.qmd` and adds that file to the reading order. It does not write sections 2.1 or 2.3, any other section, or any chapter-level element.

The section applies the section-level part of the approved `standard` `0.2.0` profile: one unit with Definition, Purpose, What it includes and Why it is needed; then the closing Example, Common Pitfall and Decision & Trade-off in that order.

## 2. Chapter-level interpretation

A single-section pilot cannot exercise the chapter-level requirements: When to Use This Chapter, Key Takeaway, a Worked Example section, a Review Checklist callout at the end of that Worked Example, and Further Reading as the last numbered section.

This pilot therefore **proposes**, but does not claim as approved, the following interpretation:

- the chapter-level elements remain required when Chapter 2 is assembled;
- their absence here is a scoped pilot interpretation, not an exception approval;
- the pilot includes a “Brief quality check” list and a Further Reading callout for evaluation; final placement of Further Reading remains a chapter-level decision;
- no exception is recorded under `profile-exceptions` because no owner has approved one.

The owner may accept this interpretation, require the full chapter skeleton in the pilot, or request a different pilot unit. Gate 3 is not approved.

## 3. References and validation

The section does not reference unwritten sections 2.1 or 2.3. External sources are limited to checkable Further Reading entries.

`handbook-toolkit validate-book --full` validates the descriptor and reading order only. It does not validate manuscript content, profile conformance or editorial quality. No artifact build is run.
