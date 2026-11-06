# Handbook Authoring and Publishing

A sample handbook that demonstrates how to plan, write, review and publish a maintainable technical handbook. It is the reference book for the handbook platform and is written in public so the workflow itself can be inspected.

**Status: bootstrap.** The editorial brief and outline are proposed. No chapter prose exists, and the pilot section is intentionally not written. Owner approval is the next step.

## Current gate

| Gate | State |
| --- | --- |
| 1 — editorial brief | Proposed, awaiting owner approval |
| 2 — proposed outline | Proposed, awaiting owner approval |
| 3 — pilot section | Blocked by Gates 1 and 2 |

The gate sequence and stop conditions are defined in [`AGENTS.md`](AGENTS.md). Gate evidence is recorded in [`PROJECT_STATUS.md`](PROJECT_STATUS.md).

## What this repository contains

- [`docs/editorial/brief.md`](docs/editorial/brief.md) — purpose, audience, scope, non-goals, quality bar and licensing.
- [`docs/editorial/outline.md`](docs/editorial/outline.md) — proposed parts, chapters, pilot candidate and approval criteria.
- [`docs/editorial/profile.md`](docs/editorial/profile.md) — the standard section profile and its allowed exceptions.
- [`AGENTS.md`](AGENTS.md) — agent-neutral roles, workflow and editorial gates.
- [`DECISIONS.md`](DECISIONS.md) — decisions with explicit status.
- [`sdd/changes/0001-sample-bootstrap/`](sdd/changes/0001-sample-bootstrap/proposal.md) — bootstrap proposal and task record.
- `manuscript/` — reserved layout for canonical sources; intentionally empty of prose.
- `publishing/` — metadata and publication plan; build configuration is deferred until the pilot is approved.

## Verify

The repository check is book-local and uses only the Python standard library:

```sh
make check
```

It verifies required files, relative Markdown links, the absence of generated artifacts and environment-specific paths, the agent-neutral role names, and the current gate condition that no chapter prose exists. Shared platform checks belong to the hub toolkit and are not vendored here.

## Workflow

Work happens on short-lived branches and is reviewed by a different agent or person before the owner merges. Conventional commits are used. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Licensing

Handbook content is licensed under CC BY-SA 4.0; scripts and build configuration are licensed under MIT. See [`NOTICE.md`](NOTICE.md).
