# Gameplay & systems

[中文](04-gameplay-systems.md) · [All categories](../README.en.md)

## When to use

Input, rules, state, restart, saves or feedback differ from expectations.

## Inputs and output

- Inputs: Rules, state owners, input path, expected normal/failure results and reproduction conditions.
- Output: Repeatable steps, before/after state, counterexamples and regression results.

## Starting routes

- **New project:** Validate a minimal loop against authorized rules; label assumptions or ask the decision-maker about unknown rules.
- **Existing project:** Diagnose the existing system while preserving working rules; do not add mechanics under the guise of repair.

## Available entry

[game-playloop-validation](../../../skills/game-playloop-validation/SKILL.md). Read the actual entry and only its needed local references.

Dedicated AI, networking, economy and procedural-generation implementations are not provided.

## Smallest check

Walk a relevant loop with normal input, then repeat or interrupt it; test saves only when in scope, not because this category lists them.

## Tools and next handoff

Choose by project needs through [resource selection](../../../skills/game-resource-selection/SKILL.md) and the [review card](../../resources/README.en.md). Categories are not engine/framework allowlists or product endorsements. Do not add an inapplicable system.

Record the goal, baseline, changed scope, evidence and open items for the next category. This page is navigation, not another installable Skill; installable Skills remain self-contained.
