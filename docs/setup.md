# Book setup for contributors

This guide is for people who want to contribute to or verify this book repository. **Readers of the published handbook need no local tools.** No Git, Python, Quarto or platform checkout is required to read the book.

The setup below installs the pinned shared toolkit from the public hub. It does **not** require a hub checkout, a parent repository, an editable install or `PYTHONPATH`.

## 1. Prerequisites

| Requirement | Notes |
| --- | --- |
| Git | Any current Git 2.x release |
| Python | `3.11` or newer; `3.12` is recommended and used by CI |
| pip and venv | Usually packaged with Python; on Debian/Ubuntu install `python3-pip` and `python3-venv` if missing |
| Network access | Needed only for the first package install |
| `make` | Optional. GNU Make runs the same checks; a no-make path is below |

Quarto, Graphviz and render tooling are **not required** for the current fast checks. They belong to a future build-setup change and are not installed or claimed here.

## 2. Quickstart

Create the virtual environment **outside** the repository. A local `.venv` is rejected by the repository check as a generated artifact, even though Git ignores it.

```sh
git clone https://github.com/cesarcastrocuba/handbook-sample-01.git
cd handbook-sample-01

# After integration, main contains this setup.
# While reviewing before integration, check out the reviewed branch instead.

cd ..
python3 -m venv handbook-sample-01-venv
source handbook-sample-01-venv/bin/activate

cd handbook-sample-01
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

make check
```

On Windows, use PowerShell:

```powershell
cd ..
py -3.12 -m venv handbook-sample-01-venv
.\handbook-sample-01-venv\Scripts\Activate.ps1
cd handbook-sample-01
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

On Windows, use the no-make commands in section 3. If Make is installed, run `make check PYTHON=python`.

`requirements.txt` installs `handbook-toolkit` directly from the public hub at the full commit recorded there, using `#subdirectory=tools`. It is a normal non-editable package install. Do not clone the hub next to this repository, do not point `PYTHONPATH` at a hub checkout, and do not run `pip install -e` against the toolkit.

## 3. Run checks without make

From the repository root, with the sibling virtual environment active:

```sh
python -B -m unittest discover -s scripts/tests -p 'test_*.py'
python -B scripts/check_repo.py
handbook-toolkit validate-book book.yaml
```

These are the same checks `make check` runs. `-B` prevents Python bytecode caches, which the repository check treats as generated artifacts.

## 4. What the fast checks mean

- The local tests cover the gate-state policy and pilot file boundary.
- `scripts/check_repo.py` checks required files, relative links, environment-specific paths, role names, gate ordering and the absence of manuscript prose.
- `handbook-toolkit validate-book book.yaml` checks the descriptor schema, the manuscript root and the reading-order file. It does **not** read chapter content or verify profile conformance.

A fast pass is not a publication or full-manuscript pass.

## 5. Current limits

- The complete draft exists. `make full` validates chapter structure and references; it does not judge editorial quality.
- `make full` runs descriptor, reading-order, cross-reference and chapter-profile validation and passes. It does not build artifacts.
- Toolkit `0.2.0` provides `validate-references` and `validate-manuscript`; artifact manifest/checksum validation remains separate.
- The book references hub `standard` `0.2.0`, approved and integrated on hub main `8ee28a0`. The fast check does not validate profile `0.2.0`.
- No HTML, PDF, DOCX, source bundle, manifest or release is produced.

## 6. Future build setup

Quarto and the render toolchain are intentionally deferred. A later build-setup change will pin those versions and add the build commands. Until then, do not install or claim a Quarto render, and do not expect `make check` to build the book.

## 7. Troubleshooting

| Symptom | Check |
| --- | --- |
| `No module named pip` | Install `python3-pip`, or recreate the venv with venv support installed |
| `handbook-toolkit: command not found` | Activate the sibling venv and rerun `python -m pip install -r requirements.txt` |
| `make: command not found` | Use the no-make commands in section 3 |
| Install cannot reach the hub | Confirm network access to `github.com`; do not substitute a local hub checkout |
| Repository check reports `.venv` | Remove the in-repo `.venv`; the venv must be a sibling outside the repository |
