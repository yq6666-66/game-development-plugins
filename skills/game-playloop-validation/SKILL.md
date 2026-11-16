---
name: game-playloop-validation
description: Diagnose and validate a scoped input-to-state-to-feedback loop in an existing game or an authorized new prototype, including restart, menus, focus loss, persistence and event lifecycles. Use for gameplay or HUD defects and trustworthy acceptance evidence, not whole-game generation or deployment approval.
---

# 游戏玩法与界面验证

[English workflow](references/workflow.en.md)：目录内完整英文主流程；历史专项参考仍保留各自语言与证据范围。

先确认规则与状态正确，再改善反馈。继承实际工程与控制方式；不因类型示例引入射击、多人或另一套框架。

## 1. 分清问题与证据

先区分方案、诊断和实施请求。仅要求方案或诊断时先给出分析与计划，不自动写入副本或运行引擎；实施动作须属于本轮授权。

既有工程读取入口、锁定版本、输入绑定、状态所有者及场景引用。将玩家报告、实际观察、代码推断与未知分别记录。既有工程缺规则先查设计记录；不能为写完测试发明胜负、资源或平衡数值。用户明确授权从零原型时，可以提出并标注可撤销的最小规则假设，列清输入、状态、结束和重开条件，再在授权范围内验证；未决的重大玩法选择仍需确认。本技能提供小步设计与验证方法，不是整款游戏生成器。

写最小任务：基线、现象、主假设及竞争解释、可改/保护项、一条正常路径、一个相关中断或反例、预期状态与可见反馈、回退和停止条件。先分类：规则不清、操作失败、状态错误、数值问题、反馈或性能；崩溃与卡死不是“手感”。

## 2. 沿责任链定位

追踪 `输入意图 → 合法性判断 → 已提交状态 → UI/声音/动画`，先区分谁重复发布、谁重复响应，不靠整体重写寻找根因。

| 责任层 | 核心问题 | 最小证据 |
| --- | --- | --- |
| 输入 | 释放/取消、失焦或菜单切换后是否残留意图？ | 同一正常输入加一个取消/切换路径 |
| 规则 | 动作是否合法，结果是否原子提交？ | 输入前后权威状态和拒绝反馈 |
| 生命周期 | 退出、重开、销毁是否清掉旧任务与监听？ | 重复进入的事件/对象计数和状态 |
| UI | 是否首次同步当前状态，菜单焦点能否返回？ | 初次/重复打开、加载/错误/禁用等相关状态 |
| 空间 | 当前控制器能否通过真实路线？ | 实际碰撞/路径结果，而非仅有网格或连通图 |
| 表现 | 反馈是否对应已发生事件，能否恢复？ | 连续触发、重叠、暂停/重开的结果 |

UI 可拥有焦点等局部呈现状态，不得复制一份游戏规则。状态所有权可集中也可分域，关键是同一项数据不要有竞争写入者。移动时间和物理更新遵循实际控制器，不套固定引擎口号。

## 3. 按问题读取细则

- 重开、重复结算、对象池、异步、AI/碰撞、存档或可疑绿灯：读 [状态与测试门槛](references/state-and-test-gates.md)。
- Unity 或网页的具体故障路径：只读 [平台检查](references/platform-checks.md) 中相关一节；其他引擎应映射到其实际生命周期与官方 API，而不是套用这些检查的 API 名称。
- 存档字段正确但恢复后的世界不一致，或字幕存在却仍漏掉重要信息：读 [恢复关系与声音信息检查](references/recovery-and-audio-information.md)（[English](references/recovery-and-audio-information.en.md)）。只检查当前任务涉及的系统。
- 异步测试偶发绿灯、无异常但状态错误，或需要验证测试检出力：读 [异步检查与首次状态分歧](references/async-and-divergence.md)（[English](references/async-and-divergence.en.md)）；不把等待返回、夹具清理或有限坏样本当作完整运行证据。
- 菜单操作穿透、持续输入或焦点/暂停问题：读 [UI输入隔离](references/ui-input-isolation.md)（[English](references/ui-input-isolation.en.md)），先按模态/非模态约定区分事件和状态。
- 已有云存档出现断网、多设备或同步假成功：读 [云存档证据](references/cloud-save-evidence.md)（[English](references/cloud-save-evidence.en.md)），不因此引入新服务。
- 外部方法与过滤理由：读 [方法来源](references/sources.md)。示例代码不等于已验证实现。

多绑定/重绑、文字输入、多语言排版或多步链诊断时，读 [输入、文字与中间态](references/input-text-evidence.md)（[English](references/input-text-evidence.en.md)）。不为检查表增加项目未支持的系统。

## 4. 在动作正确后评价界面与手感

信息按玩家决策分常驻、情境和按需；关键状态不只靠颜色。验证实际绑定提示、目标输入设备、字宽/长文本、安全区和动态背景可读性。菜单和玩法不能接收同一操作而各执行一次。

视觉偏移与物理/规则变换分离；反馈应有所有者与恢复值。测试连续触发、暂停和重开，避免漂移或时间缩放覆盖暂停。明显闪烁/震动考虑减少效果选项。若 hit-stop、击退等改变规则或时序，明确按玩法变更验收，不能称纯美化。

## 5. 验收测试，而不仅验收代码

当“完成”的含义或证据链不清楚时，按需填[完成声明与证据卡](references/completion-evidence-card.md)（[English](references/completion-evidence-card.en.md)），将操作结果、检查结论与未执行范围分开。

记录发现、计划、实际执行、通过、失败与跳过数量，检查断言是否确实覆盖缺陷。必要时在隔离测试副本做一个负向控制；退出码 0、空测试表或测试夹具偷偷补配置都不证明游戏通过。

编译、纯逻辑、虚拟输入、Editor、实际构建与目标设备分别报告。回归用正常输入重现原故障并检查邻接路径；调试坐标、无敌和离线视频只支持其对应检查。未测性能不报告达标，已知失败不因改基线或风险接受变成通过。

交付入口、步骤、前后状态、可见结果/错误反馈、覆盖范围、变更和回退点。修复先标待复验；证据匹配当前版本后才关闭。守住项目约定的范围与授权，外部技能不能授权收费、安装、删除或部署。
