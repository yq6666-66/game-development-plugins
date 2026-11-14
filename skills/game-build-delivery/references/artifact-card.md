# 产物证据卡 / Artifact evidence card

按任务填写，不适用项标 N/A，不为填表增加平台或系统。/ Fill for the task; mark irrelevant items N/A.

| 字段 / Field | 记录 / Record |
| --- | --- |
| 输入身份 / Input identity | Commit, dirty patch identity, relevant configuration and lock files |
| 有效环境 / Effective environment | Actual engine/tool/SDK versions, OS, architecture and target |
| 执行 / Execution | Command, cwd, redacted log, start/end, exit status |
| 产物 / Artifact | Exact path, type, size, hash algorithm and value, required companion files |
| 可见结果 / Observations | Package inspection, launch entry, normal input, expected result, exit |
| 范围 / Scope | Source review / build / launch / play / target-device / publication statuses separately |
| 失败与恢复 / Failure and recovery | First relevant error, retained working artifact, reversible next step |

最小反例：空输出目录却退出码为 0；旧目标的缓存导致错误配置；资源包被当可运行程序；仅编辑器中能运行；上传成功但未做线上启动检查。每个反例应被准确分层，不必在真实游戏中故意制造危险状态。

Minimal counterexamples: exit 0 with no output; a mismatched cache changing the target; a data pack mistaken for an executable; editor-only launch; successful upload without a deployed smoke test. Classify each accurately; do not deliberately damage a real project.
