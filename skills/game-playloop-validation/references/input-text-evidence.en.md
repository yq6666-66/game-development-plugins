# Action semantics, text systems and intermediate evidence

[中文](input-text-evidence.md). Read only for multiple bindings, rebinding, supported text/localization, or multi-step diagnostics. Do not add those systems merely to satisfy this checklist. This is source-based guidance, not a tested runtime implementation.

## Action contract

Define held/pressed/released, axis thresholds and binding aggregation. If two keys map to one action, does pressing the second while holding the first create a second event? Follow the game's intended semantics, not a universal rule.

Exclude the input that opened rebinding; handle cancel, conflict and restore. Resample held state after changes without inventing pressed events. Switch device prompts on meaningful input rather than drift or incidental motion. Clearing transient input must not erase intentional inventory selection. Device disconnect, pause and buffer clocks depend on the actual network/timing contract.

Check overlapping bindings, rebinding cancellation/conflict/restore and device changes. Record action counts, binding values and prompts, not screenshots alone. Test only supported devices.

## Align intermediate state and presentation

Check each step of a chain: input, committed state, display and next action. Reaching an exit does not prove that collecting its key awarded inventory only once. Existing or authorized diagnostics should read real state, not a duplicate simulation or expected answers.

Associate build, scene and tick/frame labels with matching state and images. Mark an undrawn tick as missing imagery; do not relabel a later image. Controlled advancement needs one simulation owner, not simultaneous test and normal-loop updates. Action dispatch tests do not establish device-to-action behavior. Keep diagnostics free of secrets, hidden player data and unauthorized personal information.

Counterexample: state is correct but HUD is one frame late. Preserve the same-tick mismatch instead of hiding it behind a final screenshot. A debug interface is not mandatory for every task.

## Validate supported writing systems

Use actual fonts, translations and narrow bounds to check missing glyphs, mixed scripts, unbroken strings, grapheme clusters and relevant shaping. Space-based wrapping and code-point typewriter reveals are not universal. Reveal by grapheme while keeping precomputed lines stable; verify shaping and metrics in the actual text library.

Use full sentences and placeholders that accommodate word order; specify missing-translation fallback without assuming English is the source language. For text input, test IME composition, commit and cancellation separately from key events. Check numeric width transitions such as 9→10 and 99→100 with actual locale formatting. A fixed expansion percentage does not establish success.

## Sources and scope

The [Chinese companion](input-text-evidence.md#固定来源与边界) contains the exact fixed source links and reading scope: five gamedev-skills references at c6ca6c41c839b68319ffc08430b99ab768debc32 were fully read this round. No upstream API code is copied. Ebitengine examples are not cross-engine APIs. Neither upstream nor target runtime was executed; this is a historical snapshot, not a latest-version claim.
