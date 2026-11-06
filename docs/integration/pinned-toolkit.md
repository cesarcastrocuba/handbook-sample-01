# Pinned toolkit integration

| Field | Value |
| --- | --- |
| Status | Current — toolkit pin below; Gates 1 and 2 approved, Gate 3 pending |
| Toolkit source | `https://github.com/cesarcastrocuba/handbooks-hub.git` |
| Full commit SHA | `0e8d897acae67d55eb09bf06a6e890d07d187779` (hub `main` toolkit pin) |
| Toolkit version | `0.1.0` |
| Install mode | Direct Git requirement, non-editable, `#subdirectory=tools` |
| Profile reference | `standard` `0.2.0` — approved and integrated on hub `main` at `8ee28a081399155a250ea8bc45d8492245ab2377` |

## 1. Metadata sources

- `book.yaml` is the draft book descriptor consumed by the toolkit. It records the toolkit version, profile reference, manuscript root, reading order, licensing and catalog metadata.
- `requirements.txt` is the only install source. It pins the public hub repository to the full commit SHA above and installs the `tools/` subdirectory as a normal package.
- `publishing/metadata.yaml` remains provisional publication metadata. It does not replace `book.yaml` and is not consumed by the toolkit yet.
- The editorial contract lives in `docs/editorial/brief.md`, `outline.md`, `profile.md` and `gates.json`.

No toolkit scripts, schemas or profile files are copied into this repository. Installation does not read a parent checkout and is not editable.

## 2. Profile dependency

`book.yaml` references approved hub `standard` `0.2.0`. The pinned toolkit source (`0e8d897`) predates the profile integration and contains `standard` `0.1.0`. Profiles are hub repository resources, not files in the installed `handbook-toolkit` package; the package contains schemas only. Profile `0.2.0` is approved and integrated on hub `main` at `8ee28a0`.

The toolkit pin and profile source are separate: the installed package comes from `0e8d897`, while the editorial reference is the approved `0.2.0` profile at `8ee28a0`. This book remains `status: draft`.

- No claim is made that the pinned toolkit validates profile `0.2.0`.
- The pinned toolkit validates the descriptor schema only, not the profile's contents.
- The fast check does not validate profile conformance.

If the approved profile changes, `book.yaml` must be updated before the next gate that depends on it.

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
- Profile `0.2.0` is approved and integrated at hub `main` `8ee28a0` but is not present in the pinned toolkit revision. Profiles are not installed with the toolkit package, and the fast check does not validate profile conformance.
- CI proves installation and the fast check from a clean GitHub runner. It does not prove publication readiness.

## 5. CI

The workflow installs `requirements.txt` on a clean runner and runs `make check`. It triggers on pushes to `main` and `feat/**`, on pull requests, and via `workflow_dispatch`, so the integration branch can be verified without merging.
