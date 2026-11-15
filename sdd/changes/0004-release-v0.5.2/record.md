# Prepare sample v0.5.2

Prepare the next edition with toolkit 0.11.0 under Owner decision DEC-031 / hub HUB-DEC-042.
The version is prepared and not published; the Owner must check the CI-built DOCX in desktop Word
before tagging. Independent review, merge and release remain separate actions.

## Scope

- Baseline: `a75046b4407383fddbbee02eeb47d4fbc68bc59b` (`origin/main`).
- Descriptor and direct Git requirement pin toolkit 0.11.0 at the full approved hub commit
  `d4bef53af4c70f86fecdb13d1924c79353dde32f`.
- Publication metadata prepares version 0.5.2. PROJECT_STATUS retains v0.5.1 as the published edition;
  CHANGELOG, DEC-031 and current pin documentation describe the new preparation.
- Manuscript and profile are unchanged. PR 29 did not update the manuscript revision history, so
  this preparation also leaves that history and all canonical prose untouched.
- The release verify job is ported from template 1.6.0 PR 78 at
  `9750655e6ca949d1d36c383c70e546455779b82d`: deploy output, dependent read-only job, credential-free
  checkout, pinned toolkit installation and deployment URL passed through `PAGE_URL` to `site_check`.
- Existing check.yml ran only fast checks and uploaded no editions. It now runs full checks and
  builds a preview with verified page numbers, uploading the seven-file `edition-preview` artifact
  including `book.docx`. This read-only CI path does not publish or deploy.

## Evidence

The pinned dependency was installed non-editably from requirements.txt into a sibling environment,
following docs/setup.md. An initial in-repository environment failed the artifact/link checker;
it was moved outside the repository and the documented environment layout was restored.

Executed:

```sh
PATH="$PWD/../v052-env/bin:$PATH" make full PYTHON=../v052-env/bin/python
git diff --check
git diff --exit-code origin/main -- manuscript
```

The full checks passed: 15 tests, required files, relative links, generated-artifact and environment
checks, gate/editorial consistency, descriptor/reading order, cross-references and all eight chapters
plus three appendices. All workflow shell blocks also passed `bash -n`. The two workflow regressions
check deployment-URL wiring and permissions, and that CI uploads a non-release preview.

The edition build runs in CI once the PR is opened; the run and artifact URL are recorded in the PR
body for the Owner. No local artifact build or publication result is claimed here. Generated files
remain outside source control. This preparation does not modify the hub or publish a tag/release.

Rollback boundary: revert the version/pin, release/check workflows, their tests, preparation metadata
and documentation together. No published release, catalog entry or reading-site deployment changes.
