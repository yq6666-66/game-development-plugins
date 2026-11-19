# Evidence for first-draw stalls

[中文](pipeline-readiness.md). Use for authorized visual-performance diagnosis, not implicit engine upgrades, renderer switches or a new warmup system.

Godot contributors' [Reducing stutter from shader (pipeline) compilations](https://github.com/godotengine/godot-docs/blob/2a604b9307fca7b926431313f1b39718463fb2e7/tutorials/performance/pipeline_compilations.rst), commit 2a604b9307fca7b926431313f1b39718463fb2e7 dated 2026-10-19, read 2026-11-19. Complete prose, captions and alternative text read; no image-pixel inspection or engine run. This development snapshot is not a compatibility promise for the target release.

The source distinguishes intermediate shader code from hardware/driver-dependent pipelines. Export baking is not pipeline precompilation. The described precompilation applies to Forward+/Mobile, not Compatibility/Web. Preloaded resources may miss combinations determined at instancing. Monitors count cumulative creations, not live pipelines or frame time.

Our diagnostic procedure:
1. Fix version, backend, hardware/driver, effect path and quality; label cache state known-cold, known-warm or unknown. Do not delete global driver caches implicitly.
2. Trigger first and repeated appearances through normal input. Correlate events, frame times and stage-counter deltas. Rising counts are clues, not causal proof; no delta does not exclude uploads, scripts or other bottlenecks.
3. Compare a minimal preparation change only for an identified gap. Hidden instances must not trigger scripts, audio, collisions, rewards or subscriptions. Executing gameplay early is not a harmless warmup shortcut.
4. Record preparation time/memory and first-use peaks. Average FPS or a smooth second developer run is insufficient. Recheck relevant combinations after quality changes; do not precompile every theoretical combination.

Proposed checks, not executed: compare a preloaded but unattached effect, an instantiated effect and one supported quality transition; inspect first-frame peaks against the project's budget and input correctness. Make added preparation time/memory explicit. Compatibility/Web needs actual backend evidence, not an ineffective baking toggle. Without cold-start or target-device data, leave first-play coverage unverified.

Costs include controlled sampling, prepared resources and device coverage. Benefit requires fault detection and before/after evidence. No code/images copied. [Source license](https://github.com/godotengine/godot-docs/blob/2a604b9307fca7b926431313f1b39718463fb2e7/LICENSE.txt): CC BY 3.0, not replaced by this package's MIT license.
