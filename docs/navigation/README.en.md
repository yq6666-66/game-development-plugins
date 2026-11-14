# Category navigation

[中文](README.md) · [Home](../../README.en.md)

## Starting from scratch

1. Identify players, platforms, inputs, the session goal and minimum success criteria. Mark undecided rules as reversible hypotheses.
2. Scope a prototype with the [project contract](../examples/project-contract.md), then choose technology appropriate to it.
3. Verify one input → state → feedback loop using [game-playloop-validation](../../skills/game-playloop-validation/SKILL.md) when useful.
4. For a defined visual goal, use [game-visual-iteration](../../skills/game-visual-iteration/SKILL.md) on a small sample. Art acceptance is not gameplay acceptance.

[game-prototype-planning](../../skills/game-prototype-planning/SKILL.md) now supports idea, rule and minimal prototype planning. It does not generate a project or a complete game design document. This route is not a tested game template.

## Taking over a project

1. Read actual files, versions, startup instructions, contracts and existing evidence; establish authorized access and a recoverable baseline.
2. Reproduce one problem. Separate author statements, source-level inference and runtime observation.
3. Select by problem and preserve established rules, layout, assets and input. Do not replace the framework by default.
4. Change within scope, then regress the normal path and a relevant interruption; report untested areas.

## Eight categories

Existing coverage means related methods, not complete implementation of a category.

| Category | Trigger | Available coverage / future candidate |
| --- | --- | --- |
| Game design & prototyping | What is a session and how can hypotheses be compared? | [game-prototype-planning](../../skills/game-prototype-planning/SKILL.md) available; complete game design documents are outside its scope |
| Architecture & engineering | Who owns state and how do modules interact? | Playloop lifecycle/state diagnosis; project scaffolding Skill is future work |
| Visuals & art | Materials, lighting, assets or readability need improvement | [game-visual-iteration](../../skills/game-visual-iteration/SKILL.md) available |
| Gameplay & systems | Input, restart, persistence or feedback is wrong | [game-playloop-validation](../../skills/game-playloop-validation/SKILL.md) available |
| UI & experience | HUD sync, menu focus or device input is wrong | UI checks within playloop validation; separate UI design Skill is future work |
| Testing & performance | Is evidence sufficient and what is the runtime cost? | Both Skills include evidence/performance checks, not certification or a full test platform |
| Build & collaboration | How should work be built, handed over or rolled back? | [Project contract](../examples/project-contract.md) and package checks; dedicated build Skill is future work |
| Tools & resources | Which engine, app, tool or free resource fits? | [game-resource-selection](../../skills/game-resource-selection/SKILL.md) and [template](../resources/README.en.md) available; specific product directory awaits verification |

Categories do not move folders. Existing paths remain stable and independently copyable; overlapping topics use navigation links. Add a Skill only for a distinct trigger, inputs, outputs and complete workflow, not for each source.

[Distillation tutorial](../distillation/README.en.md) · [Future showcase submissions](../showcase/README.en.md). Game uploads are not required in this increment.
