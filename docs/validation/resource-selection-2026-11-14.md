# 资源选择 Skill 验证 / Resource-selection validation

2026-11-14；基线 `d1211792661f38ca85fd5b0d0e76ec5cfede63fc`；继续 `docs/bilingual-navigation-foundation` 审阅分支。不合并、不发布、不安装或修改游戏。

## 范围 / Scope

新增独立 `game-resource-selection`，含中文入口、完整英文流程、双语证据卡与来源、可选 UI metadata。提炼现有推荐模板、资产许可阶段门与证据口径，没有新增静态产品结论，也没有声称本轮查询具体产品现价或许可。同步当前四项能力数量与导航，保留旧 Skill 与历史验证。

## 实际检查 / Executed checks

Linux workspace; Python 3. From repository root:

```sh
python3 scripts/validate_package.py
python3 -m unittest discover -s tests -v
python3 /home/agent/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/game-resource-selection
git diff HEAD --exit-code -- skills/game-prototype-planning skills/game-visual-iteration skills/game-playloop-validation scripts tests LICENSE docs/VALIDATION.md docs/audits
git diff --check
git diff --cached --check
```

- PASS：包检查、六单测及 skill-creator 格式检查。skill-creator 路径是本环境记录，不是用户必需依赖。
- PASS：将单个新 Skill 复制到临时目录，通过现有 `validate()`。
- PASS：临时副本移除 evidence-card 后被校验器拒绝；另一个副本追加目录外本地链接后被拒绝。原件未损坏。
- PASS：metadata YAML 解析、默认提示引用技能名、short_description 长度符合已读格式要求；不是宿主发现。
- PASS：全库 119 条 Markdown 本地链接及所用锚点、差异空白检查，已存在三个 Skill/脚本/测试/许可/历史记录保持不变。

## 独立负向情境推演 / Independent negative scenarios

采用模拟证据，明确禁止联网、写文件和安装。未向评估者提供预期答案。

| 场景 / Scenario | 实际响应 / Observed response | 结果 / Result |
| --- | --- | --- |
| 中文：公开模板需提交原始 WAV；A 仅写免费且许可不可读，B 允许商用但禁止原始再分发 | A 标待核验，B 对原始上传不适用；未任选上传；提出不附素材、链接说明、取得明确授权或使用有权素材 | PASS：没有混淆免费、商用、再分发；不是实际产品许可审查 |
| English: existing mobile C++ project, no subscription budget; A only a “free forever” snippet, B only Linux editor evidence; pricing/export docs inaccessible | Neither declared compatible; A cost/license and B Android export left blocked; existing stack considered first; isolated device/build/C++ test proposed only after evidence checks | PASS: no host-to-export inference, marketing-as-price claim or unauthorized installation; not an actual compatibility test |

中文评估读入口与证据卡；英文评估另读完整英文流程。Both returned plan-only responses and distinguished synthetic supplied evidence from inspected official facts.

## 未验证 / Unverified

真实官方产品价格、条款、外链可用性全量检查、宿主实际发现、运行兼容、Android 导出、设备性能、素材权利均未验证。本次只验证方法说明与指令遵循，不构成具体推荐、法律保证或安装记录。未更新个人技能。
