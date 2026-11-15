# Legacy-method distillation validation · 2026-11-15

Baseline: `84848c85038e282d449e3535eb32e3161fcbcc46`. Source documents: planning `95fbdc9ac9830eaa62fbda95021dfec1d05185f8`; old visual Skill `b0c6c185f24155dfade2941280e6202c0d493a87`. Existing method principles were already generalized in main. This change adds portable bilingual worksheets, not a new Skill and not the historical project files.

## Scenario reasoning (not runtime tests)

| Scenario | Expected decision checked against the worksheet |
| --- | --- |
| Existing build and editor disagree | Identify the target baseline; do not combine before/after evidence from different versions |
| Authorized new 2D sample has no old assets | Establish labeled reversible assumptions; do not incorrectly block on missing prior project |
| Reference is a shooter, target is a puzzle | Borrow value/readability relationships, not weapons or combat UI |
| Still improves but movement hides HUD | Reject overall acceptance; preserve the dynamic failure |
| Exposure is the experimental variable | Hold other relevant conditions, not the variable itself, fixed |

These are document-level scenario walkthroughs by the implementing agent, not an independent host evaluation. No engine, game, target device or screenshot workflow ran. No new third-party code or assets are included. Package/static test results below apply only to the final package files.

## Executed checks

On 2026-11-15 in the Linux workspace: `python3 scripts/validate_package.py` PASS; `python3 -m unittest discover -s tests -v` 20 tests PASS; `git diff --check` PASS. Skill-copy/link regressions are included in package tests; none proves host loading or engine behavior.
