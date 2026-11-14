# 八类导航与 GitHub 研究整合 · 2026-11-14

本次按用户“合并”指令整合两个已交付分支，不删除分支、不发布版本。

- 基线 main：`cc09648da6774850f1d76e74ec9be346acee31da`
- 八类导航：`3856418552f4f3b412592bbdcfaec0cb4ed248a3`
- GitHub 研究：`81f6ecefcda455df9710ea7b3c776bea3a169358`

## 合并与检查

两个分支均无内容冲突；保留双方中英文入口、16 个分类页、异步与状态分歧参考、历史研究和验证记录。正式 Skills 仍为四项。旧游戏专属分支不在此次范围。

在 Linux 工作区最终整合内容上执行：

```sh
python3 scripts/validate_package.py
python3 -m unittest discover -s tests -v
git diff --check
```

结果：包检查 PASS、9/9 单元测试 PASS（含三项导航检查）、差异检查 PASS。没有宿主加载、上游工具、引擎、游戏或真机实测；这些结果不代表 CI 通过。远端提交与本地已测试内容树另行核对后报告。

本记录保留前次研究的原日期与验证范围，不把历史待合并文字追溯改成当时已合并。
