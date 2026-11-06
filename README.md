# Handbook Authoring and Publishing

A sample handbook that demonstrates how to plan, write, review and publish a maintainable technical handbook. It is the reference book for the handbook platform and is written in public so the workflow itself can be inspected.

**Status: Gates 1 and 2 approved; Gate 3 pending.** No chapter prose exists, and the pilot is not written. Root review and integration of the approval record are next.

## Current gate

| Gate | State |
| --- | --- |
| 1 — editorial brief | Approved, 2026-11-06 |
| 2 — outline | Approved, 2026-11-06 |
| 3 — pilot section | Pending, not approved; pilot not written |

Gate 3 is an approval of written work, not a precondition for writing it. After root integration of the approval record, the pilot file is written while Gate 3 is pending; Gate 3 approval then authorizes expansion. The exact sequence is in [`docs/editorial/gates.md`](docs/editorial/gates.md). Gate evidence is recorded in [`docs/editorial/approval-record.md`](docs/editorial/approval-record.md), [`PROJECT_STATUS.md`](PROJECT_STATUS.md) and [`docs/editorial/gates.json`](docs/editorial/gates.json).

## What this repository contains

- [`docs/editorial/brief.md`](docs/editorial/brief.md) — purpose, audience, scope, non-goals, quality bar and licensing.
- [`docs/editorial/outline.md`](docs/editorial/outline.md) — approved parts, chapters, pilot candidate and approval criteria.
- [`docs/editorial/profile.md`](docs/editorial/profile.md) — the standard section profile and its allowed exceptions.
- [`docs/editorial/gates.md`](docs/editorial/gates.md) — the gate sequence, state transitions and what each gate authorizes.
- [`docs/editorial/gates.json`](docs/editorial/gates.json) — machine-readable gate state and the authorized pilot path.
- [`AGENTS.md`](AGENTS.md) — agent-neutral roles, workflow and editorial gates.
- [`DECISIONS.md`](DECISIONS.md) — decisions with explicit status.
- [`sdd/changes/0001-sample-bootstrap/`](sdd/changes/0001-sample-bootstrap/proposal.md) — bootstrap proposal and task record.
- [`sdd/changes/0002-pilot-gate-window/`](sdd/changes/0002-pilot-gate-window/proposal.md) — correction that separates pilot writing authority from Gate 3 approval.
- `manuscript/` — reserved layout for canonical sources; intentionally empty of prose.
- `publishing/` — metadata and publication plan; build configuration is deferred until Gate 3 approves the pilot.

## Verify

Install the pinned toolkit from the public hub, then run the fast checks:

```sh
python3 -m pip install -r requirements.txt
make check
```

`make check` runs the local gate-policy tests, the repository checks and the toolkit's fast `validate-book` check. It requires network access only for the one-time install; the installed package is pinned to a full hub commit SHA and is not an editable parent checkout.

`make full` is a **current-scope incomplete** full/artifact gate, not a descriptor failure. It runs the fast checks and then fails explicitly: no pilot or chapter `.qmd` exists yet, so `validate-book --full` is not run; no artifact manifest or checksums exist. Once the pilot exists, `validate-book --full` may run. Do not report `make full` as a passing full build.

The integration source, metadata ownership and limits are documented in [`docs/integration/pinned-toolkit.md`](docs/integration/pinned-toolkit.md). Shared platform checks belong to the pinned hub toolkit and are not vendored here.

## Workflow

Work happens on short-lived branches and is reviewed by a different agent or person before the owner merges. Conventional commits are used. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Licensing

Handbook content is licensed under CC BY-SA 4.0; scripts and build configuration are licensed under MIT. See [`NOTICE.md`](NOTICE.md).
