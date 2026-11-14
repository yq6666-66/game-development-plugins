# Compatibility and scope

| Layer | What is provided | What has not been established |
| --- | --- | --- |
| Skill format | Two `SKILL.md` entries, relative references, optional Codex UI metadata | Automatic discovery in every host |
| Game reasoning | Scoped hypotheses, state ownership, lifecycle, evidence and asset contracts | A tested runtime implementation |
| Unity | Version-aware diagnostic checklist | Compilation, Editor/Player execution or hardware performance of a target project |
| Browser | Input cancellation, rendering lifecycle and device evidence checklist | Browser matrix, touch-device or WebGL conformance |
| Other engines | Transferable concepts | Engine-specific adapters or API recipes |

Use the actual locked project version. Do not upgrade an engine, switch renderer, add a framework, replace controls or change a camera because a source example did so. The selected skill should guide a task already in scope.

Some checklist items apply only to 3D, animation, networking, save data or paid generation. Mark unrelated items out of scope instead of adding those systems. Missing target-device evidence is unverified, not proof of failure or success.

Core skill instructions do not depend on an upstream CLI, MCP server or API key. References are provenance, not a command to execute source scripts. New dependencies and external actions require task-specific authorization under the host's policies.
