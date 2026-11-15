# Compatibility and scope

| Layer | What is provided | What has not been established |
| --- | --- | --- |
| Skill format | Seven `SKILL.md` entries, relative references, optional Codex UI metadata | Automatic discovery in every host |
| Game reasoning | Scoped hypotheses, state ownership, lifecycle, evidence and asset contracts | A tested runtime implementation |
| Unity | Version-aware diagnostic checklist | Compilation, Editor/Player execution or hardware performance of a target project |
| Browser | Input cancellation, rendering lifecycle and device evidence checklist | Browser matrix, touch-device or WebGL conformance |
| Other engines | Transferable concepts | Engine-specific adapters or API recipes |

Use the actual locked project version. Do not upgrade an engine, switch renderer, add a framework, replace controls or change a camera because a source example did so. The selected skill should guide a task already in scope.

Some checklist items apply only to 3D, animation, networking, save data or paid generation. Mark unrelated items out of scope instead of adding those systems. Missing target-device evidence is unverified, not proof of failure or success.

Core skill instructions do not depend on an upstream CLI, MCP server or API key. References are provenance, not a command to execute source scripts. New dependencies and external actions require task-specific authorization under the host's policies.

## Scoped host evidence · 2026-11-14

Codex CLI `0.167.0-alpha.4` app-server discovered `game-resource-selection` from an isolated project `.agents/skills` folder and parsed its metadata without errors. [Evidence and reproduction](validation/codex-discovery-2026-11-14.md). Authenticated model-turn loading remains blocked/unverified; this does not establish other hosts or versions. Earlier validation records retain their original scope.

## Local Markdown checks

The package validator checks file targets for inline links and same-document reference links (`[text][id]`, `[id][]`, and `[id]` when a definition exists). It supports single-line `[id]: path` or `[id]: <path>` definitions without titles, with case-insensitive, whitespace-normalized labels. Duplicate definitions are rejected by this package convention; explicit/collapsed undefined labels are errors. Fenced and inline code examples (including multiline code spans with equal-length backtick delimiters) are excluded. Escaped square brackets/backticks are masked with backslash parity preserved.

This is a bounded packaging check, not a CommonMark parser: multiline destinations, optional titles, general escape syntax/nested brackets, embedded HTML, percent-encoded paths and fragment/heading validity are not fully validated. External URL accessibility is not tested. Prefer the supported plain syntax for required portable references, and manually review other forms. A parser PASS does not establish host loading or gameplay.

## 双宿主候选封装

新增插件清单不扩大引擎兼容性承诺。见[安装说明](../PLUGIN-README.md)与[独立证据记录](validation/dual-host-plugin-2026-11-15.md)。宿主发现、实际调用和实际游戏运行分别验收。
