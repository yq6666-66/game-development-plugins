# 七项 Skill 小步优化 · 2026-11-14

## 基线与选择

基线 main：`8693e66d50f40b70f95fec3f77f3a0322ef08eb3`。新分支 `improve/skill-contracts-2026-11-14`。修改前保留 Git bundle；没有修改旧研究分支或主分支。

逐项阅读七个入口及相关引用与包校验器：

| Skill | 本轮判断 |
| --- | --- |
| game-prototype-planning | 已有完整英文流程；保留现有假设/决策边界 |
| game-resource-selection | 已有英文与费用/许可边界；不新增未核验榜单 |
| game-visual-iteration | 缺完整英文主流程，本轮补齐 |
| game-playloop-validation | 缺完整英文主流程，本轮补齐 |
| game-engineering | 中文“依赖已存在才使用”较英文更强，可能阻断获准的新建工程；统一为优先复用，新增按授权 |
| game-ui-design | 已有英文状态/焦点/布局流程；本轮不追加重复清单 |
| game-build-delivery | 已有版本/缓存/产物/启动分层；本轮不扩平台 |

另复现包校验器缺陷：`[Details][guide]` 加 `[guide]: references/missing.md` 的缺失文件，在基线校验器得到空错误列表；修改后实际得到 `missing reference`。复制包测试复用同一校验器，原先无法发现此语法遗漏。

## 实际修改与许可

新增两项英文核心流程，保留按需引用；并不承诺全部专项/历史参考都已翻译。工程中英依赖措辞同步。所有内容依据本仓库既有原创 MIT 方法改写，不复制第三方代码。

校验器支持有边界的引用语法：同文档单行无标题定义、full/collapsed 与已有定义的 shortcut、大小写及空白归一；重复定义是本仓库拒绝的歧义，而不是宣称 CommonMark 必须拒绝。排除 fenced/inline 代码示例。支持范围与明确不支持的语法见 [兼容性](../COMPATIBILITY.md)。不是完整 Markdown 解析器，也不验证标题锚点和外部网站可访问性。

此前 NVIDIA/elements 性能候选本轮重新阅读固定提交 `1417043282f5c4262c24b837e31a7ebda26930e7` 的 `performance-diagnostics.md` 与 Apache-2.0 根许可，但未纳入正式改动：优先修复已实际证明的本地缺陷，而非堆叠额外清单。没有运行该上游项目。

## 真实命令与结果

```sh
python3 scripts/validate_package.py
python3 -m unittest discover -s tests -v
python3 <installed-skill-creator>/scripts/quick_validate.py skills/<each-skill>
git diff --check
```

- 包校验 PASS；20 项单元测试 PASS（基线 11 项，新增 9 项语法/反例测试）。
- 七个独立目录的 quick_validate PASS；已有临时目录复制测试覆盖全部七项。
- 差异检查 PASS。
- 对基线/新校验器运行同一临时缺文件夹具，确实得到 false PASS → 报错；不是仅检查固定文案。
- 新增回归覆盖：有效 full/collapsed、缺文件、越界、缺定义/重复定义、代码示例、shortcut 与普通方括号、外部地址/片段。

## 结论边界

文档/源码审阅与纯 Python 包测试已执行。未运行宿主模型加载、游戏引擎、游戏、目标设备、图形性能或真实玩家测试。20 项测试不代表 Skill 行为已被 Agent 实测。没有新增 Skill，仍为七项；没有安装上游依赖、合并、发布或删除分支。远端提交/内容树应在推送后另行核对，不把本地成功等同远端成功。

## 独立审阅后的修正

审阅补充了跨行 code span 和转义开括号两类误报。新增两项回归测试，覆盖相同长度反引号、未闭合反引号、单数/双数反斜线；排除代码示例，保留真实链接检查。仍不是完整 CommonMark 解析器。独立审阅确认两项英文流程的关键权限、正常输入及静态/运行证据边界一致。
