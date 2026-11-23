# 动作提示不能只看设备图标

[English](action-glyph-contract.en.md)。用于已有输入提示任务；不要求接入 Steam、换输入系统或下载素材。

## 诊断与最小验证

先记录“玩家/控制器→当前动作上下文→有效绑定来源→文字/图标→实际触发结果”。设备型号只能帮助选择美术风格，不足以证明某动作的绑定。特别是仿真输入，游戏看到的逻辑设备可能不是玩家拿的设备。

对无来源、多个来源、未知来源或图像加载失败分别定义提示策略；不要无条件取数组第一项，也不要把未知枚举值直接作为自制图集下标。按项目既定策略选主要提示、显示多个提示或可理解的文字后备，不凭猜测画一个熟悉按钮。

在获准样本中走正常动作、上下文改变/重绑定后刷新，再检查支持范围内的设备变化。隔离夹具可提供零来源和超出自制图集范围的来源，检查不会越界或显示误导图标。夹具通过只证明该分支处理，真实控制器输入、实际来源映射和图像解码须另测。记录动作结果和可见提示，而非仅截图。

## 官方来源事实与限制

Valve [Steam Input Gamepad Emulation - Best Practices](https://partner.steamgames.com/doc/features/steam_controller/steam_input_gamepad_emulation_bestpractices)，读取 2026-11-17 的 Gamepad Emulation、Showing device specific art、Future-Proofed Glyphs、Own Art 两节及示例（网页正文约359–407行）。说明仿真设备、按来源查图与未知来源后备；旧示例接口名不能直接当当前推荐。

Valve [ISteamInput](https://partner.steamgames.com/doc/api/ISteamInput)，同日只读 GetDigitalActionOrigins、GetGlyphForActionOrigin_Legacy、GetGlyphPNGForActionOrigin、GetGlyphSVGForActionOrigin、GetInputTypeForHandle（约583–672行）。来源查询带控制器/动作集/动作，返回来源数量；来源枚举可能超过编译时SDK范围；旧取图接口已标Legacy，文档推荐PNG/SVG接口。页面动态、未给定SDK版本，本轮未读SDK源码、未安装或调用Steam、未验证设备。实际API以项目锁定SDK为准。

上面的来源链、零来源策略与反例流程是原创综合，不是上游示例已证明存在缺陷。仿真路径和原生Steam Input路径不可混用。只保留链接和改写，不复制Valve图像或代码，不声称其资源可按本仓库MIT再分发。接入与设备矩阵有成本；无此输入需求时跳过。
