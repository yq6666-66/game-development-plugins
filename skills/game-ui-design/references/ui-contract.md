# 界面契约 / UI contract

按当前屏幕填表；以下是合成的暂停设置示例，不是默认玩法需求。
Fill for the current screen. This is a synthetic pause/settings example, not a required game feature.

| 转换 / Transition | 输入与焦点 / Input and focus | 状态与反馈 / State and feedback |
| --- | --- | --- |
| 游戏到菜单 / Play → menu | 菜单接收导航；选择有效初始项 / menu owns navigation, valid first item | 是否暂停按规则；显示实际设置 / pause by contract, show real settings |
| 打开设置 / Open settings | 保存返回目标；焦点进入设置 / retain return target, enter settings | 未保存改动与应用结果分离 / distinguish draft from applied value |
| 取消 / Cancel | 返回有效调用项，已删除则后备 / restore invoker or fallback | 丢弃还是保留草稿需定义 / define draft retention |
| 应用失败 / Apply fails | 保留可重试或退出路径 / retry or exit stays reachable | 提示真实错误，不能先显示成功 / do not show premature success |

交付额外记录：状态来源、文字长度范围、支持尺寸/语言/输入、禁用原因、事件重复处理、图层遮挡、验证范围。
Also record state source, text range, supported sizes/languages/inputs, disabled reasons, duplicate activation, occlusion and validation limits.
