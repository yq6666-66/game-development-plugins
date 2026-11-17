# Action prompts are more than device artwork

[中文](action-glyph-contract.md). Use for an existing prompt task; no mandatory Steam integration, input migration or asset download.

Trace player/controller → current action context → effective binding origins → text/glyph → observed action. Device type can select an art style but cannot establish an action binding. An emulated logical controller may differ from the device in the player's hands.

Define behavior for zero, multiple or unknown origins and image-load failure. Do not blindly take the first array entry or index a custom atlas with an unchecked enum. Use the project's intended primary/multiple-prompt or understandable text fallback rather than guessing a familiar button.

In an authorized sample, exercise the normal action, context/rebinding refresh and supported device changes. An isolated fixture can supply zero origins and an origin outside the custom atlas range to check safe, non-misleading fallback. Fixture success does not prove physical input, real mapping or image decoding. Record action results and visible prompts, not screenshots alone.

[Sources and exact reading scope](action-glyph-contract.md): Valve's online Gamepad Emulation best practices (device-specific artwork and own-art examples) and ISteamInput reference sections for digital origins, legacy/PNG/SVG glyph access and device type, read 2026-11-17. The API describes context-specific origins and a count, with origin values potentially beyond SDK-era enums. The older guide uses a glyph function now marked Legacy; inspect the project's pinned SDK before choosing an API. No SDK source, Steam invocation, image inspection or hardware testing occurred. Emulation and native Steam Input routes are distinct. Our origin-chain and edge-case checks are synthesis, not reproduced upstream bugs. Links/paraphrase only; Valve assets and code are not relicensed by this package. Integration and device matrices have costs; skip when outside scope.
