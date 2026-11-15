# Guarded GitHub releases

[中文](README.md)

This workflow publishes GitHub Releases only. It never merges branches or submits to official stores. Research branches (`distill/*`, `weekly/*`) cannot trigger it. Adding the workflow alone does not publish anything; no executable approval record is shipped.

## Version-bound approval

1. Review and merge the candidate version using the project's authorization process. Fix its full source commit SHA on `main`; update both manifests and CHANGELOG.
2. Verify that exact version/commit in both hosts: isolated install, **real skill invocation**, update and uninstall. Record host versions, platforms, inputs, outcomes and logs. Structural checks, mocked calls and historical waivers are not runtime evidence. Cover every platform required by the approved release scope and disclose untested platforms.
3. Build the deterministic allowlisted archive and record its SHA256. Store full runtime logs under `docs/validation/`, hash them, and bind each evidence item to the source SHA and version.
4. After review, add exactly one new `docs/releases/approvals/X.Y.Z.json` to `main`. This push automatically checks, builds and publishes. The approval directory is a trust boundary: `approved: true` represents an actual reviewer decision, not self-certified research readiness.
5. Read-only checks validate the record, source ancestry, manifest versions and evidence digests, then run existing validation/tests/build in a detached worktree and compare the ZIP digest. Only the publication job receives `contents: write`. It does not execute the target commit's build code with write access.
6. Publication rejects existing tags/releases/drafts, atomically creates a tag at the approved commit, creates a draft, uploads assets, checks server-returned digests/sizes and the tag target, then publishes. Missing digests, API failures and permission errors fail closed.

## Record schema

The Chinese guide contains a deliberately non-executable example. Top-level fields: `version` (formal X.Y.Z), `source_sha` (40 lowercase hex), `artifact_sha256` (64 hex), `approved: true`, `scope: github-release`, `reviewer`, `approved_at`, `evidence`.

The evidence map requires exactly `codex-install`, `codex-invoke`, `codex-update`, `codex-uninstall`, `claude-install`, `claude-invoke`, `claude-update`, `claude-uninstall`. Each entry includes `path` under `docs/validation/`, `sha256`, matching `source_sha`/`version`, `status: PASS`, `host_version`, `platform`, `date`, `input`, and `observed`. Each evidence file is structured JSON repeating the matching source/version/status/host/platform/date/input/observed fields, plus `operation` matching its map key, `mode: actual-host-runtime`, the approved `artifact_sha256`, and `log: {"path": "docs/validation/runtime.log", "sha256": "actual digest"}`. Update evidence additionally requires `update_scope: remote-candidate-end-to-end`: a real isolated remote candidate update, not a synthetic local-folder version test. The gate validates these fields and the referenced log hash. Nonempty fields and digest checks do not prove that a test happened; reviewer verification remains essential. The 0.1.0 one-time limited-validation exception is not inherited. Republishing 0.1.0, prereleases, missing evidence and skipped checks are rejected.

## Permissions, recovery and limitations

Use only GitHub's ephemeral `GITHUB_TOKEN`: read by default, write in the publish job. Do not create credentials or weaken repository/organization settings. If policy blocks execution, report it for owner resolution. Actions are pinned to full upstream commit SHAs.

Versions must advance all existing stable releases and formal-version drafts; publication explicitly sets latest. Runs serialize; ongoing publication is not cancelled. If a tag or draft exists on retry, stop rather than overwrite, move or delete it. A partially failed run may leave a public tag and a draft (failure is not zero remote side effects): preserve logs and request a separately reviewed recovery. No automatic rollback, cleanup or resume is implemented.

Asset digest validation occurs before public release and relies on GitHub's server digest, not a user-device installation test. Official store submission, remote host update propagation and game/engine compatibility remain separate.

This candidate has only local static and mocked tests, not a real Actions execution. No real tag/release was created for testing and no repository setting changed. See [validation](../validation/guarded-release-2026-11-15.md).

Official sources checked 2026-11-15: [GITHUB_TOKEN](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token), [secure use](https://docs.github.com/en/actions/reference/security/secure-use), [Release API](https://docs.github.com/en/rest/releases/releases). Action v4 SHAs were resolved with `git ls-remote` against official repositories. This repository's MIT license does not replace upstream licenses.
