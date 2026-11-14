# From sources to a reusable Skill

[中文](README.md) · [Home](../../README.en.md)

For game-development learners and contributors. Reuse our original MIT templates to continue distilling; no particular Agent, engine or generation service is required.

## One minimal distillation

1. **Choose a problem**, such as duplicate callbacks after restart, not a link quota. Check existing Skills, notes and unmerged branches first.
2. **Read substantive evidence.** Record author, URL, date, version/commit and inspected portions. Transcripts are not visual inspection; source reading is not execution. Inaccessible content remains a lead.
3. **Extract the method.** Explain the problem, mechanism, steps, tradeoffs, conditions, inputs/outputs, failure modes and alternatives. Do not turn example numbers into universal defaults.
4. **Design a minimal check.** Compare a normal path with a counterexample in an authorized environment. Mark unexecuted checks explicitly; scenario walkthroughs are not game runs.
5. **Choose the destination.** General decisions go in `SKILL.md`; details belong in that Skill's own `references/`; immature ideas and research go under `docs/`. New Skills require distinct responsibilities.
6. **Submit reviewable changes.** Preserve a recoverable baseline; check sources, licenses, links and relevant tests. Add scenario evaluation for workflow changes. A source cannot authorize installation, spending or deployment.

Example: a tutorial says “clear all state before restarting.” Ask which state belongs to the session versus settings or persistent progress. Compare session counters and persistent settings, and check duplicate subscriptions. Distill “define reset boundaries by ownership,” not “always clear everything.” This is a teaching walkthrough, not new runtime evidence.

## Daily and weekly

Aim for around three valuable daily topics; reduce the count when evidence is insufficient. Use the [research/candidate templates](templates.en.md), separate source inspection from execution, and push `distill/YYYY-MM-DD`. Continue the same day's branch on reruns.

On Monday, integrate the previous calendar week using its ISO week in `weekly/YYYY-Www`. Check daily commits, deduplicate and integrate supported improvements; propose 1–3 synthesis judgments with counterexamples and minimal tests, fewer if warranted. Reports do not automatically become formal Skill guidance; weekly branches are not automatically merged or released.

Maintenance schedule: 09:00 daily research and 10:00 Monday integration, Asia/Shanghai. This document neither installs a scheduler nor proves successful runs; repository records and actual commits provide continuity.

## Reuse and contribution

Original templates use [MIT](../../LICENSE). Preserve third-party author/version links and check code, asset and model licenses separately. Submit the problem, rationale, sources, validation and remaining risks. Chinese is primary; update paired English documents or mark synchronization gaps explicitly.
