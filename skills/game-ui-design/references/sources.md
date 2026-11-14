# 来源与取舍 / Sources and decisions

读取 / Read: 2026-11-14。原创流程综合，不复制示例脚本、图片或原文；第三方许可保持独立。
Original synthesis; no example scripts, images or source prose copied.

- Godot Engine contributors，`c5b3485cb4b6e14ae3d8a45271bcddac7caad66a`：[Keyboard/Controller Navigation and Focus](https://github.com/godotengine/godot-docs/blob/c5b3485cb4b6e14ae3d8a45271bcddac7caad66a/tutorials/ui/gui_navigation.rst) 与 [Size and anchors](https://github.com/godotengine/godot-docs/blob/c5b3485cb4b6e14ae3d8a45271bcddac7caad66a/tutorials/ui/size_and_anchors.rst) 完整正文，[许可 CC BY 3.0](https://github.com/godotengine/godot-docs/blob/c5b3485cb4b6e14ae3d8a45271bcddac7caad66a/LICENSE.txt)。文档说明初始焦点、隐藏失焦、显式邻接与按父控件定位。借鉴的是设计约束，Godot Control API 不成为其他引擎操作指令。
- Godot Engine contributors，[ActionRemapButton.gd](https://github.com/godotengine/godot-demo-projects/blob/b761b4cd5718a7118f2c95eb55f181d0a5f004f1/gui/input_mapping/ActionRemapButton.gd)，完整文件与 [MIT许可](https://github.com/godotengine/godot-demo-projects/blob/b761b4cd5718a7118f2c95eb55f181d0a5f004f1/LICENSE.md)已读。示例在映射结束恢复焦点，也明确不支持绑定 Enter；不能据此声称所有按键、手柄与取消流程完整。

The documents explain initial focus, hidden-control focus loss, explicit neighbors and parent-relative placement. The remapping sample restores focus but excludes Enter binding. These are versioned examples, not a universal UI framework or completeness claim.

信息层级、屏幕契约和焦点恢复样本为本项目综合建议。未观看文档图片或运行示例，未完成引擎、真机或用户测试。
Information hierarchy, screen contracts and fallback-focus examples are our synthesis. No image inspection or example execution; no engine, hardware or user test.
