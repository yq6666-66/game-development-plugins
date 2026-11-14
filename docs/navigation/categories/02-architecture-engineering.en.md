# Architecture & engineering

[中文](02-architecture-engineering.md) · [All categories](../README.en.md)

## When to use

Responsibilities, state ownership, dependencies or project entry points are unclear; this is not an instruction to rewrite the project.

## Inputs and output

- Inputs: Startup entry, locked versions, modules/state, dependencies and protected invariants.
- Output: Ownership/dependency map, one change boundary, startup instructions and rollback point.

## Starting routes

- **New project:** Choose the smallest structure that serves the target platform and document interfaces; justify added complexity.
- **Existing project:** Read actual files and reproduce the existing entry; find state writers and lifecycle ownership without replacing the framework.

## Available entry

[game-playloop-validation](../../../skills/game-playloop-validation/SKILL.md). Read the actual entry and only its needed local references.

Existing methods support diagnosis; there is no dedicated scaffolding/architecture implementation Skill.

## Smallest check

Trace one input-to-state-to-UI path and ownership after exit/restart; a static dependency map is not runtime proof.

## Tools and next handoff

Choose by project needs through [resource selection](../../../skills/game-resource-selection/SKILL.md) and the [review card](../../resources/README.en.md). Categories are not engine/framework allowlists or product endorsements. Do not add an inapplicable system.

Record the goal, baseline, changed scope, evidence and open items for the next category. This page is navigation, not another installable Skill; installable Skills remain self-contained.
