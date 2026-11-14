# Branch integration · 2026-11-14

Owner requested merging existing work and deleting merged branches. This record covers documentation/Skill integration, not a release or game execution.

## Inputs and preservation

- Default `main`: `48915481118f7886a02ad2e7dea089436953186b`.
- Fourth pass: `8f53b8b2bbb9e860a6f33772886ea666970b1004` (includes bilingual navigation `dc01400cb2de59bed6465cb0a0955dbb54ece686`).
- Daily research: `636fc870754c91cac2664a793d8660770fd2bc41`.
- Earlier `refactor/general-public-v3` at `0a6083cf88f38e37dd54f46deabe6d9e5aabd687` is already an ancestor of main.

Both source histories remain merge parents/ancestors, so their commits can recover deleted branch refs. A complete local pre-integration Git bundle was retained. No history rewrite, automatic merge setting or release is part of this operation.

README and PROVENANCE append conflicts were resolved by retaining both contributions. Chinese-first README is preserved and its daily-research summary is mirrored in English. Historical validation records retain their original dates and limits.

## Excluded legacy branches

`planning/visual-improvements` (`95fbdc9ac9830eaa62fbda95021dfec1d05185f8`) and `skills/game-visual-iteration` (`b0c6c185f24155dfade2941280e6202c0d493a87`) are NOT ancestors of main. They contain project-specific historical material deliberately excluded from the public generic package. They are retained, not blindly merged or deleted. This operation does not claim all their unique work is preserved in the private game repository.

## Checks on integrated content

Executed in the Linux workspace on 2026-11-14:

- `python3 scripts/validate_package.py`: PASS, four Skills.
- `python3 -m unittest discover -s tests -v`: PASS, 6 tests.
- `git diff --check`: PASS.
- Merge review: both playloop reference routes retained; four Skill directories present; no legacy project directory restored.

No upstream tool, agent host, engine, real game or target hardware was run. No CI success is claimed; the repository has no checked-in workflow at this revision. Remote head and tree identity must be checked after updating main, and branch deletion must follow that confirmation.
