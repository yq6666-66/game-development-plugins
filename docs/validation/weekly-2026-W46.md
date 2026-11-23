# Weekly integration validation · 2026-W46

Execution date: 2026-11-16. Reporting window: Asia/Shanghai 2026-11-09 00:00 to 2026-11-16 00:00, end exclusive. Baseline: `e1317d98e4d4dccd9e4f9250a20a9cb6250ca30e`. New review branch: `weekly/2026-W46`. Prior main content is preserved; today's daily branch and the guarded-release workflow are excluded.

## Actual checks

Executed in the Linux workspace, repository root, with existing Python and no new dependencies:

```sh
python3 scripts/validate_package.py
python3 -m unittest discover -s tests -v
git diff --check
git merge-base --is-ancestor <recorded-source-SHA> HEAD
```

- Package validator: PASS.
- Unit tests: 27/27 PASS, including isolated single-Skill copies and missing-reference negative tests.
- Whitespace/diff check: PASS. Final changed/new-file list was inspected before remote commit creation.
- All seven historical source commits listed for daily/fourth-pass/contracts/legacy integration in the weekly ledger are ancestors of the baseline: PASS. Remote old daily names are absent; their exact deletion times are not established.
- New local Markdown targets in changed/new documents: checked for file existence; not a general Markdown parser, fragment validator or external-link availability test.
- GitHub metadata and full branch/PR inventory read: default main, push permission, no existing week branch and no open PR. Permission does not authorize main merge or release.

## Document-level scenario walkthroughs

These are synthetic reasoning checks, not executed games or host model tasks. Normal input steps in a worksheet are instructions for future authorized use, not claims that those actions ran.

| Scenario | Expected route / checked property |
| --- | --- |
| Await returns after timeout, no business event | Do not mark the expected-success check PASS; preserve operation outcome and test verdict separately |
| A correct stale-write rejection | Conflict check may PASS under the specified policy; do not remove the lock to hide the conflict |
| Screenshot run omitted a planned case | Account for the missing terminal result; no whole-suite PASS |
| Local-only scalar prototype | Exclude cloud and object-relationship complexity instead of adding features |
| Nonmodal conversation permits movement | Follow the existing contract; do not enforce global pause merely because the UI is open |
| Pixel fixture hides HUD but normal play shows occlusion | Retain the interactive failure; controlled image evidence cannot override it |
| Planning-only user request | Fill expected evidence, leave execution unperformed; no automatic engine run or service access |

Independent read-only review covered the changed text and synthetic cases. Its cloud-save timing concern was corrected in both languages: disconnection occurs before remote acknowledgement; an already acknowledged state is retained. Its creation-date query was checked against GitHub repository metadata (`created_at=2026-11-13T19:09:25Z`), not inferred from the initial commit.

The bilingual entry routes point to existing local references; the new worksheet's mandatory detail remains inside its own Skill directory. Weekly synthesis opinions are explicitly provisional and remain in the report rather than being presented as universal tested rules.

## Evidence layers and exclusions

| Layer | This run |
| --- | --- |
| Repository/source reading | Existing recorded research, related references and commit/branch ancestry inspected; no claim of rereading all upstream repositories |
| Package/unit checks | PASS as scoped above |
| Document scenario reasoning | Completed; not an engine or empirical efficacy result |
| Codex/Claude host loading or actual invocation | NOT RUN; historical records unchanged |
| Unity/Godot/Three.js game or target device | NOT RUN |
| Cloud-save service, paid APIs, new tool installation | NOT RUN |
| Remote GitHub Actions | Check exact pushed commit separately; local PASS is not remote CI PASS |
| Main merge, release, branch deletion | NOT PERFORMED |

Recovery: the exact baseline Git commit plus a pre-edit local archive preserves the original files. No historical validation record was overwritten. No version bump, executable workflow, game asset or third-party copied content is included.
