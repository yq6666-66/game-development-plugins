# Readability evidence in composited frames

[中文](composited-readability.md). Apply to important information on the scoped screen, not every decorative/game pixel.

## Source and adaptation

Microsoft, [XAG 102: Contrast](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/102), updated 2026-11-13; read 2026-11-18. Full text and example descriptions reviewed; no example image/video inspection or game execution. The source considers varying backgrounds and worst regions. Requirements differ by element type, size and mode: check the current standard rather than hardcoding one ratio. No source-code version or hardware pass is claimed.

## Original evidence card

1. Name a player information chain: notice target, distinguish state, act. Identify its state source and protected invariants.
2. Fix route and UI state; sample bright, dark and busy backgrounds. Include flashes, overlays and transitions only when present. Separate planned samples from actual coverage.
3. Inspect the worst location in the composited frame, not just editor color values. Record element, background, opacity, display/render settings, method, applicable standard and result. A translucent panel's raw color is not its composited background.
4. Verify default and supported customized modes separately. Panels/outlines must not hide essential information; disabled choices still need understandable reasons. Saturation alone does not fix state semantics.
5. Complete the information chain through normal input. Report measurements, dynamic observations and user-understanding evidence separately. Missing target displays, operations or user studies remain unverified.

Counterexamples: a night-scene pass fails against sky; a translucent panel fails during a bright effect; custom colors obscure state differences. Observe rather than presume these defects. Budget for relevant state/background combinations, not unrelated exhaustive scenes. Contrast does not prove lack of occlusion or timely understanding; assess HDR, tone mapping and scaling against the actual pipeline. Original workflow and links only; no third-party assets copied.
