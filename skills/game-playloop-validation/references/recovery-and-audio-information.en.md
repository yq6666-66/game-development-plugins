# Recovery relationships and audio information

[中文与来源](recovery-and-audio-information.md). Read only for an in-scope persistence or accessibility task; do not add systems. Pair with [state gates](state-and-test-gates.md).

## Evidence

The 2026-11-14 reading covered Godot 4.4's saving tutorial, including its nested-object caveat, and Microsoft's XAG 104 guidance on speech and important non-speech information. Neither examples nor linked videos were run or visually reviewed. The following is our synthesis, not a certification or tested engine adapter.

## Relationship recovery

Inputs: copied saves, version and identity contract. Output: before/after identity, relationship and interaction evidence.

- Separate stable identity from display names, creation order and temporary paths.
- Inspect validation, instance creation, reference resolution, state application and resuming simulation in the existing architecture. Cyclic references may require staged resolution, not a universal parent-first algorithm.
- Use an isolated nested/reference sample. Change creation order, load through the normal path, and compare identity, relationships, counts and one interaction. Serialized fields alone are insufficient.
- Add a missing-reference or duplicate-identity case. Observe explicit failure and the agreed retention/recovery behavior; never overwrite the only save. Simple scalar prototypes need not acquire an object-graph framework.

## Information coverage

Inputs: existing audio events and UI. Output: event → decision information → alternative channel → observation.

- Select a real play path. Distinguish dialogue, consequential sounds and decoration. Do not reveal hidden information beyond what the player could already perceive.
- Mute audio and use normal controls. Reuse clear existing visual signals rather than captioning every sound.
- Check supported layouts/languages, overlap, pause/resume and stale cues after restart. A settings preview does not prove in-play usability; establish timing and directional precision for the project.
- Counterexample: dialogue subtitles are enabled but a necessary non-speech cue is absent. This is not a pass. A small sample is not comprehensive accessibility certification.

Report document review, walkthrough, host loading, game execution and user testing separately. Missing systems are out of scope; inaccessible execution is unverified, not passed. No upstream code or assets are included.
