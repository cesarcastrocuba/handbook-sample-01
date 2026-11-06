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
