# Pinned toolkit integration

| Field | Value |
| --- | --- |
| Status | Current — published; toolkit pin below |
| Toolkit source | `https://github.com/cesarcastrocuba/handbooks-hub.git` |
| Full commit SHA | `5f9620237b61c0a01803f6705604c1c738ccee10` (hub `main` toolkit pin) |
| Toolkit version | `0.4.0` |
| Install mode | Direct Git requirement, non-editable, `#subdirectory=tools` |
| Profile reference | `standard` `1.0.0` — current packaged release; preserves the approved `0.2.0` rules |

## 1. Metadata sources

- `book.yaml` is the book descriptor consumed by the toolkit. It records the toolkit version, profile reference, manuscript root, reading order, licensing and catalog metadata.
- `requirements.txt` is the only install source. It pins the public hub repository to the full commit SHA above and installs the `tools/` subdirectory as a normal package.
- `publishing/metadata.yaml` remains provisional publication metadata. It does not replace `book.yaml` and is not consumed by the toolkit yet.
- The editorial contract lives in `docs/editorial/brief.md`, `outline.md`, `profile.md` and `gates.json`.

No toolkit scripts, schemas or profile files are copied into this repository. Installation does not read a parent checkout and is not editable.

## 2. Profile dependency

`book.yaml` references hub `standard` `1.0.0`, the current approved and packaged profile. Toolkit `0.4.0` ships both the `0.2.0` and `1.0.0` snapshots. Profile `1.0.0` keeps every approved `0.2.0` rule unchanged and adds the explicit validation classification. Profiles remain installed toolkit resources; this book does not copy them.

The installed toolkit comes from the commit above and provides `build-book` with staged render resources, manifest and checksum verification. This book is `status: active`.

- The fast check validates only the descriptor and reading order; full checks validate chapters against an explicit packaged profile.
- The fast check does not validate profile conformance by itself.

If the approved profile changes, `book.yaml` must be updated before the next gate that depends on it.

## 3. Checks

```sh
make test          # local gate-policy tests, standard library only
make check         # tests, local repository checks and fast validate-book
make full          # descriptor, reading order, references and all chapters
```

`make check` requires the pinned toolkit to be installed:

```sh
python3 -m pip install -r requirements.txt
```

The fast `handbook-toolkit validate-book book.yaml` check verifies the descriptor schema, the manuscript root, and the reading order. `make full` adds reference validation and `validate-manuscript` for every chapter. Artifact validation is still separate.

## 4. Limits

- All eight chapters and three appendices are present. `make full` passes descriptor, reading order, references and chapter validation.
- No artifact is committed. Releases and the Pages site are produced by the manual release workflow; `v0.2.0` is the latest.
- Profile `1.0.0` is the current packaged release and preserves the approved `0.2.0` rules; `make full` resolves the profile version from `book.yaml`.
- CI proves installation and the fast check from a clean GitHub runner. It does not prove publication readiness.

## 5. CI

The workflow installs `requirements.txt` on a clean runner and runs `make check`. It triggers on pushes to `main` and `feat/**`, on pull requests, and via `workflow_dispatch`, so the integration branch can be verified without merging.
