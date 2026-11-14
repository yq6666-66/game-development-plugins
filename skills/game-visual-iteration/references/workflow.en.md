# Game visual iteration workflow

[中文入口](../SKILL.md). Improve what players can perceive, not resemblance to a reference alone. Apply to an existing 2D/3D game or an explicitly authorized new prototype; do not generate a whole game or read every reference by default.

## Establish the question and baseline

Distinguish planning, diagnosis and implementation. A plan or diagnosis alone does not authorize writing copies, modifying files or running the engine. For an existing project inspect the actual entry point, version, scene, assets and effective rendering configuration. Separate observations, provider claims and hypotheses. Preserve agreed layout, style, controls, budget and scope; conflicting baselines or required missing inputs are blockers. An authorized new prototype may use explicit, reversible sample assumptions rather than requiring a nonexistent old project. Never present assumptions as prior decisions.

State what players need to see more clearly, at what distance or size and in which state. Identify what to borrow and reject from references, plus protected properties. The project's agreement sets stop conditions and retry costs, not an upstream example.

## Isolate the responsible layer

| Symptom | Investigate first | Avoid |
| --- | --- | --- |
| Wrong silhouette, space or orientation | Loaded version, geometry, camera, scale and orientation | Moving the level or lighting away a geometry error |
| Assets look unrelated | Shape language, palette and material roles | Replacing the established art direction |
| Flat highlights or unreadable shadow | Light direction, fill, exposure and reflection | Adding glow or lighting every surface equally |
| Unconvincing surface | Texture bindings, channels, color space and localized wear | Uniform noise or treating every depression as water |
| Weak close/distant recognition | Silhouette, structure and edges at actual viewing distance | Microdetail or many separate objects first |
| Effects obscure play or slow it down | Occlusion, effective configuration and measured bottleneck | Enabling everything and judging from one still |

Use representative samples appropriate to the question. Material, model, HUD and audio experiments may be separate; a complete test scene is not mandatory. The near-view priority might be a landing target, unit silhouette or interactive prop, not necessarily a weapon.

## Compare one interpretable change

Keep a recoverable baseline, normal input route and observation points. Hold relevant nonexperimental conditions constant: camera, resolution, quality and exposure, except when one is the selected variable. Compare benefit and cost; do not improve the apparent result by choosing a flattering viewpoint, lowering unrelated quality or hiding failures.

Use normal controls beyond still-image comparison to inspect dynamic occlusion, information and control regressions. Play animations continuously and inspect reflections from different angles. Image metrics are supporting evidence. Expand only after the sample supports the hypothesis and the task permits it; otherwise retain the counterevidence and revise the diagnosis, not indefinitely tweak.

## Read details only when needed

- Import, batching, animation, materials or performance: [asset-to-runtime gates](asset-runtime-gates.md), matching source, export, import and runtime contracts rather than requiring every stage every time.
- Mesh statistics, LOD transitions or animation seams: [English focused checks](mesh-lod-animation-checks.en.md).
- Provenance, permissions and method selection: [source notes](sources.md) and [workflow sources](workflow-sources.md). These detailed historical references remain partly Chinese. Links do not authorize running upstream tools.
- For an engine implementation, check official documentation for the project's actual version. Transfer lighting relationships, purpose and acceptance criteria, not raw numbers, texture channels, coordinate transforms or post-processing settings.

## Report only the evidence obtained

Deliver baseline, changes and recovery path, real entry/input steps, equal-condition comparisons, actual checks completed versus planned, performance measurement conditions and uncovered risks. Mark specific checks PASS, FAIL, BLOCKED or unverified, not the whole game green.

Offline renders, debug cameras, scripted position changes and controlled recordings do not replace player input; video FPS is not runtime performance. Distinguish simulated devices, Editor, shipped build and target hardware. Reassess old evidence when relevant versions change. Current authority does not automatically cover engine migration, paid generation, publication or installation.
