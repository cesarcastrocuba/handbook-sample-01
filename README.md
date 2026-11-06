# Handbook Authoring and Publishing

A sample handbook that demonstrates how to plan, write, review and publish a maintainable technical handbook. It is the reference book for the handbook platform and is written in public so the workflow itself can be inspected.

**Status: Gates 1–3 approved; Part I drafted.** Chapters 1–3 are written; no artifacts or release exist yet.

## Current gate

| Gate | State |
| --- | --- |
| 1 — editorial brief | Approved, 2026-11-06 |
| 2 — outline | Approved, 2026-11-06 |
| 3 — pilot section | Approved, 2026-11-06; Part I expansion authorized |

Gate 3 is an approval of written work and authorizes expansion. Part I now contains Chapters 1–3. The exact sequence is in [`docs/editorial/gates.md`](docs/editorial/gates.md). Gate evidence is recorded in [`docs/editorial/approval-record.md`](docs/editorial/approval-record.md), [`PROJECT_STATUS.md`](PROJECT_STATUS.md) and [`docs/editorial/gates.json`](docs/editorial/gates.json).

## What this repository contains

- [`docs/editorial/brief.md`](docs/editorial/brief.md) — purpose, audience, scope, non-goals, quality bar and licensing.
- [`docs/editorial/outline.md`](docs/editorial/outline.md) — approved parts, chapters, pilot candidate and approval criteria.
- [`docs/editorial/profile.md`](docs/editorial/profile.md) — the standard section profile and its allowed exceptions.
- [`docs/editorial/gates.md`](docs/editorial/gates.md) — the gate sequence, state transitions and what each gate authorizes.
- [`docs/editorial/gates.json`](docs/editorial/gates.json) — machine-readable gate state and the authorized pilot path.
- [`docs/setup.md`](docs/setup.md) — contributor setup, pinned install, fast checks and current limits.
- [`AGENTS.md`](AGENTS.md) — agent-neutral roles, workflow and editorial gates.
- [`DECISIONS.md`](DECISIONS.md) — decisions with explicit status.
- [`sdd/changes/0001-sample-bootstrap/`](sdd/changes/0001-sample-bootstrap/proposal.md) — bootstrap proposal and task record.
- [`sdd/changes/0002-pilot-gate-window/`](sdd/changes/0002-pilot-gate-window/proposal.md) — correction that separates pilot writing authority from Gate 3 approval.
- [`sdd/changes/0003-pilot-2-2/`](sdd/changes/0003-pilot-2-2/scope.md) — proposed scoped interpretation for the single-section pilot.
- `manuscript/` — canonical sources; currently contains only the pilot section 2.2.
- `publishing/` — metadata and publication plan; build configuration is deferred until the publication build setup lands.

## Quickstart for contributors

Readers of the handbook need no local tools. This quickstart is only for people who want to write, review or verify the repository.

You need Git, Python 3.11 or newer, and pip/venv. A hub checkout is **not** needed: `requirements.txt` installs the pinned toolkit directly from the public hub as a normal package.

The reviewed setup is available on `main`.

```sh
git clone https://github.com/cesarcastrocuba/handbook-sample-01.git
cd handbook-sample-01

cd ..
python3 -m venv handbook-sample-01-venv
source handbook-sample-01-venv/bin/activate

cd handbook-sample-01
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
make check
```

Keep the virtual environment outside the repository. The repository check rejects an in-repo `.venv` as a generated artifact.

If `make` is unavailable, run the same fast checks directly:

```sh
python -B -m unittest discover -s scripts/tests -p 'test_*.py'
python -B scripts/check_repo.py
handbook-toolkit validate-book book.yaml
```

`make check` covers gate-policy tests, repository consistency and the fast `validate-book` descriptor check. It does not validate chapter content or profile conformance.

`make full` runs the fast checks, full descriptor/reading-order validation, cross-reference validation and chapter-profile validation. It passes for Part I. No Quarto artifact build, manifest or checksums are produced yet.

Quarto and the render toolchain are future build setup; they are not required or installed now. Full prerequisites, limits and troubleshooting are in [`docs/setup.md`](docs/setup.md).

## Workflow

Work happens on short-lived branches and is reviewed by a different agent or person before the owner merges. Conventional commits are used. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Licensing

Handbook content is licensed under CC BY-SA 4.0; scripts and build configuration are licensed under MIT. See [`NOTICE.md`](NOTICE.md).
