# Tasks — change 0001

| ID | Task | Status | Evidence |
| --- | --- | --- | --- |
| T1 | Initialize the local repository on `main` | Done | `git init -b main` |
| T2 | Define agent-neutral roles, workflow and gates | Done | `AGENTS.md` |
| T3 | Draft the editorial brief | Done | `docs/editorial/brief.md`, status Proposed |
| T4 | Draft the proposed outline and pilot candidate | Done | `docs/editorial/outline.md`, status Proposed |
| T5 | Define the content profile and exception format | Done | `docs/editorial/profile.md` |
| T6 | Reserve manuscript and publishing layouts without prose | Done | `manuscript/`, `publishing/` |
| T7 | Add the dependency-free repository check and CI entry | Done | `scripts/check_repo.py`, `Makefile`, `.github/workflows/check.yml` |
| T8 | Record decisions, status and licensing proposal | Done | `DECISIONS.md`, `PROJECT_STATUS.md`, `NOTICE.md` |
| T9 | Run local checks and record exact results | Done | `make check`; see the review report |
| T10 | Independent review of the bootstrap commit | Pending | Reviewer verdict on the exact HEAD |
| T11 | Owner decision on Gate 1 (brief) | Blocked by review | Approval block in the brief |
| T12 | Owner decision on Gate 2 (outline) | Blocked by Gate 1 | Approval block in the outline |
| T13 | Write the pilot section | Blocked by Gate 2 | Chapter 2, section 2.2 |

T13 must not start in this change.
