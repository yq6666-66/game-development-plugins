# 工程与 UI 两项 Skill 建设 · 2026-11-14

## 基线与范围

基于 main `becd721c27c01ef571b3c6a9886019593291bea5`，分支 `feat/engineering-and-ui-skills`。修改前保存完整 Git bundle，原主分支与旧分支不动。本分支仅新增工程与 UI 两项正式 Skill，从四项变为六项；构建 Skill 另行处理，具体产品推荐目录仍待核验。附件由协调线程查看为八类导航，本实施依据仓库真实缺口；本线程 Library 读取未返回像素，不宣称自己审图。

新增入口独立性：工程 Skill 负责组装、所有权与授权内架构切片；UI Skill 负责信息与界面转换设计；原玩法 Skill 保留已有流程的验证职责。两项均带目录内完整英文流程、必要参考与固定来源，不需要安装其他 Skill。

## 来源核对

实际读取 Godot 文档 commit `c5b3485cb4b6e14ae3d8a45271bcddac7caad66a` 的 scene_organization、gui_navigation、size_and_anchors 全文与 LICENSE.txt（CC BY 3.0）；Godot demo commit `b761b4cd5718a7118f2c95eb55f181d0a5f004f1` 的 ActionRemapButton.gd 全文及 MIT LICENSE。未运行例子，也未看配图。

OpenAI plugins `d420d13051bffe4543ed39e30fa46b87148e47dd` 的 web-game-foundations 入口全文已读；根及 game-studio 清单未见许可，保留为未复用的线索，不搬运内容。过滤其固定引擎偏好、DOM/GLB默认值。所有来源链接和取舍保留在每项 Skill 的 references/sources.md，方法为原创综合，非逐段翻译或源码再分发。

## 验证

实际执行：

```sh
python3 scripts/validate_package.py
python3 -m unittest discover -s tests -v
python3 /home/agent/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/game-engineering
python3 /home/agent/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/game-ui-design
git diff --check
```

- PASS：包检查、11 项单测、两项 frontmatter 检查、差异空白检查。
- 新增测试实际复制每项 Skill 到不含外层文档的临时根后验证；另删除副本英文参考，确认被校验器检测。仅临时副本受损，原件不变。
- 协调线程独立纸面检查：已有问题先复现、不强制重构；纯设计不创建工程；输入覆盖按项目声明；未知玩法不擅自新增；设计、实现和运行证据分开。
- 未验证：Agent宿主实际加载与执行、Godot/其他引擎、真实游戏、画面/设备与用户可用性。纸面检查不是盲测或运行通过。
- 远端内容核对及 CI 状态在提交后另行报告；此记录不是 CI PASS。

## 后续

可在获准的实际项目任务中分别试用一条工程切片与一屏 UI。缺失环境先输出可执行计划与具体阻塞，不能把导航完整度当作实际游戏能力证明。合并、发布由用户另行决定。
