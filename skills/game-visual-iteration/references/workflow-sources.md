# 外部工作流来源

研究日期：2026-11-13。以下为对实际文档/部分源码的只读审查所提炼的方法；没有安装、执行或验证这些工具在用户工程中的兼容性。技能使用自主转述，不打包第三方代码或资源。星数、技能数量、作者性能/完成度宣传不作为验收依据。

| 已审查来源 | 采用的方法 | 不继承的默认行为 |
| --- | --- | --- |
| [Game Studios / asset-audit](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/abc0de79d6ceb0b5d7aa693945849b3937afbe6a/.claude/skills/asset-audit/SKILL.md) | 资产清单、场景/Prefab引用核查、证据不足标未评估 | 整套 hooks、自动提交或工作室配置；网页验证不等于 Unity |
| [Sprite Forge / video2dsprite](https://github.com/0x0funky/agent-sprite-forge/blob/25203d03900b46b444bdd72a75768c33d1895ad6/skills/video2dsprite/SKILL.md) | 已批准母版、尺度锚点、逐动作验收、数值与目视结合 | 已有 API key 不等于生成/付费同意；遵循当前项目的有界重试约定 |
| [teardown](https://github.com/elvarofficial/teardown/blob/a91262ac1109051e014662d42ecb0b7bc1f113b1/SKILL.md) | 机械、UI、声音共用状态；受控录像与运行性能分开 | 自动机械动作或部署；60 fps录制不等于实时60 fps |
| [Blender asset QA](https://github.com/EL4CTEO/blender-skills/blob/3e481ad1b8e301defced7369e4254022abe0821e/skills/blender-asset-qa/SKILL.md) | 几何/UV/材质检查结合多视角与线框 | 自动改尺寸、朝向、槽位或删除冻结几何 |
| [Scenario Unity lighting](https://github.com/scenario-labs/skills/blob/94cab3f1da47841f52d4c7b3ea8583aa13dd0eb9/skills/game-engines/unity/scenario-unity-rendering-lighting/SKILL.md) | 实际生效配置、固定曝光机位、逐项照明检查 | 作者平台路径、数值阈值及兼容性结论 |
| [prompt2rig server](https://github.com/blendi-remade/prompt2rig/blob/218ce2adff35a7c04657768a85ff002ebd461c78/server.mjs) / [worker](https://github.com/blendi-remade/prompt2rig/blob/218ce2adff35a7c04657768a85ff002ebd461c78/hq/worker.py) | 预览、最终资产、实际运行分层；骨架映射与动作复核 | 自动下载模型或调用云服务；[NOTICE](https://github.com/blendi-remade/prompt2rig/blob/218ce2adff35a7c04657768a85ff002ebd461c78/NOTICE)显示依赖许可混合，不能默认可商用 |
| [open-3d / site-check](https://github.com/Moh4696/open-3d-skills/blob/53beb899e77f65d50160a3765f36f5ddb8b3c19b/skills/site-check/SKILL.md) | 先功能错误再美化、设备/GPU与模拟范围、帧时间证据 | 将浏览器模拟当真机，复制网页模板重造场景 |
| [gamedev skills router](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/c6ca6c41c839b68319ffc08430b99ab768debc32/router/SKILL.md) / [level-design](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/c6ca6c41c839b68319ffc08430b99ab768debc32/skills/disciplines/level-design/SKILL.md) | 按工程指纹选择最少技能、按实际控制器复验可达性 | 升级到技能假设版本；第一人称不等于射击游戏 |

## Blender 制作与导入

来源：[arjun988/blender-skills director](https://github.com/arjun988/blender-skills/blob/904f095d8f36a6e72adaebb08d07f884a074743d/.claude/skills/blender-director/SKILL.md)、[hard-surface](https://github.com/arjun988/blender-skills/blob/904f095d8f36a6e72adaebb08d07f884a074743d/.claude/skills/hard-surface/SKILL.md)、[lowpoly-style](https://github.com/arjun988/blender-skills/blob/904f095d8f36a6e72adaebb08d07f884a074743d/.claude/skills/lowpoly-style/SKILL.md)、[uv-workflow](https://github.com/arjun988/blender-skills/blob/904f095d8f36a6e72adaebb08d07f884a074743d/.claude/skills/uv-workflow/SKILL.md)、[unity-export](https://github.com/arjun988/blender-skills/blob/904f095d8f36a6e72adaebb08d07f884a074743d/.claude/skills/unity-export/SKILL.md)。

采用用途/平台/距离先定、轮廓优先、实例化、多角度检查和导入后复核。未采用固定面数、贴图尺寸、统一倒角/法线要求、单材质槽、默认轴转换或简化 UV 密度公式。其 MCP 可以运行任意 Python，本次未安装或执行；这不是默认允许自动操作的工作流。

实际复用任何代码/资产前，重新核对对应版本许可与依赖条款。只读研究不构成运行、安装、付费或发布授权。

## 本次深度复核的覆盖口径

固定提交链接用于可追溯，不表示已复跑。gamedev 80个入口分两组阅读：36个全文含示例，44个流程说明全文、代码未逐行审计；Studio 78入口流程均审阅，长模板与示例深度有别。Blender两仓28/94个入口的流程系统审阅，非全部脚本审计。Scenario 172入口全部取回并分级筛查，相关引擎/资产流程重点阅读，不称172个全部逐字审核。其余仓库按已列游戏入口及精选references阅读，混合仓库并非全量源码审计。

本轮没有安装上游工具、运行其脚本、启动引擎或调用收费生成服务；作者的“已验证”不转成本项目PASS。新细则分别见本技能入口链接的阶段门参考。Saltline仍缺可读原件，《黄铜之心》仍仅以用户提供分析作为方法来源。
