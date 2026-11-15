# 游戏开发插件：安装与使用

[English](PLUGIN-README.en.md)。候选版本 0.1.0；共享七项 Skills，同时提供 Codex portable manifest 与 Claude Code manifest。不是 Unity 编辑器扩展。未经两端实际调用验证，不宣称全面兼容。

## 安装前

需要支持插件的 Codex 或 Claude Code。模型服务、账号和组织策略由宿主负责，可能另有费用。本包无 MCP、hooks、后台进程、遥测或密钥。不覆盖手动安装的同名技能；先记录已有安装位置和版本，在隔离项目验证，确认无重复后再选择保留哪一种安装方式。不要自动删除用户原有文件。

从候选 ZIP 解压到独立目录（下文 `./game-development-plugins`），或使用已审核的仓库版本。目录须包含根 `plugin.json`、`.claude-plugin/` 和完整 `skills/`；不要只复制 manifest。

## Codex

先用 `codex --version`、`codex plugin --help` 确认当前客户端支持命令。示例在解压目录的父目录执行：

```sh
codex plugin marketplace add ./game-development-plugins
codex plugin add game-development-plugins@game-development-plugins
codex plugin list
```

目录来源使用本包 `.agents/plugins/marketplace.json`。启动新的 Codex 会话，明确要求使用 `game-prototype-planning`，检查宿主确实读到对应 SKILL.md，而不只是列出名称。不同客户端 UI、组织权限和版本可能不同；安装返回成功不等于模型调用通过。

## Claude Code

本地开发试用：`claude --plugin-dir ./game-development-plugins`。正式安装目录来源：

```sh
claude plugin validate ./game-development-plugins
claude plugin marketplace add ./game-development-plugins
claude plugin install game-development-plugins@game-development-plugins
claude plugin list
```

开启新会话，调用 `/game-development-plugins:game-prototype-planning`。按当前宿主可用命令查看组件清单，确认七项且无重复。默认 `skills/` 自动扫描，manifest 不重复声明它。

## 按需使用

| 目标 | Skill |
| --- | --- |
| 从零规划小原型 | [game-prototype-planning](skills/game-prototype-planning/SKILL.md) |
| 工程与模块职责 | [game-engineering](skills/game-engineering/SKILL.md) |
| 工具、引擎和资源选择 | [game-resource-selection](skills/game-resource-selection/SKILL.md) |
| 画面改进和证据 | [game-visual-iteration](skills/game-visual-iteration/SKILL.md) |
| 输入、存档与重开 | [game-playloop-validation](skills/game-playloop-validation/SKILL.md) |
| 一屏信息与交互 | [game-ui-design](skills/game-ui-design/SKILL.md) |
| 构建及本地交付 | [game-build-delivery](skills/game-build-delivery/SKILL.md) |

从零样例：“只规划一个已获准的新游戏原型，列出输入、结束、重开及验证办法，不写代码。”

接手样例：“只读检查隔离示例工程的视觉资料，列出基线、参考迁移与同机位对比计划，不修改工程。”

排错样例：“调查重开后事件重复的生命周期，先给证据和最小修复计划。”这些任务不授权安装外部工具、上传私人资料或发布游戏。

## 更新、停用、卸载与回滚

先保留旧版本包、版本号、用户本地修改及配置。将新包解压到新目录，复跑检查和隔离调用；按宿主当前官方更新机制刷新市场及插件，重开会话验证，不能只更新市场索引就认定插件已更新。Codex 有 `codex plugin marketplace upgrade`；具体版本是否还需重新安装应以 `--help` 和安装结果为准。Claude 使用当前 `claude plugin update` / marketplace update 流程，先查 `--help`。

卸载本插件：`codex plugin remove game-development-plugins@game-development-plugins` 或 `claude plugin uninstall game-development-plugins@game-development-plugins`。不手动清空宿主整个缓存或配置。市场移除是独立动作，仅在不再使用它时通过宿主命令处理。回滚时安装保留的旧包并再次验证；不要覆盖用户工程。

名称重复先查旧手动 Skills；参考缺失重新核对完整包；命令不可用核实版本；权限被组织阻止应联系管理员，不绕过。包结构通过、安装发现通过、模型实际调用通过是不同状态。

## 许可与维护

原创内容 [MIT](LICENSE)，第三方资料许可独立。每日研究、每周整合；只有通过约定验收的更新才进入发布步骤。源码分支、候选 ZIP、自建市场和官方目录上架并非同一状态。官方上架可能需账号、审核和条款，不保证自动获批。

Claude Code 的自建 marketplace 自动更新默认关闭；发布新包不代表用户已自动更新，需核对宿主设置与已安装版本。
