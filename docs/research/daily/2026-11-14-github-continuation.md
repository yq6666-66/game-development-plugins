# GitHub 追加研究 · 2026-11-14

## 基线与范围

基于执行时默认分支 `main` 的 `cc09648da6774850f1d76e74ec9be346acee31da`，新分支 `distill/github-discovery-2026-11-14`。检查当前四项 Skills、README、CHANGELOG、COMPATIBILITY、PROVENANCE、VALIDATION、project-contract 和既有研究。两个旧项目专属分支仍保留，不在本轮合并。先前第四轮、导航及公开资料研究已入 main，本轮不重复其输入重绑、IME、资产 LOD、存档关系和声音信息主题。

搜索词覆盖 GitHub GUT 异步测试及游戏开发 Skills 测试/状态机。候选来自搜索，结论来自实际克隆固定提交的文件，而非搜索摘要。深度主题为下述两项；未为了数量加入新的独立 Skill。

## 1. GUT：异步成功条件与测试夹具边界

- 项目/作者：[bitwes/Gut](https://github.com/bitwes/Gut)，Tom “Butch” Wesley；所读提交 `cf45f668709d988346e766afee916d4169a9283b`，提交时间 2026-08-18T10:28:41-04:00，读取 2026-11-14。
- 范围：README、`documentation/docs/Awaiting.md`、`documentation/docs/Memory-Management.md`、`addons/gut/test.gd` 中 `wait_for_signal`、`wait_until`、`assert_no_new_orphans` 相关实现和注释，以及 `addons/gut/LICENSE.md`。
- 问题：测试在等待后继续，却未证明事件发生；夹具清理掩盖产品未释放对象。
- 方法：区分等待结束原因与成功断言；选择对应更新阶段；把产品退出路径和测试框架兜底回收分开观察。
- 条件：GUT 为 Godot/GDScript 测试框架，版本必须匹配。当前源文件不是任意 Godot 版本的兼容保证。泛化方法可用于其他引擎，但 API 不迁移。
- 最小流程建议：先正常发出事件，再构造不发事件的隔离样本；分别记录等待返回与状态断言；产品退出后检查，再让夹具清理。**未实际执行。**
- 局限：孤立 Node 计数不覆盖所有资源或引用循环；延迟释放需要正确观察阶段。固定秒数/帧数不成为通用门槛。
- 许可：所读 MIT；本轮仅原创方法总结和链接，不复制源码。
- 落地：playloop 的新目录内双语参考及按需入口。有效性需在真实项目证明坏样本失败且健康样本通过。

## 2. abagames Skills：首次分歧与测试检出力

- 项目/作者：[abagames/agentic-gamedev-skills](https://github.com/abagames/agentic-gamedev-skills)；提交 `4ed8d751d08b5c1be14ccca02ce0b9a9bea60593`，提交时间 2026-10-17T18:25:47+09:00，读取 2026-11-14。
- 范围：README、根 LICENSE；`.agents/skills/localizing-game-state-divergence/SKILL.md` 及其 `references/observation-event.md`；`.agents/skills/generating-semantic-game-mutants/SKILL.md`。未审阅/运行其完整变异夹具、checker 或所有参考文件。
- 问题：没有异常的错误分数难定位，绿灯测试不知道能否发现实际机制缺陷。
- 方法：预先定义不变量，按事件保留稳定身份与前后读写；区分最早可见违规和原因；用健康/已知坏样本检查所选测试，修订后使用未见样本。
- 条件：精确回放定位需要忠实、可复现状态与输入；没有条件时不伪造确定性，也不强制现有项目重构。Agent 盲测需真实访问隔离。
- 最小流程建议：对重复计分的最小回放扫描首次违规，干预相关事件并检查邻接条件；在隔离副本去掉去重，确认现有断言能检出。**未实际执行。**
- 不直接采用的结论：有限 trace 全相同不等于证明语义等价；index 0 失败也可能是初始化缺陷；最早写过字段及移除事件后的差异不是充分因果证明。本文显式保留这些不确定性。
- 许可：根 MIT；本轮不复制夹具、示例代码或上游正文，采用原创综合步骤。
- 落地：与异步证据一起进入 playloop 参考，不新增相近 Skill。实际效果仍需目标项目和保留样本验证。

## 候选但本轮未转为正式能力

另一条只读研究线索提供 procedural-gen/level-design、GameCI 缓存隔离、playtesting 反馈分类。为避免扩展范围，本轮不计入这两个完成主题，也不声称在本分支复核了完整实现。未来优先核对程序化生成的跨进程复现及状态化可达性；先检查与既有审阅的新增价值。

## 本轮结果

实际修改：一项 Skill 的入口路由、新中英参考、README 双语摘要、CHANGELOG、PROVENANCE、本研究记录及[验证记录](../../validation/github-continuation-2026-11-14.md)。四项 Skill 数量不变。原件可由基线 Git 历史恢复，修改前另有本地备份。

资料状态：上述列明文件已读，函数仅局部源码核查。运行状态：未运行 Godot、GUT、上游 fixtures、浏览器游戏或 Agent 盲测。无安装、外部生成调用、合并、删除或发布。包检查不能替代这些运行证据。
