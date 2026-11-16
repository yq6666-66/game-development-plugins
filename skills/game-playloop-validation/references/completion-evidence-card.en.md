# Completion claims and evidence worksheet

[中文](completion-evidence-card.md). Use when a successful button callback or green test does not establish what actually finished. This worksheet organizes existing state, async, input and persistence guidance; it adds no framework or game system. Select relevant rows only. Cloud saves, menus and restart are not mandatory features.

## Define the claim before judging it

- **Claim:** which version, route and outcome? “This slot persisted locally” is narrower than “the save system is complete.”
- **Observation layer:** input, authoritative business state, persistence/remote boundary or UI? A callback is not a committed outcome; a label is not proof of a saved result.
- **Expected condition and termination reason:** define success, rejection, cancellation and timeout independently. Returning from a wait is not automatically success.
- **Environment and authority:** record the actual build, inputs, versions and recoverable test data. Execution, data changes and services must be authorized. A planning-only task leaves results unexecuted.

## Fill only the relevant paths

| Path | Normal input and preconditions | State or side effect to observe | Expected versus actual | Outcome and evidence |
| --- | --- | --- | --- | --- |
| Normal completion | Enter through the real route and trigger the scoped action | Which owner committed what, and does feedback agree? | Write expectation before recording observation | PASS/FAIL/BLOCKED/unexecuted with current-version evidence |
| Relevant counterexample | Invalid condition, rejection or authorized isolated known-bad sample | Was an unwanted change prevented; can the check detect it? | Do not invent failure rules absent from the game | An expected rejection can pass; no exception alone cannot |
| Interruption and recovery | Relevant held-input/menu, cancellation, scene switch or disconnect | Can stale intent/work survive; who owns the restored state? | Follow the existing modal, pause or recovery contract | Timeout/cancellation are operation outcomes, not automatic test verdicts |

Separate the operation outcome from the check verdict. Correct rejection of a stale write can PASS a conflict check. A timed-out operation expected to succeed cannot PASS just because the test ended. Unexecuted paths are not passes. Explain exclusions rather than adding features. Account for planned scope, executed checks, terminal outcomes and uncovered paths so no planned check silently disappears.

## Synthetic example: the UI says “saved”

These are proposed checks, not execution records or a prescribed service/conflict algorithm.

1. Local save: trigger normal input, reload isolated data, and compare required identities, relationships and fields. A write callback alone cannot establish world restoration.
2. Only if cloud saves are in scope: disconnect after local persistence but before remote acknowledgement, then restart. If acknowledgement already occurred, retain that state separately; a later disconnect does not undo it. Judge local recovery separately from remote acknowledgement; pending synchronization is not confirmed. Use the actual protocol later, without adding a service.
3. Only if concurrency is in scope: have two isolated clients write from the same version. Check rejection, merge or overwrite under the approved policy. Expected conflict rejection is not a broken save system; removing a lock to overwrite is not a conflict fix.

For a local-only prototype retain item 1 and exclude the others. Unsettled rules remain a design question; do not choose a vendor, timestamp algorithm or global pause merely to complete the table.

## Select existing details

- Waits, stale callbacks, fixture cleanup or suspicious green results: [async and divergence](async-and-divergence.en.md).
- Wrong restored relationships or missing essential sound information: [recovery and audio information](recovery-and-audio-information.en.md).
- Consumed menu events with continuing movement: [UI input isolation](ui-input-isolation.en.md).
- Local, remote and concurrent outcomes: [cloud-save evidence](cloud-save-evidence.en.md).
- General state, restart and lifecycle: [state and test gates](state-and-test-gates.md), a historical Chinese reference.

## Provenance and limits

The 2026-11-16 weekly integration reorganizes existing local guidance into an original worksheet, not a new upstream runtime finding. Linked references preserve authors, versions, reading dates and source links: the 2026-11-14 Godot 4.4, XAG 104, GUT `cf45f668` and abagames `4ed8d751` readings, and the 2026-11-15 Godot 4.5, Unity Cloud Save and Steam Cloud readings. Consult those references for exact scope and unexecuted checks. This Skill remains independently copyable without outer repository research notes. Weekly validation covers document scenarios and packaging, not engine, service or game execution. MIT covers this original text, not third-party content.
