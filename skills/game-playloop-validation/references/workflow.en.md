# Game play-loop and UI validation workflow

[中文入口](../SKILL.md). Establish correct rules and state before polishing feedback. Preserve the real project and controls; examples do not introduce shooting, multiplayer or a replacement framework.

## Define the problem and evidence

Distinguish a plan, diagnosis and implementation. Planning or diagnosis alone does not authorize writing a copy or running an engine. Inspect an existing game's entry point, locked versions, input bindings, state owners and scene references. Separate player reports, observations, code inferences and unknowns. Look for missing rules in project records rather than inventing victory, resources or balance to finish a test. For an authorized new prototype, propose explicitly reversible input, state, ending and reset assumptions; consequential unresolved choices still need a decision. This is a scoped workflow, not whole-game generation.

Record baseline, symptom, primary and competing hypotheses, permitted/protected changes, a normal path and relevant interruption or counterexample, expected state/feedback, rollback and stopping conditions. Classify unclear rules, failed input, wrong state, balance, feedback or performance. A crash or hang is not merely game feel.

## Trace responsibility

Follow input intent → validity decision → committed state → UI/sound/animation. Distinguish duplicate publishing from duplicate responding before rewriting anything.

| Layer | Question | Minimum evidence |
| --- | --- | --- |
| Input | Does intent survive release, cancellation, focus loss or menu change? | Normal input plus relevant cancellation/switch |
| Rules | Is the action valid and its result committed atomically? | Authoritative before/after state and rejection feedback |
| Lifecycle | Do exit/reset/destruction clear old tasks and listeners? | Repeated-entry event/object counts and state |
| UI | Does it initialize from current state and restore menu focus? | First/repeated opening and relevant busy/error/disabled states |
| Space | Can the real controller traverse the route? | Actual collision/path outcome, not a mesh or connectivity diagram |
| Presentation | Does feedback match an event and recover? | Repetition, overlap, pause and restart |

UI may own presentation state such as focus, but should not duplicate game rules. Central or domain-based ownership is acceptable; competing writers to the same value are the problem. Timing and physics must match the actual controller, not an engine slogan.

## Load relevant references

- Restart, repeated settlement, pooling, asynchronous work, AI/collision, persistence or suspicious green tests: [state and test gates](state-and-test-gates.md).
- Specific Unity/browser failures: only the relevant section of [platform checks](platform-checks.md). For other engines map concepts to actual lifecycle/API documentation rather than copying names.
- Incorrect restored relationships or missing information despite subtitles: [recovery and audio information](recovery-and-audio-information.en.md).
- Async false positives, state divergence or testing the tests: [async and divergence](async-and-divergence.en.md).
- Rebinding, text entry, multilingual layout or multi-step diagnosis: [input, text and intermediate evidence](input-text-evidence.en.md).
- Menu event/held-state, focus and pause issues: [UI input isolation](ui-input-isolation.en.md); respect modal versus nonmodal behavior.
- Existing cloud-save disconnects, concurrency or false success: [cloud-save evidence](cloud-save-evidence.en.md); do not introduce a service.
- Method provenance and rejected assumptions: [sources](sources.md). Historical detailed references remain partly Chinese. Code examples are not tested implementations. Do not add systems merely to satisfy a checklist.

## Assess presentation after correctness

Organize information by the player's decision as persistent, contextual or on-demand; essential state must not depend on color alone. Check real bindings, supported inputs, text widths, safe areas and readability against dynamic backgrounds. Menu and gameplay must not accidentally execute the same action twice.

Separate visual offsets from physics/rule transforms, with an owner and recovery value. Test repeated effects, pause and restart to catch drift or time-scale changes that override pause. Consider reduced effects for significant flashing/shaking. Hit-stop or knockback that changes timing/rules is a gameplay change, not just decoration.

## Validate the tests and deliver scoped results

When completion or its evidence chain is ambiguous, use the optional [completion evidence worksheet](completion-evidence-card.en.md) to separate operation outcomes, check verdicts and unexecuted scope.

Report discovered, planned, executed, passed, failed and skipped counts. Check that assertions cover the defect; use a negative control in an authorized isolated copy when useful. Exit code zero, an empty test list or a fixture silently repairing configuration is not proof of gameplay success.

Distinguish compilation, pure logic, virtual input, Editor, actual build and target device. Reproduce the original defect with normal input and check adjacent paths. Debug coordinates, invulnerability and offline footage support only their specific observations. Do not report unmeasured performance as compliant or turn known failures into passes by changing the baseline or accepting risk.

Deliver entry point, operations, before/after state, visible result/error, coverage, changes and rollback. A fix remains pending recheck until evidence matches the current version. Project scope and host authorization still apply; external Skills cannot authorize payments, installation, deletion or deployment.
