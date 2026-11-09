# Contributing

This is a sample book repository. Contributions follow the same rules as the platform it demonstrates.

## Before you start

Read [`AGENTS.md`](AGENTS.md), [`PROJECT_STATUS.md`](PROJECT_STATUS.md), [`docs/editorial/gates.md`](docs/editorial/gates.md) and the [editorial brief](docs/editorial/brief.md). Do not add manuscript `.qmd` files before Gates 1 and 2 are approved. Once they are approved, only the pilot file at `pilot.path` in [`docs/editorial/gates.json`](docs/editorial/gates.json) may be added while Gate 3 is pending. The check enforces that file boundary only; reviewers confirm the file contains only section 2.2 and that the gate approval record is real. Every other chapter stays blocked until Gate 3 approval. The current gates are listed in `PROJECT_STATUS.md`.

## Branches and commits

- Branch from `main`: `<type>/<topic>`, for example `fix/outline-link`.
- Use Conventional Commits, for example `docs(editorial): clarify pilot scope`.
- Keep one work unit per commit. Tests and documentation belong with the change they verify.
- Do not add AI attribution or co-author trailers.

## Pull requests

A pull request states:

1. the gate or decision it serves;
2. the files and behavior changed;
3. the exact checks run and their results;
4. any check not run and why;
5. the rollback boundary.

A different agent or person reviews the exact HEAD. The implementer never reviews or merges their own change. The owner merges. `main` is protected (`DEC-015`): direct pushes are rejected, including for administrators.

## Content checks

Run:

```sh
make check
```

`make check` runs the gate-policy unit tests and then the repository check. Report the command and output. Do not claim a build, render or publication that was not executed. Quarto is not installed in the bootstrap environment, so publishing checks are explicitly deferred.

## Reviewer environment

A reviewer starts from a clean clone at the exact commit under review. The pinned toolkit is installed from `requirements.txt`; a hub checkout is not needed.

Create the virtual environment outside the repository, then install the requirements:

```sh
git clone https://github.com/cesarcastrocuba/handbook-sample-01.git
cd handbook-sample-01
python3 -m venv ../review-venv
../review-venv/bin/python -m pip install --upgrade pip
../review-venv/bin/python -m pip install -r requirements.txt
```

Run the full check with the Makefile variables pointing at that environment:

```sh
make full PYTHON=../review-venv/bin/python TOOLKIT=../review-venv/bin/handbook-toolkit
```

Alternatively, put the environment on `PATH`; the Makefile then resolves both `python3` and `handbook-toolkit` from it:

```sh
PATH="../review-venv/bin:$PATH" make full
```

`make full` runs the fast checks and then the full descriptor, reading-order, reference and chapter/appendix validation. Record the exact commit, command and result in the review.

## Editorial rules

- English, vendor-neutral, evidence-oriented.
- Follow the [content profile](docs/editorial/profile.md); declare exceptions.
- Label illustrative examples.
- Cite sources that exist and can be checked. Never invent a citation, measurement or review result.
- Respect the licenses in [`NOTICE.md`](NOTICE.md); do not add third-party material without a rights review.
