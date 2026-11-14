# 方法来源与采用边界

研究日期：2026-11-13。只读审查了以下实际技能及列出的参考，没有安装其工具链或运行游戏。这里是自主提炼，不复制整包指令；示例可编译、静态检测通过或作者自述不等于用户项目运行通过。

| 来源 | 纳入的方法 | 不纳入 |
| --- | --- | --- |
| [game-design-theory](https://github.com/akillness/jeo-skills/blob/f082e31bed503eed20f8c88608b0f071774e60c9/.agent-skills/game-design-theory/SKILL.md) | 单一可证伪问题、观察/假设分开、机制到感知的因果链 | 理论或JSON校验代替好玩/玩法验收 |
| [game-engine](https://github.com/github/awesome-copilot/blob/222eba62d518c27317e917c92e3ec1a7e6729455/skills/game-engine/SKILL.md) | 输入/更新/渲染分离，帧率独立，音频手势与WebGL恢复检查 | 从零模板、多人/商业化/发布范围 |
| [game-developer](https://github.com/Jeffallan/claude-skills/blob/078a25cc5bfd8011459be7b91d004e900c1d02d3/skills/game-developer/SKILL.md) / [Unity patterns](https://github.com/Jeffallan/claude-skills/blob/078a25cc5bfd8011459be7b91d004e900c1d02d3/skills/game-developer/references/unity-patterns.md) | 状态进入退出清理、配置与状态分开、先Profile | 全平台固定60FPS、强制ECS/LOD |
| [game-ui-design](https://github.com/omer-metin/skills-for-antigravity/blob/e8dcf4e8737921a10088bd5c9eb65e81f74c051f/skills/game-ui-design/SKILL.md) / [patterns](https://github.com/omer-metin/skills-for-antigravity/blob/e8dcf4e8737921a10088bd5c9eb65e81f74c051f/skills/game-ui-design/references/patterns.md) | 必要信息、动态提示、焦点/返回路径、非纯颜色编码 | 外部规则优先用户、控制器优先、统一安全区和字号 |
| [game-ui-ux](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/c6ca6c41c839b68319ffc08430b99ab768debc32/skills/disciplines/game-ui-ux/SKILL.md) | 菜单栈、焦点恢复、HUD初始同步和监听清理 | 固定引擎版本/设备/尺寸 |
| [threejs-game-ui-designer](https://github.com/majidmanzarpour/threejs-game-skills/blob/8286774b22a2566bf894dbc825825c16921866af/skills/threejs-game-ui-designer/SKILL.md) / [ui-patterns](https://github.com/majidmanzarpour/threejs-game-skills/blob/8286774b22a2566bf894dbc825825c16921866af/skills/threejs-game-ui-designer/references/ui-patterns.md) | 单一状态源、UI发意图、取消/失焦清理、长文本及数值宽度 | 套用HUD布局替换既定小地图与触控区 |
| [game-feel](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/c6ca6c41c839b68319ffc08430b99ab768debc32/skills/disciplines/game-feel/SKILL.md) | 先动作正确，表现/物理分离、重叠触发与效果归零、减震减闪 | 示例强度/秒数、默认攻击与命中玩法 |
| [higgsfield-websites](https://github.com/higgsfield-ai/skills/blob/27000402070db19d958789d05b3b52b6f4718d7c/higgsfield-websites/SKILL.md) / [game-flow](https://github.com/higgsfield-ai/skills/blob/27000402070db19d958789d05b3b52b6f4718d7c/higgsfield-websites/references/game-flow.md) | 规则/呈现/平台分层，动作合法性验证、资产清单 | 自动安装登录、无需确认生成封面、不检查生成物、自动部署及覆盖用户指令 |

## Unity 与跨平台核验

- [Unity input system](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/c6ca6c41c839b68319ffc08430b99ab768debc32/skills/unity/unity-input-system/SKILL.md)：查现有配置与动作资产，复用输入；静态、虚拟设备与实际设备测试分别记录。
- [Unity C# scripting](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/c6ca6c41c839b68319ffc08430b99ab768debc32/skills/unity/unity-csharp-scripting/SKILL.md)：保留 .meta/GUID，追踪场景/Prefab引用；编译不等于PlayMode。
- [level-design](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/c6ca6c41c839b68319ffc08430b99ab768debc32/skills/disciplines/level-design/SKILL.md)：按控制器能力复验通道与可达性，不为通过而修改冻结布局。
- [teardown](https://github.com/elvarofficial/teardown/blob/a91262ac1109051e014662d42ecb0b7bc1f113b1/SKILL.md)：机械、仪表、音效由同一状态驱动。
- [site-check](https://github.com/Moh4696/open-3d-skills/blob/53beb899e77f65d50160a3765f36f5ddb8b3c19b/skills/site-check/SKILL.md)：先定位功能/输入错误，再评估画面；区分模拟设备、软件渲染与真实目标平台。

不把任何外部技能的自动权限、自动部署、收费服务或模型默认值转成用户授权。需要复用代码时另查许可；本技能不包含第三方代码或资产。

## 本次深度复核的覆盖口径

固定提交链接用于可追溯，不表示已复跑。gamedev 80个入口分两组阅读：36个全文含示例，44个流程说明全文、代码未逐行审计；Studio 78入口流程均审阅，长模板与示例深度有别。Blender两仓28/94个入口的流程系统审阅，非全部脚本审计。Scenario 172入口全部取回并分级筛查，相关引擎/资产流程重点阅读，不称172个全部逐字审核。其余仓库按已列游戏入口及精选references阅读，混合仓库并非全量源码审计。

本轮没有安装上游工具、运行其脚本、启动引擎或调用收费生成服务；作者的“已验证”不转成本项目PASS。新细则分别见本技能入口链接的阶段门参考。Saltline仍缺可读原件，《黄铜之心》仍仅以用户提供分析作为方法来源。
