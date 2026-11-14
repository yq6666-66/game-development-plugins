# Mesh counts, LOD transitions and animation seams

[中文](mesh-lod-animation-checks.md). Use only for relevant optimization, LOD or loop-export questions; do not add 3D, LOD or animation systems to unrelated projects.

## Identify the counted representation

Separate source mesh, modifier-evaluated mesh, exported mesh and available runtime statistics, including the measuring tool's definition. UV, normal and color discontinuities may split export/GPU vertices. Fewer source vertices do not establish lower runtime cost. Do not blindly delete UVs, hard edges or vertex colors that support shading, masks or animation.

Use a representative asset, before/after exports and its actual scene. Compare exported vertices/triangles and target runtime measurements under the same visual requirements. Missing runtime data stays unmeasured; lower counts alone do not prove a speedup.

## Test LOD transitions, not just levels

For each level inspect silhouette, UVs, material mapping, shader-required attributes, pivots and bounds. For skinned assets check representative motion and simplified-skeleton deformation. From the actual player view, cross the project's transition conditions and return, observing flashes, missing masks, material changes and pose defects.

Correct stills of every level do not establish correct transitions. Associate images with levels/conditions; do not inherit fixed screen percentages, polygon budgets or compression gains. Round-trip threshold testing is this package's synthesized suggestion, not an executed result.

## Separate pose and velocity at loop seams

Play continuously across seams and inspect both pose continuity and abrupt displacement/rotation velocity changes. Root motion should satisfy its accumulated-displacement contract, not a forced return to the first world-space position. Check duplicated endpoint frames, sampling rate, clip range and the target player's loop behavior for unintended pauses.

Constraints, drivers and preview cycle modifiers do not automatically become exported animation. Check sampling/baking and whether target constraints apply the motion again. Inspect root movement, contacts and seams in the target environment, not only first/last stills. Sampling rates, bone scaling and action organization depend on the project toolchain.

## Sources and limits

[Fixed sources](mesh-lod-animation-checks.md#来源与证据): EL4CTEO game-optimization and animation at 3e481ad1…; arjun988 lod-pipeline at 904f095d…. Fixed text was reread, not the latest upstream audit. No Blender, export scripts or target game were executed. Author-reported tests are not this package's PASS. This is original paraphrase with no upstream code/assets.
