# Game UI design workflow

[中文入口](../SKILL.md). Input: player task, real game state, supported devices/inputs/languages, layout constraints and authorized scope. Output: a bounded screen/flow contract, implementation when authorized, and observed interaction evidence. No other Skill is required.

For a new project, select a player decision and its minimum information; do not automatically add health bars, inventories or shops. In an existing game, inspect state and interaction code to distinguish missing information, display errors and rule defects. Preserve art direction. Design-only work does not authorize implementation.

Map information source → player decision → available action → feedback. Prioritize by urgency and frequency, not size or glow alone. Text, symbols, color and sound must agree; unknown state is not an invitation to fabricate production data.

Describe applicable entry, normal, empty, busy, error, disabled and return states. Each transition names input owner, initial focus, cancel semantics, focus restoration and side effects. Pausing is a project decision; a confirm event must not accidentally trigger both menu and gameplay. Define fallback focus for removed/hidden list items. Cover only declared inputs and do not claim all devices from one input test. Use the [UI contract](ui-contract.md) for a compact transition example.

Express layout with containers, alignment and size constraints; check long text, scaling and supported aspect ratios. Verify safe areas and touch targets on target devices rather than copying pixel thresholds. Use the existing layout system, not mandatory DOM/Canvas/frameworks. Implement a recoverable screen with real state bindings. Read-only presentation and action requests have distinct roles; business results drive success/failure feedback.

Exercise entry, action and return using normal input, plus relevant cancellation, repeated activation, disappearing focus targets and failure feedback. Compare equal-state/resolution images and supported narrow/long-text cases. Still images establish layout observations only; simulated dimensions do not establish hardware input behavior. Deliver transitions, edits, images, operations and separately scoped design, package, runtime and device evidence. No blanket accessibility certification without corresponding evidence. For critical overlay information over dynamic backgrounds, use [composited readability evidence](composited-readability.en.md) rather than checking design color alone.

[Sources](sources.md).
