# Publishing

This directory holds publication metadata and, later, the pinned build configuration. **No build is configured or claimed during bootstrap.** Quarto is not installed in the bootstrap environment.

## Current state

- `metadata.yaml` records the working title, version and licensing intent.
- No `_quarto.yml`, reading order or style bundle exists yet.
- No HTML, PDF, DOCX, source bundle, manifest or checksum has been produced.
- No deployment, GitHub Pages site, catalog entry or release exists.

## Planned pipeline

1. Pin the hub toolkit version and record it here.
2. Declare the reading order from `manuscript/`.
3. Build once from an owner-approved commit with a fixed source epoch.
4. Verify structure, links, profile conformance and artifact identity.
5. Publish HTML for reading and attach PDF, DOCX, source bundle, manifest and checksums to a release.
6. Reference the approved release from the hub catalog only after owner approval.

## Constraints

- Generated artifacts are never committed; see [`.gitignore`](../.gitignore).
- The toolkit is installed from the hub at a pinned version. Shared scripts are not copied into this repository.
- A release must identify the exact commit and the checksums of every artifact.
- Publication requires owner approval and a confirmed licensing/attribution record.

Build configuration is intentionally deferred until the pilot section is approved, so that the first configuration can be tested against real content rather than an empty book.
