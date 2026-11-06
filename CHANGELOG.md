# Changelog

All notable changes to this sample handbook are recorded here. The format follows Keep a Changelog; versions follow semantic versioning once releases begin.

## [Unreleased]

### Added

- Bootstrap scaffold for the sample handbook *Handbook Authoring and Publishing*.
- Agent-neutral roles, editorial gates and contribution workflow.
- Proposed editorial brief, outline and content profile.
- Lightweight SDD proposal for the bootstrap.
- Dependency-free repository consistency check.

### Fixed

- Removed the Gate 3 deadlock: Gates 1 and 2 now authorize the pilot file while Gate 3 is pending; Gate 3 approves the reviewed pilot and authorizes expansion.
- The check enforces only the pilot file boundary and gate ordering; section 2.2 scope and owner authorization remain review responsibilities.
- Corrected documentation and check output that overstated file-level enforcement as section-level or proof of owner authorization.
- Gate state is machine-readable in `docs/editorial/gates.json`, explained in `docs/editorial/gates.md`, and enforced by state-machine tests.
- Pinned public-hub toolkit integration via direct Git requirement at full SHA `0e8d897acae67d55eb09bf06a6e890d07d187779` with `#subdirectory=tools`.
- Draft `book.yaml` and empty `manuscript/book.yml`; profile reference is `standard` `0.2.0`, contingent on hub branch approval.
- CI installs the pinned toolkit and runs the fast `validate-book` check; `make full` fails explicitly until pilot, content validation and artifacts exist.
