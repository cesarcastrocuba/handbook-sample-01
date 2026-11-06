# Pinned toolkit integration

| Field | Value |
| --- | --- |
| Status | Draft integration — no gate approved |
| Toolkit source | `https://github.com/cesarcastrocuba/handbooks-hub.git` |
| Full commit SHA | `0e8d897acae67d55eb09bf06a6e890d07d187779` (hub `main`) |
| Toolkit version | `0.1.0` |
| Install mode | Direct Git requirement, non-editable, `#subdirectory=tools` |
| Profile reference | `standard` `0.2.0`, proposed on hub branch `feat/topic-neutral-profile` |

## 1. Metadata sources

- `book.yaml` is the draft book descriptor consumed by the toolkit. It records the toolkit version, profile reference, manuscript root, reading order, licensing and catalog metadata.
- `requirements.txt` is the only install source. It pins the public hub repository to the full commit SHA above and installs the `tools/` subdirectory as a normal package.
- `publishing/metadata.yaml` remains provisional publication metadata. It does not replace `book.yaml` and is not consumed by the toolkit yet.
- The editorial contract lives in `docs/editorial/brief.md`, `outline.md`, `profile.md` and `gates.json`.

No toolkit scripts, schemas or profile files are copied into this repository. Installation does not read a parent checkout and is not editable.

## 2. Profile dependency

`book.yaml` references `standard` `0.2.0` because that version makes figures, tables and the review checklist topic-neutral. The pinned hub revision contains `standard` `0.1.0`. Profiles are hub repository resources, not files in the installed `handbook-toolkit` package; the package contains schemas only. Version `0.2.0` exists on the hub branch `feat/topic-neutral-profile` and is still **Proposed**.

The reference is forward-looking. The owner approved this book's direction at Gate 2 on 2026-11-06; the hub profile itself is still **Proposed**. Until the hub branch is approved and merged:

- this book remains `status: draft`;
- no claim is made that the toolkit can validate profile `0.2.0`;
- the pinned toolkit validates the descriptor schema only, not the profile's existence or contents.

If the hub branch is rejected or changed, `book.yaml` must be updated before any gate that depends on the profile is approved.

## 3. Checks

```sh
make test          # local gate-policy tests, standard library only
make check         # tests, local repository checks and fast validate-book
make full          # current-scope incomplete gate: fast checks pass, then it fails
```

`make check` requires the pinned toolkit to be installed:

```sh
python3 -m pip install -r requirements.txt
```

The fast `handbook-toolkit validate-book book.yaml` check verifies the descriptor schema, the manuscript root, and that the reading-order file exists and is syntactically valid. It does not validate chapter content, profile conformance, links or artifacts.

## 4. Limits

- No pilot or chapter `.qmd` exists yet. `validate-book --full` is not run now, but may run once Gates 1 and 2 permit the pilot and that file exists.
- `make full` is a current-scope incomplete content-and-artifact gate, not a descriptor failure. The fast descriptor check passes.
- The manuscript content validator, Quarto build, artifact manifest and checksums are not implemented in toolkit `0.1.0`. Artifact validation is not run.
- Profile `0.2.0` is not present at the pinned hub revision. Its use is a proposed reference, not an approved contract; profiles are not installed with the toolkit package.
- CI proves installation and the fast check from a clean GitHub runner. It does not prove publication readiness.

## 5. CI

The workflow installs `requirements.txt` on a clean runner and runs `make check`. It triggers on pushes to `main` and `feat/**`, on pull requests, and via `workflow_dispatch`, so the integration branch can be verified without merging.
