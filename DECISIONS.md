# Decision log

Status terms:

- **Accepted — platform constraint**: fixed by the platform handoff; not an editorial approval.
- **Scaffold default**: reversible technical choice made to bootstrap the repository.
- **Proposed**: awaits owner decision.

Only the owner approves editorial scope, gates, licensing and releases.

| ID | Status | Decision | Rationale / next step |
| --- | --- | --- | --- |
| DEC-001 | Accepted — platform constraint | This is an independent book repository. It owns its canonical Quarto sources and takes community pull requests; the hub owns the shared toolkit, schemas, profiles and portal. | Books install a pinned toolkit version. Do not import a parent checkout or vendor shared scripts here. |
| DEC-002 | Accepted — platform constraint | Roles are agent-neutral: Owner, Implementer, Reviewer. The implementer never reviews or merges their own change. | Separation of duties is a review requirement, not a product choice. See `AGENTS.md`. |
| DEC-003 | Proposed | Editorial gates run in order: brief, outline, one pilot section, then chapter-by-chapter expansion. No chapter prose before Gates 1 and 2; no further prose before Gate 3. | Owner approval of each gate is recorded in `PROJECT_STATUS.md`. |
| DEC-004 | Proposed | Content and documentation use CC BY-SA 4.0; scripts and build configuration use MIT. | Default platform licensing. Confirm attribution and third-party rights before publication. See `NOTICE.md`. |
| DEC-005 | Accepted — platform constraint | Publishing uses the hub toolkit at a pinned version. Generated artifacts are built once from an approved commit and attached to a release; they are not committed. | The toolkit version is not yet available and will be pinned when the hub publishes it. |
| DEC-006 | Accepted — platform constraint | Repository and handbook language is English. | Matches the platform contract. |
| DEC-007 | Proposed | The pilot candidate is Chapter 2, section 2.2, "The Brief as a Decision Record". | Chosen because it exercises the full content profile and validates the gate process before chapter expansion. |
| DEC-008 | Scaffold default | Keep a dependency-free book-local check (`scripts/check_repo.py`) for file, link and gate consistency. Do not copy shared platform validators. | Reversible when the pinned hub toolkit provides the book-level verify command. |

Record new proposals in a pull request. Do not mark a proposal accepted without owner confirmation.
