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
