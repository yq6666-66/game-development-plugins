# Build & collaboration

[中文](07-build-collaboration.md) · [All categories](../README.en.md)

## When to use

Builds are unreproducible, handoffs are unclear, or release/rollback preparation is needed; preparation is not release permission.

## Inputs and output

- Inputs: Target platform, versions/dependencies, build entry, artifact contract, permissions and branch policy.
- Output: Build instructions, artifact identity, validation logs, handoff checklist and rollback method.

## Starting routes

- **New project:** Establish one target platform and a reproducible local build path; do not register services or deploy by default.
- **Existing project:** Read existing build/CI and branch records; check effective versions and cache boundaries before changing configuration.

## Available entry

[Project contract](../../examples/project-contract.md). Read the actual entry and only its needed local references.

This is a navigation checklist, not an installable build Skill; publishing, deployment, signing and spending require task-specific authorization.

## Smallest check

Build in an authorized environment, inspect logs/artifacts, then separately test startup and relevant actions; an exit code does not prove playability. Mark unexecuted steps.

## Tools and next handoff

Choose by project needs through [resource selection](../../../skills/game-resource-selection/SKILL.md) and the [review card](../../resources/README.en.md). Categories are not engine/framework allowlists or product endorsements. Do not add an inapplicable system.

Record the goal, baseline, changed scope, evidence and open items for the next category. This page is navigation, not another installable Skill; installable Skills remain self-contained.
