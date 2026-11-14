# Integration surfaces and decision lifetime

[中文](integration-surface.md). Use for host integrations, automation, local services or generation pipelines. This is neither security certification nor an installation instruction.

Map entry → files/configuration → trigger (load, invocation, build, runtime) → read/write scope → external service/account/cost → target-host replacement or missing feature. Readable SKILL.md content does not make dynamic shell, hooks, configuration parsers or Agent tools portable. Do not transplant permissions, model choices or automatic execution settings.

Static scans yield leads. Content readability, metadata discovery, call-chain execution and target results are separate checks. Missing host tools are a capability gap, not cross-host compatibility PASS.

Trace input, generation, postprocessing, export and publication separately. A local UI/server does not make generation offline; an offline-viewable result does not remove upstream service dependencies. Inspect transmitted prompts, images/URLs, worker routing and companion JSON/logs/source URLs, not just the model file. Private prompts and time-limited access URLs may require review before sharing.

Read interface/export logic first. If execution is authorized, use public sample inputs to observe actual traffic and outputs. Without execution, report static flows, not a confirmed leak or passed security test. Execution and sharing remain subject to authorization.

Keep a lightweight decision record when useful: proposed/trial/adopted/superseded/withdrawn; requirements, assumptions, alternatives, verified scope, review triggers, affected outputs and exit costs. Reuse existing ADRs. Recommendation is not adoption; completed documentation does not unlock dependent work. Recheck affected assumptions when platforms, versions or use change without discarding unchanged evidence.

No registered references found does not prove no impact. A newly documented requirement may affect existing code. Small projects need not adopt a full architecture bureaucracy.

[Fixed sources and reading scope](integration-surface.md#固定来源与读取范围): Studio abc0de79… and prompt2rig 218ce2ad…; full and partial reads are explicitly separated. No scripts are copied or run, no complete security review or dependency/output commercial-license clearance is claimed.
