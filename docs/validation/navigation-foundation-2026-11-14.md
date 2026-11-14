# 导航与学习入口增量 / Navigation foundation

日期 / Date: 2026-11-14。环境 / Environment: Linux workspace, Python 3。

## 基线与范围 / Baseline and scope

- 默认分支 `main`，基线 `48915481118f7886a02ad2e7dea089436953186b`。
- 独立分支 `docs/bilingual-navigation-foundation`；不合并、不发布，不修改游戏。
- 已读取 README、CHANGELOG、兼容性、来源、验证、项目约定、两项 SKILL 与包校验器。
- `refactor/general-public-v3` 已并入基线；`planning/visual-improvements` 和 `skills/game-visual-iteration` 仍有非祖先提交。检查提交历史及差异范围，包含旧项目规划、旧 Skill 与图标；未将旧私有项目内容或未知授权图标重新引入公开包。
- 改动：首页中英双入口、八类导航、从零/接手流程、蒸馏入门与模板、推荐记录格式、未来作品投稿说明。没有新增正式 Skill 或具体工具推荐。

The increment adds bilingual entry and learning documents, not new executable integrations. Existing Skill paths, contents, tests, validator, license and historical audit/validation evidence remain unchanged. The old README's candidate wording is superseded; historical records retain their original scope and dates.

## 实际命令与结果 / Commands and results

```sh
git branch -r --no-merged main
git log --oneline main..origin/planning/visual-improvements
git log --oneline main..origin/skills/game-visual-iteration
python3 scripts/validate_package.py
python3 -m unittest discover -s tests -v
git diff --exit-code -- skills tests scripts docs/VALIDATION.md docs/audits LICENSE
git diff --check
```

- PASS：现有包结构校验；六项单元测试，包括负向测试。
- PASS：保护项与基线无差异。历史证据没有修改。
- PASS：本次全库 91 条 Markdown 本地文件链接与使用的标题锚点检查；首次运行发现待创建的两条验证报告链接，补齐本文件后复验。检查脚本为本次工作区临时辅助，不扩展正式校验器。
- PASS：独立只读内容复核覆盖中英首页及四组新文档，未发现阻断问题；审阅时待补的报告链接已创建并复验。
- 情境检查：新原型可从目标和可撤销假设进入；接手项目先读取真实基线；资源页不是已验证推荐；作品页不虚构已完成游戏；八类不冒充八项 Skill。

## 未验证 / Not verified

外部链接可用性全量检查、宿主发现/安装、Unity/其他引擎/浏览器游戏执行、真机输入、画面和性能均未运行。本轮文档检查不增加引擎兼容性或游戏运行证据。不修改或证明定时任务运行状态。未创建发布或合并到主分支。

The existing historical validation remains in `docs/VALIDATION.md`; its prior authorization checklist is a dated record, not the current branch status. Future additions require their own evidence.
