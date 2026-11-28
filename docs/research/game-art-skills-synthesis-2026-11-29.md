# 游戏美术 Skills 精选 · 同方向合并蒸馏

北京时间 2026-11-29。接续[实时 3D 专项](game-art-3d-2026-11-29.md)。研究范围：外部技能入口、明确列出的参考与工具声明，以及一手产品文档。以下把同一工作中的互补方法合成 **3 张诊断卡**，不把上游技能按仓库数量新增为本插件入口。分支候选，未改正式 Skill。[English quick reference](#english-quick-reference)

## 1. 程序化建模与高低模交付

**合并来源。** [EL4CTEO / blender-geometry-nodes](https://github.com/EL4CTEO/blender-skills/blob/ab601e27a247c18773924188eb580f81c561b249/skills/blender-geometry-nodes/SKILL.md) 与[配方](https://github.com/EL4CTEO/blender-skills/blob/ab601e27a247c18773924188eb580f81c561b249/skills/blender-geometry-nodes/references/recipes.md)贡献实例与字段的边界；[Setcode / blender-game-assets 的道具配方](https://github.com/setcodes/gamedev-skills/blob/096c224aa498a789fa99d476583029fcb9f538e1/skills/blender-game-assets/references/hard-surface.md)贡献同角度剪影比较和斜下方观察；[RobLe3 / blender-export](https://github.com/RobLe3/cc-blender-skill/blob/a2634b588e80265e796aa53f8ab178d75105c2af/plugin/skills/blender-export/SKILL.md) 和 [v1.4.0 验证记录](https://github.com/RobLe3/cc-blender-skill/blob/a2634b588e80265e796aa53f8ab178d75105c2af/docs/test-results/v1.4.0-integration.md)贡献最低层烘焙与实际导出的网格一致；[remiehneppo / blender-modifiers](https://github.com/remiehneppo/blender-skills/blob/d25db98be04bc46d77854e7da1bd8187dc982e43/skills/blender-modifiers/SKILL.md)提供提取求值网格的思路，但其示例包含遍历删除场景对象，不采用该操作。Blender 官方：[实例](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances.html)、[Cycles 烘焙](https://docs.blender.org/manual/en/latest/render/cycles/baking.html)。

**合并流程。** 保留可编辑母版和版本，另出交付副本。先按目标相机判定哪些细节影响轮廓、交互或碰撞，例如吊灯支架、屋檐厚度和台阶；浅纹理可以烘焙，但轮廓不能靠法线贴图补齐。散布任务固定输入、种子以及由任务定义的稳定标识；仅当目标端不支持实例或交付需要独立网格时，在交付副本上求值或实体化。烘焙前确认法线贴图对应实际低模、UV、投射设置和导出后保留的切线约定；不要在烘焙后无记录地换网格或重排 UV。

**最小验证。** 选一件带悬挑和接缝的小道具：同机位检查剪影，斜下方检查穿射和缺面，导入目标构建确认原定节点、比例与贴图；三个阶段各自记录。另用测试散布点中插入一个新点：若要求旧对象视觉保持不变，核共有 ID 的结果，而不是把相同 Seed 当保证。静态 JavaScript 合成检验：Seed 固定为 9，列表从 10/20/30 变为 5/10/20/30；按列表位置取值改变旧项 3/3，按稳定 ID 取值改变 0/3。可复现的合成映射为 `(key*31+9*17)%997`，只是排查思路，不代表 Blender 节点行为。若上游没能稳定保留 ID，写未支持或采用明确可复验的映射，不承诺新增元素不影响旧结果。

## 2. 程序化 PBR 与烘焙贴图交付

**合并来源。** [mulosbron / material-maker](https://github.com/mulosbron/game-dev-skills/blob/281bdc558484fea0046cb04f290bdc5f7c18b83d/skills/material-maker/SKILL.md) 提示将图源和目标导出物分开；[Setcode / blender-game-assets](https://github.com/setcodes/gamedev-skills/blob/096c224aa498a789fa99d476583029fcb9f538e1/skills/blender-game-assets/SKILL.md) 提供游戏视角与近景复查；用 [Material Maker 官方导出说明](https://rodzill4.github.io/material-maker/doc/export.html)和 [Khronos glTF 规范](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html)核对对应导出用途。这个主题管生成和绑定合同，不复制上一轮的 GLB 压缩或风格化灯光实验。

**合并流程。** 保留程序化图源、输入贴图来源和最终输出表。先确认需静态贴图还是目标端动态材质；名称相同不代表导出为同一种 Shader。记录目标引擎版本、确切导出配置、实际生成物、每张图的用途、通道、颜色或数据空间，以及消费者。复查目标构建里的实际材质绑定，不以导出器中的预览代替。若要验证表面凹凸、透明边缘或远景接缝，按问题分别选掠射光、明暗背景或正常相机移动。导出生成的脚本只作为待审查产物，不默认执行；不写入个人环境或游戏资源目录，本轮不装工具。

**最小验证。** 在同一几何和光照下做两块材质样板，分别改变粗糙度、金属度，在目标运行时检查是哪一个槽生效。用原创建模验证将两通道故意交换的反例必须能被发现，避免一张全灰样板掩盖错误。通过条件是服务于目标用途的图层和贴图确实被消费；看起来差不多但无法区分两个通道，就不能给通过。外部技能正文宣称 MIT；根目录和该技能目录常用 `LICENSE` 路径未取得。**只作原始线索，不镜像该技能，也不转用其代码和导出脚本**。Material Maker 工具本身另有 [MIT 许可](https://github.com/RodZill4/material-maker/blob/842d7e17cdf1060793b4ae57d70d98f1b7b972a6/LICENSE.md)，不覆盖第三方 Skill 或贴图。

## 3. GPU 帧排错：合并像素定位和性能证据，但不混用

**合并来源。** [JiaboLi / renderdoc-mcp](https://github.com/JiaboLi-GitHub/renderdoc-mcp/blob/176d12ba194eef5f6a4b7fc7d0ae90cda923afcd/skills/renderdoc-mcp/SKILL.md) 提供先定位错误像素及相关绘制事件的方法；[dcc-mcp / renderdoc-perf](https://github.com/dcc-mcp/dcc-mcp-renderdoc/blob/8c28ff276d3fbf79ded71d99303dfeb70b1bd233/src/dcc_mcp_renderdoc/skills/renderdoc-perf/SKILL.md) 和[工具声明](https://github.com/dcc-mcp/dcc-mcp-renderdoc/blob/8c28ff276d3fbf79ded71d99303dfeb70b1bd233/src/dcc_mcp_renderdoc/skills/renderdoc-perf/tools.yaml)提供先核回放、计时和驱动计数器的范围；像素定位与格式能力可对照 [RenderDoc v1.45 官方文档](https://github.com/baldurk/renderdoc/blob/v1.45/docs/how/how_inspect_pixel.rst)。只借决策顺序，MCP 不作为依赖。

**合并流程。** 先确认目标是画错还是画慢。画错：冻结已获准分析的构建和捕获，记录设备、API、分辨率、帧与目标像素；从首次出现差异的渲染阶段查目标、深度、混合和贴图绑定，功能支持时才使用像素历史。画慢：先读环境实际支持的计数器和单位，记录回放能测什么；用游戏中同一路线实测确认持续影响。绘制数量只用于定位，不能作为 GPU 时间。基于投影三角形的覆盖热图不是 GPU 实测像素开销。无回放或计时能力时直接标未测，不报 0 ms，不推断性能通过；不要用 Game/Editor 设置、诊断工具改动或兼容性切换抹去反例。捕获可能含私有纹理与 Shader，未经许可不外传。

**最小验证。** 构造两个独立反例：目标像素在写入时正确、被后续透明合成覆盖时，检查应定位到后续绘制，而不是改基础材质；计时不可用但捕获能重放时，检查应输出“时长未测”，仍可列事件与绑定用于排查。前述为情境推演，未生成或重放 GPU 捕获。

## 收录依据与后续落点

本轮阅读 **7 个外部技能入口**：Geometry Nodes、Modifier、Blender Game Assets、Blender Export、Material Maker、RenderDoc MCP、RenderDoc Perf。另读列出的参考、工具声明与官方文档。热度采用 2026-11-29 北京时间检索时 GitHub 页面显示的累计 Stars，不是新增 Star 榜：[EL4CTEO Blender Skills](https://github.com/EL4CTEO/blender-skills) 约 3.0k、[cc-blender-skill](https://github.com/RobLe3/cc-blender-skill) 196；[Material Maker](https://github.com/RodZill4/material-maker) 约 6.3k、[RenderDoc](https://github.com/baldurk/renderdoc) 约 11.4k，各自均为工具热度，不转嫁到第三方 Skill。小型来源因方法差异和可追溯性纳入，不称热门。EL4CTEO 已出现在[旧来源表](../../skills/game-visual-iteration/references/workflow-sources.md)；此次只增稳定身份反例，不重复收 Blender QA 入口。识别到 Agent-Fleet 的 Blender Core 明列 EL4CTEO 为来源，因此不将其作为另一项独立佐证。

[EL4CTEO](https://github.com/EL4CTEO/blender-skills/blob/ab601e27a247c18773924188eb580f81c561b249/LICENSE)、[Setcode](https://github.com/setcodes/gamedev-skills/blob/096c224aa498a789fa99d476583029fcb9f538e1/LICENSE)、[RobLe3](https://github.com/RobLe3/cc-blender-skill/blob/a2634b588e80265e796aa53f8ab178d75105c2af/LICENSE)、[dcc-mcp](https://github.com/dcc-mcp/dcc-mcp-renderdoc/blob/8c28ff276d3fbf79ded71d99303dfeb70b1bd233/LICENSE) 在固定版本核对了 MIT 文件；其他未核清条款的来源只作链接，不复制。未安装、执行上游、审计整个包、导入 Unity 或验证设备表现。本报告唯一执行项是独立的合成身份检查。建议仍由已有 [game-visual-iteration](../../skills/game-visual-iteration/SKILL.md) 承接；正式整合前优先用一个道具和一条 GPU 缺计时反例验证，不修改项目配置，不把第三方安装步骤、许可或作者验收直接继承进来。

## English quick reference

1. **Procedural geometry and bake handoff:** Keep an editable master; identify silhouette and interaction geometry at the intended camera. Verify persistent IDs when adding elements and bind the normal bake to the precise low-poly export. Compare the front, underside and target import.
2. **Procedural PBR delivery:** Track source graph, target profile, output maps and consumer bindings. Use distinct metallic and roughness signals and a deliberately swapped negative fixture. Do not execute generated scripts by default.
3. **GPU frame diagnosis:** Use the first incorrect render stage for a visual failure. Gate counters by actual replay support; an unavailable timer is unknown, not zero. Confirm any sustained cost on the original player route. These are research workflows, not installation or production test results.
