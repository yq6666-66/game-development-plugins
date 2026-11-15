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

## 补充：双宿主本地合成跨版本测试

独立核验者建立独立插件副本和隔离宿主配置，先安装副本版本 0.1.0，再仅把该副本的两份 plugin 清单改为 **测试用 0.1.1**。仓库正式清单及发行包仍为 0.1.0；这不是正式 0.1.1 发布。

- Codex：再次执行 `plugin add game-development-plugins@game-development-plugins`，返回 0.1.1 安装缓存；新 app-server 的 `skills/list` 发现全部 7 技能，路径均在 0.1.1 缓存且 errors=[]。这是本地目录重新安装路径，不是 marketplace upgrade 或远程更新传播测试。
- Claude Code：`plugin update game-development-plugins@game-development-plugins` 明确返回从 0.1.0 更新至 0.1.1；list 与 details 核对 0.1.1 和全部 7 技能。
- 两端测试后卸载，列表均为空。未登录或发模型请求。执行环境和宿主版本沿用上述 Linux 隔离测试。

归档：[Codex 0.1.0 安装](dual-host-plugin-2026-11-15/synthetic-upgrade/codex-install-010.log)、[0.1.1 重新安装](dual-host-plugin-2026-11-15/synthetic-upgrade/codex-reinstall-011.log)、[列表](dual-host-plugin-2026-11-15/synthetic-upgrade/codex-list-011.log)、[技能发现](dual-host-plugin-2026-11-15/synthetic-upgrade/codex-skills-011-filtered.json)、[卸载后](dual-host-plugin-2026-11-15/synthetic-upgrade/codex-list-after-remove.log)；[Claude 0.1.0 安装](dual-host-plugin-2026-11-15/synthetic-upgrade/claude-install-010.log)、[初始列表](dual-host-plugin-2026-11-15/synthetic-upgrade/claude-list-010.log)、[更新](dual-host-plugin-2026-11-15/synthetic-upgrade/claude-update-011.log)、[新列表](dual-host-plugin-2026-11-15/synthetic-upgrade/claude-list-011.log)、[新详情](dual-host-plugin-2026-11-15/synthetic-upgrade/claude-details-011.log)、[卸载后](dual-host-plugin-2026-11-15/synthetic-upgrade/claude-list-after-uninstall.log)。日志处理规则同上，仅替换隔离路径与筛除无关宿主信息。

本补充把**本地合成升级**状态更新为 PASS。此前升级未验证记录保留原时间范围。**远程 Git/目录传播、降级回滚、真实任务调用、Windows、正式发布与官方上架仍未验证或未执行**；不得将本测试外推为这些项目通过。

## 补充：Windows 隔离安装与用户选择跳过真实调用

同日 Windows 实测由连接该电脑的核验者执行并报告。本记录依据其实际执行报告；Windows 原始文件仍保存在本机独立证据目录，未把未取得的原始日志冒充为本仓库附件。公开记录不包含个人目录或凭据。

| 项目 | 结果 |
| --- | --- |
| 候选包传输和完整性 | PASS；通过获授权 Library 传输，SHA256 与本文 r2 候选完全一致 |
| Windows Codex 0.146.0 隔离安装 | PASS；新 CODEX_HOME 内添加本地 marketplace 并安装，plugin list 显示 version=0.1.0、installed=true、enabled=true |
| Windows Codex 真实技能读取/任务调用 | BLOCKED 后按用户选择跳过；未能安全组合隔离插件配置与已有登录，不能认定技能读取或任务通过 |
| Windows Claude Code 2.1.167 | 登录状态 loggedIn=false、authMethod=none；未尝试登录；真实任务按用户选择跳过 |
| 游戏运行 | 未运行；不属于本轮插件封装实测 |

核验者执行的安装步骤（路径占位符只指独立证据目录）：

```powershell
$env:CODEX_HOME = '<EVIDENCE_ROOT>\isolated-codex'
codex plugin marketplace add '<EVIDENCE_ROOT>\candidate'
codex plugin add game-development-plugins@game-development-plugins
codex plugin list --json
```

执行结束恢复原 CODEX_HOME；未复制登录凭据、未修改个人配置或游戏工程。本机证据文件名为 `codex-plugin-list.json` 与 `HOST-TEST-RESULT.txt`，保留候选包及隔离配置以供后续检查。GitHub 下载受策略阻止后使用已授权 Library 传输，未绕过策略。

**用户明确选择不再等待登录和两端真实任务调用。该选择记录为 SKIPPED，不是 PASS，也不等于批准把原完整验收门槛视为已满足。** 后续不自动重试登录或调用。两端模型真实任务及 Windows Claude 安装/调用验收仍不完整；正式发布、官方上架和主分支合并未执行。本条只更新验证状态，发行包未变。

## 发布范围确认

用户随后明确批准将当前候选合并并按现状发布 0.1.0，已知真实任务调用跳过及其他未验证限制。本次属于明确接受有限验证范围的发布，不把历史 SKIPPED/BLOCKED 改成 PASS，不追认先前完整验收通过。最终主分支提交和发行资源由发布结果核对。
