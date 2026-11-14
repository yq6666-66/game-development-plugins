# 游戏开发插件 · Game Development Plugins

**中文优先 · [English](README.en.md)**

一个持续蒸馏游戏开发经验的 **AI Agent Skills 技能包**，帮助游戏开发学习者、独立开发者和团队把问题转成可执行、可检查的小步任务。既适用于从零开发，也适用于接手与优化已有项目。

它不是 Unity / Unreal 的运行时插件，不是游戏引擎，也不保证自动生成完整游戏。方法不绑定任何引擎、框架、语言或游戏类型，Three.js 只是可能的实现选择之一。具体 API、依赖与性能需要在实际项目版本和设备上验证。

## 从这里开始

| 你的情况 | 下一步 |
| --- | --- |
| 从零开发 | [明确目标、最小玩法与验证样本](docs/navigation/README.md#从零开发) |
| 接手已有项目 | [读取真实工程、确认基线与保护项](docs/navigation/README.md#接手已有项目) |
| 已有具体问题 | [按八类能力与问题选择](docs/navigation/README.md#八类导航) |
| 想学习、改写或继续蒸馏 | [蒸馏方法与开放模板](docs/distillation/README.md) |

## 当前可用的 Skills

| Skill | 适用任务 | 边界 |
| --- | --- | --- |
| [game-resource-selection](skills/game-resource-selection/SKILL.md) | 按项目选择引擎、工具与资源，核查当前费用、平台和许可 | 不自动安装或付费，不把免费当作再分发授权 |
| [game-prototype-planning](skills/game-prototype-planning/SKILL.md) | 创意、规则与最小原型计划，定义观察信号和反证 | 不生成完整游戏，不以方案代替试玩 |
| [game-visual-iteration](skills/game-visual-iteration/SKILL.md) | 视觉参考拆解、材质与光照排错、资产接入、画面小步对比 | 不替代美术方向，不默认更换工具链 |
| [game-playloop-validation](skills/game-playloop-validation/SKILL.md) | 输入、规则、状态、生命周期、重开、存档、HUD 与反馈验证 | 不发明既有玩法，不代替发布授权 |

原型、画面与玩法三项 Skill 均支持已有工程或明确授权的新原型；尚未建立工程时，先写最小任务与可撤销假设，不把“缺少旧工程”当作拒绝从零开发的理由。

**八类导航不等于八项已实现技能。** 目前有上述四项可复制使用。更多独立 Skills、完整工具与免费资源目录、作品展示及完整双语参考库属于后续工作；[导航页](docs/navigation/README.md)逐项标明状态。尚未上传或验证使用本插件完成的游戏。

## 最小使用流程

1. 明确项目目标、目标设备、输入方式、允许改动与预期证据。可使用[项目约定模板](docs/examples/project-contract.md)。
2. 阅读选定 `SKILL.md`、所需参考文件与[兼容性边界](docs/COMPATIBILITY.md)。
3. 只复制 `skills/` 下**完整的单个 Skill 目录**到 Agent 宿主当前文档规定的位置。不要只复制入口，也不必安装全部技能。
4. 验证宿主实际识别技能。目录存在不等于加载成功；不支持 Skills 的宿主可将说明作为任务上下文读取。不要假定所有 Codex 环境使用同一个路径。
5. 每轮选择一个可验证目标，记录实际步骤、结果与未验证范围。仅咨询或制定方案不等于授权修改、安装或发布。

示例：
- 从零：“用 game-playloop-validation 为获准的新原型提出最小输入、结束与重开假设，标明哪些需要我决定，再验证一条完整循环。”
- 接手：“用 game-visual-iteration 读取现有工程，查清一个道具为何与场景不协调。保留原风格和布局，先给最小对比方案。”
- 排错：“重开后事件触发两次。追踪状态与监听的生命周期，不另造一套游戏框架。”

## 持续蒸馏与共同学习

本项目采用**每日研究蒸馏、每周整合更新**的维护节奏。研究来自开源项目、教程、官方文档、开发讨论与复盘，用自己的话提炼适用条件、步骤、取舍和验证方法，不以热度代替证据。

每日记录进入研究分支，每周成果进入可审阅的整合分支。**每周更新不等于每周自动合并主分支或发布版本**；不足、阻塞和未验证项如实保留，质量优先于数量。维护约定不是某次定时任务已成功执行的证明，以实际记录和提交为准。

欢迎使用、修改和分享本仓库的原创 MIT 模板，继续蒸馏适合自己的经验，并反馈方法与反例。[入门教程与模板](docs/distillation/README.md)说明怎样从资料形成可复用技能，而不是照搬第三方项目。第三方代码、文章、模型与素材仍遵守原许可。

## 检查与证据

Python 3.9+，仓库根目录执行，无第三方 Python 依赖：

```sh
python3 scripts/validate_package.py
python3 -m unittest discover -s tests -v
```

这些检查只覆盖包结构与校验行为，不证明宿主加载、引擎运行、真机控制或画面表现。查看[历史验证](docs/VALIDATION.md)、[导航文档检查](docs/validation/navigation-foundation-2026-11-14.md)、[原型规划检查](docs/validation/prototype-planning-2026-11-14.md)及[资源选择检查](docs/validation/resource-selection-2026-11-14.md)。中文与英文首页、导航和蒸馏入门已配套；新原型规划及资源选择 Skill 提供目录内完整英文流程；既有两项 Skill 正文以中文为主，部分技术与历史文档为英文，尚非完整逐文件双语。

## 文档与许可

[八类导航](docs/navigation/README.md) · [蒸馏教程](docs/distillation/README.md) · [兼容性](docs/COMPATIBILITY.md) · [来源](docs/PROVENANCE.md) · [历史审阅](docs/audits/2026-11-13/README.md) · [变更记录](CHANGELOG.md) · [MIT](LICENSE)

读取或安装本包不授予付费、上传、修改游戏、合并或部署权限。来源记录中的路径数量不是运行通过的技能数量。

[第四轮来源与增量](docs/audits/2026-11-14-fourth/README.md) · [验证记录](docs/validation/fourth-pass-2026-11-14.md)

## 公开资料蒸馏 · 2026-11-14

[每日研究](docs/research/daily/2026-11-14.md)为玩法闭环 Skill 补充存档关系恢复和重要声音信息覆盖的中英文参考。[验证范围](docs/validation/market-2026-11-14.md)区分包检查与游戏运行；原始日分支独立开展研究，本次整合保留其来源和历史验证范围。

[GitHub 追加蒸馏](docs/research/daily/2026-11-14-github-continuation.md)：补充异步结果、夹具清理、首次状态分歧和测试检出力检查；保持四项 Skills，不增加重复入口。
