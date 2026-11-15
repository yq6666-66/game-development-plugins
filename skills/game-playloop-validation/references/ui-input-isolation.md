# UI 输入隔离：事件消费、持续状态和焦点不是一件事

[English](ui-input-isolation.en.md)

适用：开菜单仍移动、确认操作穿透、隐藏控件后释放触发玩法、暂停时界面不响应。先读取项目的模态/非模态规则和实际输入管线，不默认所有对话都暂停或冻结移动。

## 检查四个责任边界

1. **事件传播**：谁接收并标记处理，后续哪些处理阶段被跳过？不要只凭按钮回调运行就认定玩法不会收到。
2. **持续状态**：移动等是否在另一循环轮询全局按键？事件消费并不一定清除held状态。输入门控应由明确上下文负责；开关界面时处理旧按住意图与释放，不能同时创建竞争输入系统。
3. **焦点**：进入时的默认焦点、控件隐藏/删除后的后备焦点、退出后的返回目标。鼠标可点不等于键盘/手柄可达。
4. **暂停**：暂停物理/处理与停止信号不同。按项目设计保留必要UI响应，避免菜单确认与玩法重复动作。

## 最小验证表（建议，未执行）

- 按住移动→打开模态菜单→释放→关闭：门控遵守规则，关闭后无残留移动。
- 文字输入或确认：不同时触发已被上下文禁止的玩法；非模态边走边聊保留允许移动。
- 按下控件→控件隐藏→释放：分别记录按下/释放接收者与业务动作次数。
- 键盘/手柄进入→焦点项消失→取消退出：只测项目支持设备，验证有效后备和焦点恢复。
- 暂停→UI信号→恢复：界面响应正确，游戏副作用符合暂停合同。

## 来源与条件

2026-11-15 阅读 Godot 官方 4.5 文档相关段落：

- [Input](https://docs.godotengine.org/en/4.5/classes/class_input.html)：全局输入状态不受GUI消费自动影响。
- [InputEvent](https://docs.godotengine.org/en/4.5/tutorials/inputs/inputevent.html)：输入传播次序与处理标记。
- [GUI navigation](https://docs.godotengine.org/en/4.5/tutorials/ui/gui_navigation.html)：焦点与导航。
- [Pausing games](https://docs.godotengine.org/en/4.5/tutorials/scripting/pausing_games.html)：处理模式、暂停与信号。
- [Godot input.cpp](https://github.com/godotengine/godot/blob/876b290332ec6f2e6d173d08162a02aa7e6ca46d/core/input/input.cpp)，4.5-stable 对应提交，局部输入状态实现审查，不是整引擎审计。
- [Issue #112198](https://github.com/godotengine/godot/issues/112198)：作者报告4.5.1控件按下后隐藏、释放穿透；本轮未复现，不声称所有版本均存在该缺陷。

正文/API/局部源码已检查；没有运行Godot、用户游戏或目标设备，测试表不计PASS。发布日期未确认；版本固定但实现仍须按项目锁定版本复核。通用方法是区分事件、状态、焦点与暂停；Godot方法名与处理顺序不能照抄到其他引擎。只保留原创综合与链接，不复用上游源码或资产。
