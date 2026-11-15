# 双宿主插件候选验证 · 2026-11-15

基线：`main`，`890e87292294f3b66e0d1203c4debd58910531db`。结束前 `git ls-remote origin refs/heads/main` 仍返回该值。独立工作分支：`feat/dual-host-plugin`。基线提交保留所有修改前文件，原有七技能内容未改。

## 实际执行

环境：Linux、Python 3；未安装额外依赖。

```sh
python3 scripts/validate_package.py
python3 scripts/build_plugin.py --check
python3 -m unittest discover -s tests -v
python3 scripts/build_plugin.py --output /workspace/shared/game-development-plugins-0.1.0-candidate-r2.zip
git diff --check
```

| 项目 | 结果与范围 |
| --- | --- |
| 原有技能校验 | PASS；本地文件与可携带引用检查 |
| 双清单与目录约束 | PASS；本仓库白名单结构检查，不是完整远端 Schema 验证 |
| 自动化测试 | PASS；27 项，包括确定性 ZIP、解包后再校验、7 技能、版本不一致、符号链接、输出覆盖保护、目录逃逸和两宿主 source 互换负测 |
| 差异空白检查 | PASS；`git diff --check` |
| 代码独立审阅 | 已修复审阅发现的 Windows 默认编码风险和目录 source 类型过宽；清单读取显式 UTF-8，互换回归测试先失败后修正通过 |
| Codex 隔离安装/发现/卸载 | PASS；0.167.0-alpha.4，7 项插件技能 enabled，errors=[]，卸载后 installed=[]；见下方日志范围 |
| 宿主真实技能调用 | 未验证；结构、安装与目录发现不能替代 Agent 实际调用 |
| Claude Code | BLOCKED；环境无 Claude Code，不擅自安装 |
| 游戏/引擎运行 | 未运行；本轮只封装已有技能，不宣称游戏效果或引擎兼容通过 |
| 正式发布/官方目录上架 | 未执行；真实宿主验收与平台资格/审查尚未全部满足 |

候选包：`game-development-plugins-0.1.0-candidate-r2.zip`。
SHA256：`eab9e03f6c1fbc3bfbc82ac2c730ec318c4247cfdfbda02c21d6dbb1ab3d4c67`。

历史初版候选包保留，未覆盖；交付以 r2 为准。ZIP 只包含发行白名单与共享技能，不含研究笔记、Git 元数据或用户工程。测试使用临时目录，不修改用户现有宿主配置。

## 情境推演（不是实测调用）

1. 用户从零咨询原型：应选择 `game-prototype-planning`，先定义目标与可观察证据，不假定已存在工程或获准生成游戏。
2. 既有项目画面排错：应选择 `game-visual-iteration`，保留布局/基线、固定观察条件，不以静帧宣称操作通过。
3. 已有手工复制技能：说明保留旧目录，先在隔离配置验证插件，避免同名技能重复加载；不自动删除旧技能。
4. 发布新包但用户未启用目录自动更新：不能报告用户已更新，应检查目录刷新及已安装版本。
5. 缺少 Claude/登录/官方资格：保留候选成果，不伪造验收，也不自动安装、付费、接受未知条款或发布。

实际双宿主调用完成后应另增有时间、宿主版本、输入、输出及日志的证据，而非回写本轮为成功。

## 补充：Codex 隔离宿主实测

独立核验者使用 `codex-cli 0.167.0-alpha.4`、Debian 13 x86_64，以全新临时 `CODEX_HOME` 执行：

```sh
codex plugin marketplace add <CANDIDATE_ROOT> --json
codex plugin add game-development-plugins@game-development-plugins --json
codex plugin list --json
# codex app-server：initialize 后请求 skills/list
# params: {"forceReload": true, "cwds": ["/tmp"]}
codex plugin remove game-development-plugins@game-development-plugins --json
codex plugin list --json
```

结果：安装版本 0.1.0，installed=true、enabled=true；宿主 skills/list 实际发现命名空间下全部 7 项技能，全部 enabled=true，errors=[]。卸载后 installed=[]，独立核验者确认该版本缓存不再存在。未发起模型回合、未登录、未付费、未修改用户原有配置。

[安装](dual-host-plugin-2026-11-15/plugin-add.log)、[安装列表](dual-host-plugin-2026-11-15/plugin-list.log)、[目录添加](dual-host-plugin-2026-11-15/marketplace-add.log)、[技能发现筛选记录](dual-host-plugin-2026-11-15/skills-list-filtered.json)、[卸载](dual-host-plugin-2026-11-15/plugin-remove.log)、[卸载后列表](dual-host-plugin-2026-11-15/plugin-list-after-remove.log)。日志中的临时工作路径已替换为占位符，技能发现记录只保留本插件；其余宿主内置技能与无关环境通知不公开。PATH alias 的临时目录警告原样保留，不影响上述返回结果。

**真实技能调用、升级/降级、Windows、Claude Code 仍未验证。** 本机 alpha 实测不是最低版本或所有 Codex 客户端的兼容承诺。独立代码复核再次运行 27 项测试与分发结构检查通过。该补充仅增加证据，不改变候选发行包、不构成发布或上架。

## 补充：Claude Code 隔离宿主实测（同日后续）

上述初始记录中“环境无 Claude Code”是当时状态，历史记录保留。本次后续经授权从官方 npm 安装 `@anthropic-ai/claude-code@2.1.325` 至隔离目录；独立的 HOME、CLAUDE_CONFIG_DIR 和 npm prefix 不影响用户原有设置。已读取下列实际执行日志，并独立核对详情确有全部 7 项技能及 0 个 Agents/Hooks/MCP/LSP 组件。

| 步骤 | 状态 | 证据 |
| --- | --- | --- |
| validate | PASS with warnings | [validate.log](dual-host-plugin-2026-11-15/claude/validate.log) |
| 本地 marketplace 添加 | PASS | [marketplace-add.log](dual-host-plugin-2026-11-15/claude/marketplace-add.log) |
| 插件安装、启用 | PASS；版本 0.1.0，enabled=true | [plugin-install.log](dual-host-plugin-2026-11-15/claude/plugin-install.log)、[plugin-list.log](dual-host-plugin-2026-11-15/claude/plugin-list.log) |
| 宿主组件发现 | PASS；7 项 Skills，其余组件 0 | [plugin-details.log](dual-host-plugin-2026-11-15/claude/plugin-details.log) |
| update | 仅本地目录 no-op，不是跨版本升级通过 | [plugin-update.log](dual-host-plugin-2026-11-15/claude/plugin-update.log) |
| 卸载及目录移除 | PASS；卸载后 list=[] | [plugin-uninstall.log](dual-host-plugin-2026-11-15/claude/plugin-uninstall.log)、[plugin-list-after-uninstall.log](dual-host-plugin-2026-11-15/claude/plugin-list-after-uninstall.log)、[marketplace-remove.log](dual-host-plugin-2026-11-15/claude/marketplace-remove.log) |

验证警告：缺少 marketplace description 与官方目录 icon。另有 README 一步安装提示。这些不改变 validator 的通过结果，但**不代表已满足官方上架所有条件**。暂不为消除目录图标警告引入未确认的品牌图；description 和安装入口可随下一候选打包修订。官方目录还需安全扫描、政策审查及账号权限。本轮仅记录证据，不改既有候选包。

**未登录、未发起模型调用、未付费。真实任务调用、跨版本升级/降级及 Windows 仍未验证，正式发布和上架未执行。** 日志只替换隔离路径，没有把宿主估算 token 数当实际用量。后续重新运行的结构检查与 27 项单测不替代以上未验证项。
