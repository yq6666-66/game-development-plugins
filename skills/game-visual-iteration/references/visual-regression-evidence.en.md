# Automated screenshots: determinism is not full acceptance

[中文](visual-regression-evidence.md)

Use for authorized screenshot baselines or intermittent pixel differences. Do not require Three.js/Puppeteer or copy browser security flags.

Keep two evidence tracks separate:

1. Pixel comparison records build, renderer, device, viewport/DPR, camera, seed and animation state. Define asset/shader/video-frame readiness and timeout outcomes. Verify worker coverage; page injection does not necessarily reach workers. Network idle or a fixed delay alone does not establish readiness.
2. Real interaction removes screenshot-only input blocking, frozen clocks and hidden UI. Use normal inputs to check HUD, occlusion, menus, focus and pause/resume. A pixel pass does not replace this track.

Declare masks and exclusions beforehand. Do not pass excluded content. Every planned case needs a terminal result and reason: report planned, executed, actually compared, passed, failed, skipped and blocked counts. Missing references, device loss, black frames, resource errors, timeouts and browser restarts must not silently become passes. Preserve retry outcomes; budgets are project-specific.

Review whether a difference is an intended art change, environment change or regression before replacing references. Raising tolerance, excluding unexplained failures or regenerating baselines is not proof of repair. Calibrate thresholds from measured variation and important regions, not upstream constants; cross-GPU/backend comparisons need justified baselines/tolerances.

Suggested, unexecuted checks: repeat a stable capture; deliberately change a visible material and require a real diff/failure; introduce a missing reference/resource failure and require a non-pass with complete accounting; remove capture fixtures and run normal menu/movement/pause inputs separately.

## Evidence and sources

Static reading on 2026-11-15; no upstream execution or rendered screenshot inspection. mrdoob/three.js and contributors, commit `b529cbbda2ba956a8444545a5634f6db22b68385`, 2026-11-14T16:26:36Z, package 0.187.0:

- [README](https://github.com/mrdoob/three.js/blob/b529cbbda2ba956a8444545a5634f6db22b68385/test/e2e/README.md), [runner](https://github.com/mrdoob/three.js/blob/b529cbbda2ba956a8444545a5634f6db22b68385/test/e2e/puppeteer.js), [deterministic injection](https://github.com/mrdoob/three.js/blob/b529cbbda2ba956a8444545a5634f6db22b68385/test/e2e/deterministic-injection.js), [cleanup](https://github.com/mrdoob/three.js/blob/b529cbbda2ba956a8444545a5634f6db22b68385/test/e2e/clean-page.js) and [package](https://github.com/mrdoob/three.js/blob/b529cbbda2ba956a8444545a5634f6db22b68385/package.json), full files.
- [Issue #33559](https://github.com/mrdoob/three.js/issues/33559), gkjohnson, 2026-05-11 original report. The inspected device-loss branch restarts the browser without adding that case to the failure collection. This supports a static missing-result risk, not an independently reproduced runtime defect.

Frozen time can hide animation/audio problems. Transfer contracts, not engine APIs or upstream driver paths. Original synthesis and links only; MIT metadata does not automatically cover assets/dependencies.
