# 重绑定不是改一个键：持久化身份、加载失败与设备恢复

读取日：2026-11-16（Asia/Shanghai）。本轮为文档和局部源码检查，未运行 Unity、样例或真实设备。

## 来源、版本与读取范围

Unity Technologies / InputSystem，固定开发快照 `3ec61dddad2cffb6badc9092eb8b39152c5cf3ef`（提交 2026-11-12T09:40:02Z）。package.json 声明 1.20.2、Unity 6000.0；CHANGELOG 最新为 Unreleased，因此不能称该快照为已发布 1.20.2。README 还保留旧 Unity 前置说明，实际项目须核包清单与自己的锁定版本，不据旧段落降级。

已读：
- [README](https://github.com/Unity-Technologies/InputSystem/blob/3ec61dddad2cffb6badc9092eb8b39152c5cf3ef/README.md)、package.json、LICENSE.md 全文；README 表明从 Unity 6.7 起开发转内部仓库，公开库维护模式，不能将本快照称为所有 Unity 版本最新实现。
- [RebindSaveLoad.cs](https://github.com/Unity-Technologies/InputSystem/blob/3ec61dddad2cffb6badc9092eb8b39152c5cf3ef/Assets/Samples/RebindingUI/RebindSaveLoad.cs) 与 [RebindActionUI.cs](https://github.com/Unity-Technologies/InputSystem/blob/3ec61dddad2cffb6badc9092eb8b39152c5cf3ef/Assets/Samples/RebindingUI/RebindActionUI.cs) 全文。
- [InputActionRebindingExtensions.cs](https://github.com/Unity-Technologies/InputSystem/blob/3ec61dddad2cffb6badc9092eb8b39152c5cf3ef/Packages/com.unity.inputsystem/InputSystem/Runtime/Actions/InputActionRebindingExtensions.cs) 1181–1310 行保存/恢复实现与注释；不是全文件审计。
- [CHANGELOG](https://github.com/Unity-Technologies/InputSystem/blob/3ec61dddad2cffb6badc9092eb8b39152c5cf3ef/Packages/com.unity.inputsystem/CHANGELOG.md) 1–65 行，包含 1.20.0 输入抑制行为变更，只记录上游修复声称，未复现。
- 官方 [Input Bindings 1.14.2](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.14/manual/ActionBindings.html)：override、saving/loading、displaying 小节；[Devices 1.14.2](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.14/manual/Devices.html)：reset、sync、disconnected/device ID 小节。页面生成日期 2025-08-06 不等于发布日期。旧版文档用于机制对照，不据此声称新快照所有 API 一致。
- GitHub issue 搜索未取得可用主体；不将其计为研究证据。

## 解决的问题与新增价值

已有 input-text-evidence 覆盖重绑取消、冲突和提示，ui-input-isolation 覆盖事件/held 状态。本次新增的是“改键后重启/升级/换设备仍对应同一个动作”的恢复证据，不重复创建输入 Skill。

## 已读机制

1. Unity override 并不随普通 action JSON 自动持久化，需专门保存恢复。恢复 API 默认先移除现有 overrides，随后解析输入，按 binding ID 找目标，找不到只给警告。**推断**：坏 JSON 或旧资产 ID 不匹配可能使恢复部分失败或先失去原覆盖，调用返回/没有崩溃不是完整恢复证明。
2. UI 样例用 binding ID 找条目，显示当前有效绑定并响应 BoundControlsChanged，而不是只在改键成功时刷新。组合绑定逐部件执行；取消当前部件不自动证明整组回滚。样例 Disable 分支直接 Dispose，与 Cancel 回调清理不是同一段逻辑，因此隐藏/销毁时的状态恢复应独立验证，不能照搬示例宣称无遗漏。
3. 设备重连可复用实例；设备 ID 的唯一性限 Unity 会话，不能直接当跨启动用户身份。Reset 是取消动作，不等价于伪造一次松键；项目须区分解除按住和提交“松开完成”的玩法。

## 可复用流程与条件

适用于已有或获准的重绑/多设备功能，输入为实际 action 资产、用户配置、版本及设备合同，输出为绑定恢复表和正常输入证据。无此功能的项目跳过，不引入 Unity 或云服务。

- 先记动作/绑定稳定标识、默认值、当前覆盖、有效控件、显示提示、配置版本和用户归属；不要持久化数组下标或设备会话 ID 当长期身份。
- 将读取、结构校验、ID/类型匹配、应用和必要回退分开。加载前保留可恢复快照；未知绑定按项目约定迁移、忽略并报告或回退，不能把警告等同成功，也不自创通用合并算法。
- 组合重绑定义取消的原子边界：单部件还是整组。任意退出路径都检查操作资源、监听、输入上下文和原 enabled 状态；具体实现按版本验证，不强制全部 action map Enable。
- 配置恢复后再核 UI 与实际动作；设备断开、重连及键盘布局变化分别记录配置、解析结果与展示，不因一次热插拔清掉玩家长期偏好。

## 最小验证（待运行，不计 PASS）

| 路径 | 应观察什么 |
| --- | --- |
| 改一键→保存→彻底重启→按新/旧键 | 配置、有效绑定、提示与动作次数一致 |
| 保留旧配置，调整资产顺序或移除绑定 | 不误绑别的动作；未知ID按合同可见处理 |
| 坏JSON/缺字段→加载 | 不静默丢掉可用配置，失败可恢复 |
| 组合绑定完成第一部件→取消/关闭界面 | 符合单部件/整组提交约定，无输入被永久禁用 |
| 按住→拔设备→重连；换布局 | 不误触松开提交、无卡住意图，提示匹配实际控制 |

这些是基于源码的情境建议，不证明目标平台驱动和运行行为。成本包括配置迁移、设备矩阵、输入上下文回归；不设固定重试次数或统一自动暂停规则。

## 落地与许可

建议在 game-playloop-validation 的 input-text-evidence 专项旁增加按需“重绑定恢复”中英文参考，入口只做轻量路由。有效性以坏配置检出、实际重启恢复、真实设备中断测试为准。源仓库为 Unity Companion License，样例还涉及第三方许可；仅原创方法总结与链接，不复制代码、UI、美术或资产，根 MIT 不重新许可上游。

## English procedure

Use only for existing or authorized rebinding/device-support work. Track stable action/binding identifiers, defaults, overrides, resolved controls, displayed prompts, configuration version and user ownership. Do not use collection indexes or session-only device IDs as persistent identity. Separate reading, structural validation, identifier/type matching, application and recovery; preserve a recoverable configuration before mutation. A structurally valid configuration can still resolve to no controls; inspect that result and actual input, not only a successful load return. Unknown bindings need the project's migration, warning or fallback policy, not silent success.

Define whether composite rebinding commits per part or as one transaction. Test cancel, closing and disabling separately; restore the prior input context rather than enabling every action map indiscriminately. Validate save/restart with both old and new controls; test stale identifiers and malformed input. During device loss/reconnection, distinguish action cancellation from release-triggered gameplay and verify UI prompts against actual resolved controls. Do not erase durable player preferences merely because one device temporarily disconnects.

These are source-based test designs, not executed Unity or hardware tests. The pinned public repository is a development snapshot, not a released package or the complete current implementation for all Unity versions. The older versioned manual is a mechanism comparison only. Upstream code/assets are not included and retain their own licenses.
