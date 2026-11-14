# Game Development Plugins · 游戏开发插件

A small, evidence-first **AI agent skill bundle** for improving existing games. This is not a Unity package, Unreal plugin, executable game engine, or automatic game generator. It does not install tools, call paid services, or deploy projects.

**Third-distillation candidate.** The reusable package is in `skills/` and the original package is provided under the [MIT License](LICENSE). This branch is a review candidate, not an engine/runtime release.

## Choose the problem, not the engine hype

| Skill | Use it for | Not its job |
| --- | --- | --- |
| [game-visual-iteration](skills/game-visual-iteration/SKILL.md) | Reference-to-task conversion, lighting/material diagnosis, asset integration and measured visual polish | Replacing an art direction or importing a whole third-party toolchain |
| [game-playloop-validation](skills/game-playloop-validation/SKILL.md) | Input, state, UI, restart, persistence and feedback defects | Inventing missing rules or approving deployment |

The core reasoning is engine-neutral. Unity and browser checklists are supplied as concrete examples, not verified adapters. Other engines require mapping lifecycle, input, asset and measurement concepts to the actual version. No engine/runtime compatibility certification is claimed. Skill instructions are primarily Chinese; identifiers and entry descriptions are English.

## Use and install deliberately

1. Read the selected `SKILL.md`, its linked references, and the [compatibility boundaries](docs/COMPATIBILITY.md).
2. Copy **only the complete selected folder** from `skills/` into the skill-discovery location documented by your agent host. Do not copy historical research or other projects into the installed skill. No network installer is required.
3. Confirm the host discovers the expected `name` and description. The folder format alone does not prove a host loads it. If the host does not support skills, attach/read the selected instructions as task context instead.
4. Give an existing project, a concrete defect or improvement goal, allowed scope, target platform and evidence requirements. Use [the project contract](docs/examples/project-contract.md) if these are not documented already.

For a Codex installation, use the host's installed skill-management/installer facility or its current documented skill-directory workflow. This repository does not claim a fixed path works in every Codex deployment. For other hosts, check their current documentation before installation; no host config is changed automatically.

### Example requests

- “Use game-visual-iteration. Keep this project's art direction and layout. Investigate why one imported prop looks different in the target scene; propose the smallest measurable correction.”
- “Use game-playloop-validation. After restarting this level, events fire twice. Inspect the current lifecycle and prove which path leaks state before changing code.”
- “Review this 2D strategy game's tiny-screen HUD. Prioritize information and actual controls; do not add first-person or combat assumptions.”

## Verify the package

With Python 3.9 or newer, run the local, standard-library-only checks from the repository root:

```text
python3 scripts/validate_package.py
python3 -m unittest discover -s tests -v
```

These check packaging, links and validation behavior. They do not run a game, validate upstream tools, or prove cross-engine correctness. Behavioral task evaluations are documented separately in [validation](docs/VALIDATION.md).

## Provenance and release boundaries

Methods were independently summarized, not copied as an upstream execution framework. [Provenance](docs/PROVENANCE.md) describes inputs and limits; the [second-round audit](docs/audits/2026-11-13/README.md) records file-level reading depth. Tool marketing, stars, a root license or a generated video are not operational evidence.

The portable skills contain no required project coordinates, material-slot counts, target frame rate or fixed retry count. Project-specific historical notes are excluded from this candidate. Preserve the current project's own contract.

No merge, release, personal-skill update or game modification is performed merely by reading this package. The MIT License applies to this package; linked upstream content retains its own terms.

## Research candidate · 2026-11-14

New [daily research](docs/research/daily/2026-11-14.md) adds bilingual on-demand checks for recovery relationships and essential audio information to the existing playloop skill. [Validation scope](docs/validation/market-2026-11-14.md) separates package checks from game execution. This daily branch does not merge the pending bilingual-navigation or fourth-distillation branches.
