# Validation record

Candidate scope: third distillation into a reusable instruction bundle. No game engine, upstream plugin or paid service is executed by these package checks.

## Automated checks

Executed in the current Linux workspace on 2026-11-14: package validator PASS; six unit tests PASS (including negative cases); both skills passed the Codex skill-creator frontmatter validator. These results do not establish host installation or engine behavior.

Run `python3 scripts/validate_package.py` and `python3 -m unittest discover -s tests -v` from the repository root. The validator checks skill names/frontmatter, required reference existence, absence of unfinished scaffold text, and local Markdown links inside the distributed skills. Unit tests include deliberate invalid frontmatter and missing references to show the validator rejects them.

## Behavioral evaluation

The second-distillation skills were tested on simulated task responses for asset-import discrepancies and restart/event accumulation. Those were instruction-following tests, not game runs. Third-distillation independent task-response evaluations were reported by reviewers on 2026-11-14:

| Scenario | Observed behavior | Review finding and correction |
| --- | --- | --- |
| 2D cross-genre task | Did not force Unity, weapons or a fixed two-retry rule | Descriptions limited scope to existing games. Both now allow an explicitly authorized new prototype with labeled, reversible assumptions; existing-project rules must not be invented. |
| Unity visual task | Overall scoped diagnosis and evidence approach was appropriate | Clarified that a plan/diagnosis request does not authorize writing copies or running an engine. Controlled comparisons now hold all relevant conditions except the experiment variable fixed, so an exposure experiment may change exposure. |

These were independent instruction-following walkthroughs, not actual 2D or Unity game execution. The corrections received package/static checks below; no post-correction independent behavioral rerun or host discovery is claimed.

## Release checklist

- [x] MIT approved for the original package; inherited icons excluded because provenance was not established.
- [x] Third-distillation independent task evaluations and their limitations recorded.
- [x] Owner-authorized independent review-branch upload only; no main merge or release authorized.
- [ ] Host discovery tested if claiming an installed integration.

Unverified: runtime behavior of Unity, browsers or other engines; target hardware; upstream tool security; commercial rights for third-party assets. A package-validation PASS does not change these statuses.

## 双宿主插件候选验证

见[2026-11-15 独立记录](validation/dual-host-plugin-2026-11-15.md)。历史记录不变；包结构、宿主调用与游戏运行保持分层。
