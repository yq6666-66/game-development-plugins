# Loaded resources are not playable scenes

[中文](loading-readiness.md). Use only for an authorized loading or scene-transition task; do not add streaming implicitly.

Godot contributors' [Background loading](https://github.com/godotengine/godot-docs/blob/2a604b9307fca7b926431313f1b39718463fb2e7/tutorials/io/background_loading.rst), commit 2a604b9307fca7b926431313f1b39718463fb2e7, read 2026-11-19: complete prose and both language examples, not executed. Request, status and retrieval are separate; early `load_threaded_get()` can block the caller. The example separately instantiates and attaches the scene. These APIs are not engine-neutral.

Our derived contract separates request acceptance, resource readiness, instance creation, scene attachment and playable input. A percentage describes its own stage, not total remaining time or playability. Give failure, cancellation and stale results explicit destinations.

Record the request's scene/generation and consumer. A late result must not return a player to an abandoned scene. Ignoring a result is not cancellation of underlying work or resource release; honor shared ownership. Verify actual engine coalescing/cache behavior for repeated paths before defining commit deduplication; do not assume independent cancellable handles.

Poll without blocking loops. Measure instantiation, attachment and first interaction separately; do not conceal a stall with fake progress. Transfer input only when usable, with understandable retry/back behavior on failure.

Proposed checks, not run here: delay readiness and retain responsiveness; abandon A then choose B and complete A late; fail attachment after successful retrieval and reject false readiness/duplicate instances; compare cached and first-load cases with stage timing, owner and actual input results. Instrumentation and fault isolation have costs. Static review cannot prove thread safety, and this contract never authorizes arbitrary background scene-tree mutation or a fixed timeout/cancel API.

Original synthesis, no copied code. [Source license](https://github.com/godotengine/godot-docs/blob/2a604b9307fca7b926431313f1b39718463fb2e7/LICENSE.txt): CC BY 3.0; this package's MIT license does not replace it.
