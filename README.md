# Handbook Authoring and Publishing

A sample handbook that demonstrates how to plan, write, review and publish a maintainable technical handbook. It is the reference book for the handbook platform and is written in public so the workflow itself can be inspected.

**Status: Gates 1 and 2 approved; Gate 3 pending.** Pilot section 2.2 is written and awaiting independent review. No other chapter prose exists; root integration and pilot review are pending.

## Current gate

| Gate | State |
| --- | --- |
| 1 — editorial brief | Approved, 2026-11-06 |
| 2 — outline | Approved, 2026-11-06 |
| 3 — pilot section | Pending, not approved; pilot 2.2 written, awaiting review |

Gate 3 is an approval of written work, not a precondition for writing it. The pilot file now exists; Gate 3 approval authorizes expansion. The exact sequence is in [`docs/editorial/gates.md`](docs/editorial/gates.md). Gate evidence is recorded in [`docs/editorial/approval-record.md`](docs/editorial/approval-record.md), [`PROJECT_STATUS.md`](PROJECT_STATUS.md) and [`docs/editorial/gates.json`](docs/editorial/gates.json).

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
- [`sdd/changes/0003-pilot-2-2/`](sdd/changes/0003-pilot-2-2/scope.md) — proposed scoped interpretation for the single-section pilot.
- `manuscript/` — canonical sources; currently contains only the pilot section 2.2.
- `publishing/` — metadata and publication plan; build configuration is deferred until Gate 3 approves the pilot.

## Verify

Install the pinned toolkit from the public hub, then run the fast checks:

```sh
python3 -m pip install -r requirements.txt
make check
```

`make check` runs the local gate-policy tests, the repository checks and the toolkit's fast `validate-book` check. It requires network access only for the one-time install; the installed package is pinned to a full hub commit SHA and is not an editable parent checkout.

`make full` runs the full descriptor/reading-order check, then fails as a **current-scope incomplete** editorial-and-artifact gate: toolkit `0.1.0` does not validate manuscript content or profile conformance, and no artifact manifest or checksums exist. Do not report `make full` as a passing full build.

The integration source, metadata ownership and limits are documented in [`docs/integration/pinned-toolkit.md`](docs/integration/pinned-toolkit.md). Shared platform checks belong to the pinned hub toolkit and are not vendored here.

## Workflow

Work happens on short-lived branches and is reviewed by a different agent or person before the owner merges. Conventional commits are used. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Licensing

Handbook content is licensed under CC BY-SA 4.0; scripts and build configuration are licensed under MIT. See [`NOTICE.md`](NOTICE.md).
