# Testing & performance

[中文](06-testing-performance.md) · [All categories](../README.en.md)

## When to use

Evidence gaps, regressions, stalls or resource growth; first state the claim to test.

## Inputs and output

- Inputs: Version, environment, reproduction path, intended metrics and counterexamples; mark unknown budgets.
- Output: Test matrix, results/failure evidence, measurement scope and unverified items.

## Starting routes

- **New project:** Define observable assertions and one failure case for the smallest loop before building a test platform.
- **Existing project:** Reproduce and baseline first; select relevant paths/interruptions and do not transfer old passes to a new version.

## Available entry

[game-playloop-validation](../../../skills/game-playloop-validation/SKILL.md). Read the actual entry and only its needed local references.

No full testing framework, cross-device automation or profiler is provided; route visual cases to the visual Skill.

## Smallest check

Separate package checks, walkthroughs, host loading, engine runs and target-device testing; control performance comparisons and distinguish CPU/GPU/end-to-end evidence.

## Tools and next handoff

Choose by project needs through [resource selection](../../../skills/game-resource-selection/SKILL.md) and the [review card](../../resources/README.en.md). Categories are not engine/framework allowlists or product endorsements. Do not add an inapplicable system.

Record the goal, baseline, changed scope, evidence and open items for the next category. This page is navigation, not another installable Skill; installable Skills remain self-contained.
