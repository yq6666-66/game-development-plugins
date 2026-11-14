# Async checks and first state divergence

[中文 and pinned sources](async-and-divergence.md). Apply only to in-scope async behavior or reproducible state defects. Do not require Godot, a replay architecture, telemetry or new gameplay systems.

## Bounded waiting is not success

Input: expected event/condition, clock, timeout and cancellation contract. Output: termination reason, operation result, business state and cleanup evidence.

Choose the actual render/physics/event/condition boundary. Register observation before triggering potentially synchronous completion. Make waiting bounded; assert its result and the business state separately. A returned coroutine or zero process exit is insufficient. Cover normal completion and a missing/cancelled result, including stale callbacks after restart.

Test production exit/reset before fixture cleanup. Otherwise automatic disposal can conceal a product leak. Object counts, listeners and resources have different observation limits. In the pinned GUT source, `wait_for_signal` and `wait_until` report whether completion preceded timeout; `assert_no_new_orphans` checks current orphan Nodes, not every leaked resource. Match actual Godot/GUT versions; do not transplant sample delays.

## Earliest observation versus cause

Record build, setup, relevant configuration/random state, ordered input and predeclared invariants. When replay is not deterministic, report variability instead of inventing a stable event index or rewriting the architecture without approval.

Trace only the minimal reproduction, retaining within-tick order, stable identity, read/write values and invariant outcomes. Scan for the earliest observable violation. Bisection requires the relevant monotonicity and faithful checkpoints; a value may fail then recover. Follow the actual dependency chain, not merely the earliest writer of a field. A failure at index zero can expose initialization defects as well as bad setup.

An isolated single-variable intervention can strengthen a causal explanation, but deleting an event may also invalidate preconditions. Distinguish first violation, suspected writer and established cause, and list unobserved state.

## Known-bad controls

Only within authorized test evaluation, use recoverable copies to introduce a meaningful defect with a predefined failure expectation. Keep healthy baseline and defective case separate from release artifacts.

Distinguish suite detection from Agent repair evaluation. Separate invalid, unreachable and behaviorally indistinguishable-under-tested-input cases; finite agreement is not proof of equivalence. Agent evaluation requires genuine answer isolation and a healthy control, not just a different folder in a shared repository. Judge behavior rather than matching a reference diff, and reserve unseen cases for remeasurement. One detected defect does not establish general Skill effectiveness.

## Evidence

Pinned reading and licenses are in the Chinese source section. GUT docs and selected functions, two abagames Skill entries and the observation reference were read; their engine, test runner and mutation fixtures were not executed. This is original synthesis, not copied upstream code. Report document review, scenario walkthrough, package checks, host loading and game execution separately.
