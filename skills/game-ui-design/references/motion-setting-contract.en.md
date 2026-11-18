# Reduced-motion settings: configuration and information contract

[中文](motion-setting-contract.md). Use only for dynamic UI or additive camera effects already in scope. Do not add camera perspectives or change gameplay automatically.

## Source boundary

Microsoft, [Xbox Accessibility Guideline 117](https://learn.microsoft.com/en-us/xbox/accessibility/xbox-accessibility-guidelines/117), updated 2026-11-13; read 2026-11-18. Read goals, overview, scoping questions, implementation guidance and example descriptions, not linked videos or image pixels. No engine version, source execution or runtime evidence. The guidance supports player control over nonessential movement, not freezing the entire game. Original synthesis only; no reused assets or medical safety guarantee.

## Proposed repository workflow

1. Inventory effects, triggering events, owners and conveyed information. Separate decoration from rules and necessary feedback; the project decides disablement and alternatives.
2. Define what off means: freeze, reset or hide; when it applies; and its persistence scope. A zero setting is not behavioral evidence.
3. In an authorized recoverable copy, compare the same event with default and reduced effects. Preserve required state, direction and result information; do not pass by pausing gameplay or skipping the event.
4. Toggle during an effect, leave/re-enter and trigger again. Restart only where persistence is promised. Compare visible behavior with settings; old animation jobs must not restore disabled effects.
5. Use normal input to check camera control, focus and timing. Rule/input changes require separate gameplay acceptance rather than a visual-only label.

Record setting/effect → application time → static/alternative feedback → re-entry/persistence → observed evidence. Missing device/user testing remains unverified. A recording describes a sample, not universal comfort, photosensitivity safety or accessibility certification. Budget for lifecycle investigation and paired regressions; no new dependency is required.
