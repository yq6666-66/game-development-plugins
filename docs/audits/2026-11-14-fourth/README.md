# 第四次蒸馏 · 2026-11-14

## 基线与真实范围

默认 main 为 `48915481118f7886a02ad2e7dea089436953186b`。为保留已批准但未合并的四项 Skill 与双语导航，本轮候选从开发分支 `docs/bilingual-navigation-foundation` 的 `dc01400cb2de59bed6465cb0a0955dbb54ece686` 建立，分支 `distill/fourth-pass-2026-11-14`。检查时无日/周研究分支；另外三条旧分支保留，不重复引入已合并内容。本轮不是从 main 偷换旧基线，也没有合并、发布或修改游戏。

先对照四项 Skill、现有参考、前轮审查与约定。以下为旧来源的针对性深层复读和通用方法细化，不声称所有项目重新全文审计、上游最新版本已核验或已运行。

## 本轮决策

| 主题 | 旧内容 | 本轮新价值与落点 |
| --- | --- | --- |
| 输入/文字/链路 | 已有取消、状态所有者与长文本 | playloop 新双语参考：多绑定语义、重绑、IME/字素簇、同tick中间态 |
| 工具接入 | 已有费用/许可与证据卡 | resource 新双语参考：执行面、分阶段数据/旁文件、决策寿命 |
| 网格/LOD/循环 | 已有导入合同与完整动作 | visual 新双语参考：统计口径、切换过程、姿态和速度接缝 |
| 原型观察 | 已有反证与竞争解释 | 计划字段补相反回应和受支持条件下的少数阻塞 |
| 蒸馏质量 | 已有分层证据 | 双语教程补不以WARN减少抵消关键FAIL |

新增的是三个细则主题及两项维护/规划细化，不是新增五个 Skill。四项 Skill 数量不变，各新增参考留在自身目录。英文新参考包含等价流程，固定来源详情可循同目录中文页读取；未宣称所有历史文件已双语。

## 固定来源与读取范围

1. **gamedev-skills/awesome-gamedev-agent-skills**, `c6ca6c41c839b68319ffc08430b99ab768debc32`：全文读取五个深层参考（含示例），链接见 [输入参考来源](../../../skills/game-playloop-validation/references/input-text-evidence.md#固定来源与边界)。不是所有上层 Skill 与 references 全覆盖。
2. **akillness/jeo-skills**, `f082e31bed503eed20f8c88608b0f071774e60c9`：全文复读 `.agent-skills/game-design-theory/SKILL.md`；未运行 validator。
3. **Jeffallan/claude-skills**, `078a25cc5bfd8011459be7b91d004e900c1d02d3`：全文复读 `skills/game-developer/SKILL.md` 及三个例子；未重复纳入固定性能/池等要求。
4. **omer-metin/skills-for-antigravity**, `e8dcf4e8737921a10088bd5c9eb65e81f74c051f`：全文复读 `skills/game-ui-design/SKILL.md`；其三份深层参考未重新穷读。不继承 controller-first 等默认。
5. **Donchitos/Claude-Code-Game-Studios**, `abc0de79d6ceb0b5d7aa693945849b3937afbe6a`：全文复读 `.claude/skills/skill-improve/SKILL.md`、`propagate-design-change/SKILL.md`、`architecture-decision/SKILL.md`；skill-test 开头/静态规范部分、architecture-decision/references/5-generate.md 前120行、compat-inventory.sh 前190行；balance-check 前90行、playtest-report 前100行。另取得线上仓库元数据及 main 的 skill-improve 正文；其他范围仍是固定快照。链接见 [工具参考](../../../skills/game-resource-selection/references/integration-surface.md#固定来源与读取范围)与[教程](../../distillation/README.md#比较蒸馏前后的质量)。
6. **blendi-remade/prompt2rig**, `218ce2adff35a7c04657768a85ff002ebd461c78`：全文读取 server.mjs 与 NOTICE，README 运行/许可段落、LICENSE 重检。静态数据流观察，不是全代码安全审计或最新版本声明。
7. **EL4CTEO/blender-skills**, `3e481ad1b8e301defced7369e4254022abe0821e`：全文复读 skills/blender-animation、blender-game-optimization、blender-texture-baking 下 SKILL.md，含示例，不审计关联脚本。
8. **arjun988/blender-skills**, `904f095d8f36a6e72adaebb08d07f884a074743d`：全文复读 .claude/skills/animation、asset-optimization、lod-pipeline 下 SKILL.md，含示例。美术方法链接见 [专项检查](../../../skills/game-visual-iteration/references/mesh-lod-animation-checks.md#来源与证据)。

## 未作为本轮新深度成果

- 黄铜之心：仍只有用户提供分析；原HTML、运行和许可未取得，不再包装为新源码发现。
- Fable：本轮重开仓库页不足以算深度重审；独立样本、录像与运行区别等已覆盖。
- Saltline：原件不可读，保留未核验；不拿 Fable 代替。
- Scenario、open-3d-skills、threejs-game-skills、awesome-copilot、Higgsfield、agent-sprite-forge、teardown：沿用前轮分级记录，本轮未重新全文检查，不虚增覆盖。相关方法无新证据时不重复计数。
- 过滤固定预算/帧率/默认引擎/固定暂停规则与无授权自动安装。来源中的零引用不等于无影响、FAIL+WARN总分可掩盖新失败，作为明确反例保留。

## 许可与验证

全部为原创转述与链接，没有复制代码、模型、素材、长文或执行上游脚本。MIT 不覆盖第三方依赖/输出。没有安装工具、外部生成、收费、引擎/游戏运行。

[本轮验证记录](../../validation/fourth-pass-2026-11-14.md)单列结构、单测与独立情境推演；历史宿主发现不能算新增参考已在模型回合加载。相关运行验证仍未完成。
