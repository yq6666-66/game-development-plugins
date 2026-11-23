# Game engineering workflow

[中文入口](../SKILL.md). Input: goals, platform, chosen stack, actual files and change scope. Output: ownership/interfaces, a bounded implementation or design, reproducible entry and scoped evidence. No other Skill is required.

For a new project, identify one meaningful input-to-result-to-exit slice. Choose the smallest structure supporting it; do not inherit an example's engine or invent settled rules. A design-only request does not authorize project creation. For an existing project, inspect the entry, locked versions, build steps, writers and current behavior. Reproduce or state the blocker before changing a recoverable slice. A large file alone is not a reason to replace the framework.

For each affected state, name its creator, permitted writers, readers, reset and release owner. Separate rule and presentation responsibilities where useful without requiring pure functions, ECS or a singleton. Define a seam's request/result or event, error behavior and lifetime. Calls suit direct responses; notifications need ordering and subscription cleanup. Supply required dependencies at an observable composition point; small prototypes need not acquire a DI framework.

Distinguish spatial parentage from destruction ownership. A persistent player should not disappear with a room just because the hierarchy was convenient. See [boundary decisions](boundaries.md) when ownership or dependency choices are unclear.

Implement one authorized vertical slice while preserving callers and a baseline. Keep configuration, asset identity, serializable state and live objects conceptually distinct, without a mandatory folder or format. Do not upgrade engines, add services or publish implicitly. Compile and start the real entry, then exercise relevant exit/reload/cancel behavior. Test two instances if instancing is supported; shared state must be intentional.

For loading or scene transitions, use [loading readiness](loading-readiness.en.md) to distinguish resource retrieval, current ownership and playable state.

Deliver changed paths, interface decisions, alternatives, commands, observed results and recovery. Label static analysis, compilation and runtime separately; a unit test does not establish scene assembly. Missing device evidence is unverified. Escalate material scope changes rather than expanding the architecture. [Sources](sources.md).

Prefer existing runtime dependencies. For a necessary missing dependency, follow explicit task authorization and host rules rather than refusing a new project solely because no dependencies exist yet. This Skill itself does not authorize installation, new services, engine upgrades or publication.
