# UI & experience

[中文](05-ui-experience.md) · [All categories](../README.en.md)

## When to use

Players cannot understand state, HUD is stale, or focus, text input and multi-device layout fail.

## Inputs and output

- Inputs: UI state list, input devices, languages/sizes, information priorities and accessibility goals.
- Output: State/focus transition table, key-screen evidence and operable paths.

## Starting routes

- **New project:** List essential information and actions first, then design one screen including error/exit states.
- **Existing project:** Check actual state sources and input ownership; separate display, state and reachability defects.

## Available entry

[game-ui-design](../../../skills/game-ui-design/SKILL.md). Read the actual entry and only its needed local references.

The UI design Skill provides information, transition, layout and focus guidance; it is not a complete design system or accessibility certification.

## Smallest check

Enter, operate and leave with supported inputs; check back/cancel/restart, text input and essential audio alternatives. Simulated sizes do not prove device usability.

## Tools and next handoff

Choose by project needs through [resource selection](../../../skills/game-resource-selection/SKILL.md) and the [review card](../../resources/README.en.md). Categories are not engine/framework allowlists or product endorsements. Do not add an inapplicable system.

Record the goal, baseline, changed scope, evidence and open items for the next category. This page is navigation, not another installable Skill; installable Skills remain self-contained.

The standalone `game-ui-design` now covers this design/implementation workflow, but no runtime adapter or certification is claimed.
