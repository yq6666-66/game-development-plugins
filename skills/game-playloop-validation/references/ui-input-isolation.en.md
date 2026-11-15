# UI input isolation: events, held state and focus

[中文](ui-input-isolation.md)

Use when menus leak movement/confirmation, hiding controls changes release delivery, or pause breaks UI. Read the project's modal/non-modal contract first. Do not freeze every conversation.

Separate four boundaries: event propagation/consumption; continuous input polling and ownership; initial/fallback/return focus; and pause processing versus signals. Consuming an event need not clear global held state. Gate actions through the authorized context, preserving allowed non-modal movement and avoiding competing input systems.

Suggested checks, not executed:

- Hold movement, open a modal menu, release, close: enforce its policy and prevent stale movement.
- Enter text/confirm: no forbidden gameplay action; non-modal walk-and-talk still works if intended.
- Press a control, hide it, release: record both recipients and business-action counts.
- Use a supported keyboard/controller, remove the focused element, cancel: verify fallback and returned focus.
- Pause, trigger a UI signal, resume: UI and game side effects follow the project's pause contract.

## Sources and scope

Read on 2026-11-15, Godot official 4.5 documentation: [Input](https://docs.godotengine.org/en/4.5/classes/class_input.html), [InputEvent](https://docs.godotengine.org/en/4.5/tutorials/inputs/inputevent.html), [GUI navigation](https://docs.godotengine.org/en/4.5/tutorials/ui/gui_navigation.html), [Pausing](https://docs.godotengine.org/en/4.5/tutorials/scripting/pausing_games.html). Global Input state, event ordering, focus and pause/signal sections inspected; publication dates unconfirmed.

[Input implementation](https://github.com/godotengine/godot/blob/876b290332ec6f2e6d173d08162a02aa7e6ca46d/core/input/input.cpp), 4.5-stable commit, localized state review only. [Issue #112198](https://github.com/godotengine/godot/issues/112198) is an author's 4.5.1 hide-before-release report, not independently reproduced or generalized to every version.

No engine, game or device execution. These scenarios are not passes. Transfer the event/state/focus/pause distinction, not Godot APIs or ordering, and verify the project's locked version. Original synthesis and links only.
