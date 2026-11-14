# 分类导航

[English](README.en.md) · [首页](../../README.md)

## 从零开发

1. 明确玩家、平台、输入、一局目标与最小成功标准；尚未确定的规则标作可撤销假设。
2. 使用[项目约定](../examples/project-contract.md)限定原型范围，选择技术而非被 Skill 绑定技术。
3. 先验证一个输入到状态到反馈的闭环；需要时用 [game-playloop-validation](../../skills/game-playloop-validation/SKILL.md)。
4. 有明确视觉目标后，用 [game-visual-iteration](../../skills/game-visual-iteration/SKILL.md)建立小样本，不把美术通过当作玩法通过。

[game-prototype-planning](../../skills/game-prototype-planning/SKILL.md) 现可用于创意、规则与最小原型规划。它不自动生成工程或完整游戏设计文档，本入口也不是已运行的游戏模板。

## 接手已有项目

1. 读实际文件、版本、启动方式、项目约定与已有证据，确认访问范围和可恢复基线。
2. 先复现一个具体问题，区分原作者陈述、源码推断和实际运行观察。
3. 按问题选技能，保留布局、规则、资产与输入等已确定条件，不另起框架。
4. 在允许范围修改并回归正常路径及相关中断路径；报告未验证部分。

## 八类导航

“现有覆盖”是相关方法，不代表整个分类已实现。

| 分类 | 触发问题 | 现有覆盖 / 后续候选 |
| --- | --- | --- |
| 游戏策划与原型 | 一局如何开始、结束，假设如何比较？ | [game-prototype-planning](../../skills/game-prototype-planning/SKILL.md) 可用；完整游戏策划文档不在其范围 |
| 架构与工程 | 状态由谁负责，模块如何协作？ | 玩法验证含状态与生命周期诊断；工程搭建 Skill 待建设 |
| 画面与美术 | 材质、光照、资产与可读性如何改善？ | [game-visual-iteration](../../skills/game-visual-iteration/SKILL.md) 可用 |
| 玩法与系统 | 输入、重开、存档、反馈是否正确？ | [game-playloop-validation](../../skills/game-playloop-validation/SKILL.md) 可用 |
| 界面与体验 | HUD 同步、菜单焦点、设备输入是否可用？ | 玩法验证含 UI 检查；独立 UI 设计 Skill 待建设 |
| 测试与性能 | 证据是否覆盖问题，运行成本是什么？ | 两项 Skill 含证据/性能检查；不是性能认证或完整测试平台 |
| 构建与协作 | 如何构建、交接、发布与回退？ | [项目约定](../examples/project-contract.md)与本包检查可复用；独立构建 Skill 待建设 |
| 工具与资源推荐 | 该用什么引擎、应用、工具或免费资源？ | [条件化推荐模板](../resources/README.md)可用；具体推荐目录待核验 |

类别不是目录迁移指令。两项既有 Skill 保留原路径，新增规划 Skill 采用独立目录并可独立复制；交叉主题通过导航关联。新增 Skill 需独立触发条件、输入输出和完整流程，不能按来源数量拆分。

## 后续贡献

[蒸馏教程](../distillation/README.md) · [作品展示提交说明](../showcase/README.md)。作品是未来验证与学习材料，不是本阶段必须上传的交付。
