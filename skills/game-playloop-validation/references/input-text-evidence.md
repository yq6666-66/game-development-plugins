# 输入语义、文字系统与中间态证据

[English](input-text-evidence.en.md)。仅在多绑定、重绑、多语言/文字输入或多步链排错时读取；不要求项目新增这些系统。以下为静态资料蒸馏，非已运行实现。

## 动作合同

明确 held / pressed / released、轴阈值以及物理绑定如何聚合。两个键映射同一动作时，按住第一个再按第二个，是整个动作仅触发一次，还是每个绑定独立触发？沿用玩法要求，不假定某种永远正确。

重绑应隔离打开提示的输入，处理取消、冲突与恢复；绑定变化后重新采样 held，不凭空生成 pressed。设备提示由有意义输入切换，过滤漂移/偶然移动；清除瞬时输入不等于清除有意保留的物品选择。断开设备是否暂停、缓冲使用哪个时钟，要结合联网、暂停与规则合同确定，不统一套用。

最小检查：同动作双绑定交叠按下；重绑取消/冲突/恢复；设备切换。分别记录动作次数、实际绑定和提示，不只看截图；只测试项目支持的设备。

## 中间态与画面对齐

多步链分别检查输入、已提交状态、显示与下一动作。例如取钥匙→开门→出口，最终成功不能掩盖重复奖励。诊断快照若已有或获准添加，应读取真实状态，不维护另一套模拟或打印期望答案。

将版本、场景、tick/帧标签和状态关联到对应画面。未绘制的 tick 标缺图，不能给后续截图贴旧状态。受控推进只有一个模拟推进者，不能测试循环与正常循环重复更新。动作分发只证明动作层，设备到动作层另验。诊断不暴露秘密、隐藏玩家信息或未经授权的个人数据。

反例：状态正确但 HUD 延后一帧时，同 tick 证据应保留差异，不用最终截图掩盖。不要求所有任务安装调试接口。

## 按实际文字系统验证

仅覆盖项目支持的语言/文本功能。用实际字体、译文和窄框检查缺字、混排、长无空格串、字素簇及必要的字形塑形；按空格拆行和按码点打字不适用于所有文字。打字机按字素簇推进，并保持预先排好的行稳定，具体塑形和测量由实际文字库验证。

完整句子和占位符应容许词序变化；明确缺翻译回退，原语言不一定英语。文本输入另测 IME 组合、提交、取消，不以按键事件代替。动态数值检查如 9→10、99→100 及项目实际本地化格式；不要把固定扩容比例当通过标准。

## 固定来源与边界

来自 gamedev-skills/awesome-gamedev-agent-skills 固定提交 c6ca6c41c839b68319ffc08430b99ab768debc32，本轮全文读取：
- [输入](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/c6ca6c41c839b68319ffc08430b99ab768debc32/skills/ebitengine/ebitengine-game/references/input.md)
- [诊断](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/c6ca6c41c839b68319ffc08430b99ab768debc32/skills/ebitengine/ebitengine-game/references/playtest-diagnostics.md)
- [文字](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/c6ca6c41c839b68319ffc08430b99ab768debc32/skills/ebitengine/ebitengine-game/references/text-and-ui.md)
- [布局](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/c6ca6c41c839b68319ffc08430b99ab768debc32/skills/disciplines/game-ui-ux/references/layout-and-flow.md)
- [输入缓冲](https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/c6ca6c41c839b68319ffc08430b99ab768debc32/skills/disciplines/input-systems/references/buffering-and-accessibility.md)

使用自己的话归纳，不复制 API 示例；Ebitengine 的代码不是跨引擎接口。本轮未运行来源或目标游戏，固定快照不代表最新上游。
