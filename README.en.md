# Game Development Plugins · 游戏开发插件

[中文（默认）](README.md) · English

A continually distilled **AI Agent Skills bundle** for game-development learners, independent developers and teams. Turn problems into scoped, actionable and verifiable tasks for both **new projects** and **existing-project takeovers**.

This is not a Unity/Unreal runtime plugin, game engine or guaranteed whole-game generator. Methods are not tied to an engine, framework, language or genre; Three.js is only one possible implementation choice. Verify APIs, dependencies and performance in the actual project version and target device.

## Dual-host plugin candidate

The existing individual-Skill copy workflow remains available. Codex and Claude Code manifests now share the same `skills/` directory. **0.1.0 is an initial release with limited validation**, not a claim of complete dual-host acceptance or an official-directory listing.

See the [installation guide](PLUGIN-README.en.md), [approved implementation scope](docs/plans/dual-host-plugin/README.md), and [validation record](docs/validation/dual-host-plugin-2026-11-15.md). No MCP server, hooks, background tasks or automatic game-project modification scripts are included.


## Start here

| Situation | Entry |
| --- | --- |
| Starting from scratch | [Define the smallest playable hypothesis](docs/navigation/README.en.md#starting-from-scratch) |
| Taking over a project | [Inspect real files and establish a baseline](docs/navigation/README.en.md#taking-over-a-project) |
| Solving a known problem | [Eight-category navigation](docs/navigation/README.en.md#eight-categories) |
| Learning or distilling further | [Distillation tutorial and open template](docs/distillation/README.en.md) |

## Available now

| Skill | Scope | Not its job |
| --- | --- | --- |
| [game-engineering](skills/game-engineering/SKILL.md) | Bounded project setup, ownership and dependency changes | No automatic rewrite or engine migration |
| [game-ui-design](skills/game-ui-design/SKILL.md) | Screen information, transitions, layout and focus design | Not a screenshot-only usability claim |
| [game-build-delivery](skills/game-build-delivery/SKILL.md) | Build/export diagnosis and traceable local delivery | No automatic signing, release or deployment; builds are not playtests |
| [game-resource-selection](skills/game-resource-selection/SKILL.md) | Contextual engine/tool/resource selection with current cost, platform and license checks | Automatic installs/purchases or treating free as redistribution permission |
| [game-prototype-planning](skills/game-prototype-planning/SKILL.md) | Ideas, rules and minimal prototype plans with observable signals and counterevidence | Whole-game generation or substituting plans for playtests |
| [game-visual-iteration](skills/game-visual-iteration/SKILL.md) | Reference analysis, lighting/material diagnosis, asset integration and controlled visual iteration | Replacing art direction or the toolchain |
| [game-playloop-validation](skills/game-playloop-validation/SKILL.md) | Input, rules, state, lifecycle, restart, persistence, HUD and feedback | Inventing existing rules or authorizing deployment |

The planning, visual and playloop Skills support an existing game or an explicitly authorized new prototype. For a new project, define a minimal task and reversible assumptions instead of requiring a nonexistent legacy codebase.

**All eight bilingual category guides are complete, but this does not mean eight implemented Skills.** The seven above are currently installable. Additional focused Skills, a full tools/free-resources directory, a game showcase and fully bilingual references remain future work. The [navigation](docs/navigation/README.en.md) labels availability. No game made with this bundle has yet been uploaded or verified here.

## Minimal use

1. State goals, target devices, inputs, allowed changes and required evidence. Reuse the [project contract](docs/examples/project-contract.md).
2. Read the chosen `SKILL.md`, relevant references and [compatibility limits](docs/COMPATIBILITY.md).
3. Copy the **entire selected Skill folder** from `skills/` into the location documented by your host. Do not install research notes or assume one path fits every Codex deployment.
4. Verify actual host discovery. A valid folder alone does not prove loading. Hosts without Skills support can read the instructions as task context.
5. Work on one verifiable goal and report actual steps, results and unknowns. Planning does not authorize modification, installation or publishing.

Example tasks:
- New prototype: “Use game-playloop-validation to propose minimal input, ending and restart assumptions within the approved scope; identify decisions requiring my input and verify one complete loop.”
- Takeover: “Use game-visual-iteration to inspect why one prop differs from the scene. Preserve style and layout; propose a minimal controlled comparison.”
- Debugging: “Events fire twice after restart. Trace lifecycle and state ownership instead of replacing the framework.”

## Continuous distillation and shared learning

Our maintenance cadence is **daily research distillation and weekly integration updates**. Sources include open projects, tutorials, official documentation, discussions and retrospectives. We restate conditions, steps, tradeoffs and verification methods in our own words; popularity is not evidence.

Daily research goes to research branches; weekly integration goes to reviewable branches. **Weekly updates do not promise automatic main-branch merges or releases.** Quality takes priority over counts; shortages, blockers and unverified claims remain visible. The cadence is a maintenance commitment, not proof that a scheduled run succeeded: consult actual records and commits.

You are welcome to reuse, modify and share the original MIT templates to continue your own distillation, and contribute methods or counterexamples. The [tutorial and template](docs/distillation/README.en.md) explain how to turn sources into reusable guidance. Third-party code, articles, models and assets retain their own licenses.

## Checks and evidence

Run from the repository root with Python 3.9+; no third-party Python packages required:

```sh
python3 scripts/validate_package.py
python3 -m unittest discover -s tests -v
```

These checks cover packaging and validator behavior, not host discovery, engine execution, device input or visual quality. See [historical validation](docs/VALIDATION.md), [navigation checks](docs/validation/navigation-foundation-2026-11-14.md), [prototype-planning checks](docs/validation/prototype-planning-2026-11-14.md) and [resource-selection checks](docs/validation/resource-selection-2026-11-14.md). The homepage, navigation and introductory tutorial are paired in Chinese and English. The new planning and resource-selection Skills include a complete English workflow inside its folder. Visual iteration and playloop validation now also provide complete English core workflows inside their folders. Some detailed and historical references remain in their original language; complete file-by-file bilingual parity is not claimed.

[Navigation](docs/navigation/README.en.md) · [Tutorial](docs/distillation/README.en.md) · [Compatibility](docs/COMPATIBILITY.md) · [Provenance](docs/PROVENANCE.md) · [Source audit](docs/audits/2026-11-13/README.md) · [Changelog](CHANGELOG.md) · [MIT](LICENSE)

Reading this bundle does not authorize spending, uploads, game modifications, merges or deployments. A source-path count is not a count of runtime-tested Skills.

[Fourth-pass scope and changes](docs/audits/2026-11-14-fourth/README.md) · [Validation](docs/validation/fourth-pass-2026-11-14.md)

## Public-source distillation · 2026-11-14

The [daily research](docs/research/daily/2026-11-14.md) adds bilingual references for recovery relationships and essential audio information to the playloop Skill. [Validation scope](docs/validation/market-2026-11-14.md) distinguishes package checks from game execution. This integration preserves the independent daily branch's sources and historical evidence limits.

[Additional GitHub research](docs/research/daily/2026-11-14-github-continuation.md) adds scoped async-result, fixture-cleanup, state-divergence and detection-power checks without adding another Skill.

Two new standalone engineering/UI Skills include complete English workflows and local source records. [Construction and validation](docs/validation/engineering-ui-2026-11-14.md).

## Daily research · 2026-11-15

[Three topics](docs/research/daily/2026-11-15.md): screenshot readiness/result completeness, UI event versus held-input isolation, and cloud-save conflict evidence. Portable bilingual references extend the two existing tracks; seven Skills remain. [Validation scope](docs/validation/daily-2026-11-15.md) excludes engine/game execution.

## Weekly integration · 2026-W47

[Weekly report](docs/research/weekly/2026-W47.md): three additions cover packaged resources, loading readiness and composited HUD readability. Seven skills remain. [Validation](docs/validation/weekly-2026-W47.md) does not include engine runs.
