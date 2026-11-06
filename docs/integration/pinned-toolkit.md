# Pinned toolkit integration

| Field | Value |
| --- | --- |
| Status | Current — Gates 1–3 approved; complete draft; local release candidate verified; toolkit pin below |
| Toolkit source | `https://github.com/cesarcastrocuba/handbooks-hub.git` |
| Full commit SHA | `66d0581689e1e9c91913da25b5cb4a7723f3ec5c` (hub `main` toolkit pin) |
| Toolkit version | `0.3.0` |
| Install mode | Direct Git requirement, non-editable, `#subdirectory=tools` |
| Profile reference | `standard` `0.2.0` — approved and integrated on hub `main` at `8ee28a081399155a250ea8bc45d8492245ab2377` |

## 1. Metadata sources

- `book.yaml` is the draft book descriptor consumed by the toolkit. It records the toolkit version, profile reference, manuscript root, reading order, licensing and catalog metadata.
- `requirements.txt` is the only install source. It pins the public hub repository to the full commit SHA above and installs the `tools/` subdirectory as a normal package.
- `publishing/metadata.yaml` remains provisional publication metadata. It does not replace `book.yaml` and is not consumed by the toolkit yet.
- The editorial contract lives in `docs/editorial/brief.md`, `outline.md`, `profile.md` and `gates.json`.

No toolkit scripts, schemas or profile files are copied into this repository. Installation does not read a parent checkout and is not editable.

## 2. Profile dependency

`book.yaml` references approved hub `standard` `0.2.0`. The pinned toolkit source (`66d0581`) includes the approved profile and its packaged snapshot. Profiles remain hub repository resources; this book does not copy them. Profile `0.2.0` is approved and integrated on hub `main` at `8ee28a0`.

The installed toolkit comes from `66d0581` and provides `build-book` with staged render resources, manifest and checksum verification. The editorial reference is the approved `0.2.0` profile at `8ee28a0`. This book remains `status: draft`.

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
- A local `0.1.0-rc.1` six-file build exists outside the repository. No artifact is committed and no release or Pages deployment exists.
- Profile `0.2.0` is approved and integrated at hub `main` `8ee28a0`; the pinned toolkit includes its packaged snapshot, while validation still uses an explicit profile path in `make full`.
- CI proves installation and the fast check from a clean GitHub runner. It does not prove publication readiness.

## 5. CI

The workflow installs `requirements.txt` on a clean runner and runs `make check`. It triggers on pushes to `main` and `feat/**`, on pull requests, and via `workflow_dispatch`, so the integration branch can be verified without merging.
