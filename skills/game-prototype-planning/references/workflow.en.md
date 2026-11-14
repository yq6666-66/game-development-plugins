# Game idea and minimal prototype planning

This is the complete English workflow. Output is a **testable plan and decision basis**, not an already playable game. No other Skill is required. The shared [planning sheet](planning-sheet.md) and [sources](sources.md) are bilingual.

## 1. Bound the decision

Identify whether the request is exploration, planning, or planning inside authorized implementation. Planning does not itself authorize game edits, engine execution or publication. Preserve specified platform, genre, engine, scale and deadline; do not default to the browser or Three.js.

For a new project, form a small reversible hypothesis from audience, context, desired experience and constraints. Do not demand a nonexistent legacy project. Compare ideas only on differences relevant to the next decision.

For existing projects, inspect actual rules, entry points and evidence. Separate established decisions from allowed experimental variables. Look up missing rules before proposing them; proposals are not historical facts. Ask about material unresolved tradeoffs; label reversible details as suggestions rather than blocking all planning.

## 2. Translate experience into rules and signals

State one decision question, such as whether players can predict the cost of two routes before acting. Trace `rule → player choice/system change → perceivable signal → intended experience`, marking unsupported links and competing explanations.

Define only relevant inputs, options, legality, state changes, feedback and recovery. Add wins, losses, scoring, resources or restart only when appropriate. An open-ended toy can end observation and reset without a win condition. Use project values or explicitly labeled experiment assumptions, not universal time limits, sample sizes or performance targets.

## 3. Choose the smallest sufficient medium

Paper, role-play, interaction sketches, greyboxes, executable prototypes and isolated variants in an existing project are valid options. Explain why the medium answers the question and what it cannot establish. Paper cannot prove runtime timing, physics or device behavior. Do not discard visual, audio or narrative fidelity when that is the mechanism being tested.

Preserve a recoverable baseline. Change only the intended factor between control and variant and state held conditions. Choose disposable versus evolutionary code deliberately; neither single-file implementation nor rewriting is mandatory. Demo code does not automatically become production code. Identify necessary tasks, exclusions, dependencies, blockers and risk-scaled stopping conditions.

## 4. Decide what evidence changes the judgment

Before implementation, record observable signals, counterevidence, alternatives, collection methods and continue/adjust/stop/inconclusive criteria. Separate rule correctness, player understanding and experience. No-error execution is not evidence of fun; replay or session duration alone does not prove the desired experience.

Select a relevant normal path and counterexample. When playtesting is needed, specify participants, devices, inputs and coaching; account for order and familiarity effects. Sample size and thresholds depend on risk and context. Without playtests, deliver a plan, not fabricated feedback or a keep/kill verdict.

## 5. Deliver an actionable handoff

Use the [planning sheet](planning-sheet.md) as needed: decision, facts/assumptions, rules, scope, medium, comparison, signals/counterevidence, decision gate, rollback, unknowns and next owner. Check the actual environment before giving implementation commands; otherwise mark the startup entry unresolved.

If results exist, report observed facts and coverage before continuing, adjusting, stopping or declaring insufficient evidence. Success supports only the tested hypothesis, not the whole product. After implementation, verify state and feedback through actual inputs; this plan is not runtime acceptance. See [sources and licensing](sources.md) for methodological boundaries.
