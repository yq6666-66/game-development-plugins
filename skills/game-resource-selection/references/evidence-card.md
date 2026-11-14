# 候选证据卡 / Candidate evidence card

仅填已知项；未知保留并说明后果。Fill known information; retain unknowns and their consequences.

| 字段 / Field | 内容 / Content |
| --- | --- |
| 需求 / Need | 项目问题、范围、预算、平台、现有栈与不得改变项 / Problem, scope, budget, platforms, stack and invariants |
| 候选 / Candidate | 名称、官方入口、维护者、版本/套餐/提交 / Name, official entry, maintainer, version/plan/commit |
| 证据 / Evidence | 来源链接、访问日期、读取范围、具体支持的事实 / URL, access date, scope and supported fact |
| 接入 / Integration | 依赖、硬件、宿主与导出平台、输入输出 / Dependencies, hardware, host/export platforms, inputs/outputs |
| 成本 / Cost | 免费范围、必要费用、触发条件、币种/地区/未知 / Free limits, mandatory costs, triggers, currency/region/unknowns |
| 权利 / Rights | 商用、修改、署名、打包、原文件再分发、条款与许可版本 / Commercial use, modification, attribution, packaging, raw redistribution, terms/license version |
| 状态 / Status | 官方已读 / 作者声称 / 自己推断；运行环境或未运行 / Official inspected / author claim / inference; execution environment or not run |
| 决定 / Decision | 推荐/条件适用/BLOCKED待核验、依据与风险 / Recommended/conditional/BLOCKED-unverified, reasons and risks |
| 验证 / Verification | 最小输入、步骤、结果、失败与回退 / Minimal inputs, steps, results, failures and rollback |
| 替代 / Alternative | 复用现有工具或不引入依赖的路线 / Existing-tool or no-new-dependency route |

## 负向示例 / Negative example

素材页面写“free”，但未说明原文件再分发。不能因此把素材提交到公开模板仓库，也不能把整页缺失当作已检查许可。可记录链接，并将公开打包列为待权利确认。此示例不对应任何真实产品或已运行测试。

An asset page says “free” without raw-redistribution terms. Do not put it in a public template repository or call missing terms verified. Record the link and block packaging pending rights confirmation. This is illustrative, not a claim about a real product or executed test.

- 可选 / Optional: 执行触发与数据路径 / execution triggers and data flow; 采纳状态、复查触发与受影响产物 / adoption status, review triggers and affected outputs.
