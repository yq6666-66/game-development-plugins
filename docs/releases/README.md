# 受控 GitHub 自动发布

[English](README.en.md)

此流水线仅发布 GitHub Release，不提交官方商店，不自动合并。`distill/*`、`weekly/*` 和其他分支不触发发布。新增流水线本身也不触发发布；本目录故意没有可执行审批 JSON。

## 流程

1. 在候选分支更新两个插件清单版本、CHANGELOG 和相关文档，完成代码审阅后按项目权限合并。确定已在 `main` 的完整源提交 SHA。
2. 对该**准确提交与版本**进行 Codex、Claude 的隔离安装、真实技能调用、更新、卸载验收，记录环境、宿主版本、输入与观察。不能以包结构检查、模拟调用、作者声明代替。记录验证平台，不推断其他平台。完整平台支持范围由本次批准方案确定；如果计划要求 Windows 等多平台，应在每项证据中完整记录，不得仅填写一个已测平台掩盖缺口。
3. 用该提交构建白名单 ZIP，记录 SHA256。将验收日志保存到 `docs/validation/`；每项记录绑定同一源 SHA/版本并计算文件 SHA256。
4. 审阅人核实证据和发行范围。在后续 `main` 提交中**只新增一个** `docs/releases/approvals/X.Y.Z.json`（可伴随相关文档），结构见下方。新增审批记录的 main push 自动启动检查、构建和发布。不需要每日反复确认已授权事项，但不能自动虚构验收或把研究成果当正式版本。审批目录是信任边界，写入 `approved: true` 必须以实际审阅批准为依据。
5. 只读作业验证记录、版本、main 祖先关系、逐文件摘要，重新在隔离 worktree 运行现有校验/测试/构建并比较批准 ZIP 摘要。仅成功后进入 `contents: write` 的发布作业。发布作业不运行待发布提交里的构建代码，只运行事件提交中的发布器。
6. 发布器拒绝任何同名 tag、Release 或 draft；原子创建绑定源 SHA 的 tag，创建 draft，上传 ZIP/校验和/发行说明，核对 GitHub 返回的每份资产摘要与大小、再次核对 tag，再公开。GitHub 未提供摘要、API 失败、权限不足均失败关闭。

## 审批结构（示例不是验收证据）

```json
{
  "version": "0.2.0",
  "source_sha": "完整40位源提交SHA",
  "artifact_sha256": "实际64位ZIP摘要",
  "approved": true,
  "scope": "github-release",
  "reviewer": "实际审阅人",
  "approved_at": "实际审阅时间",
  "evidence": {
    "codex-install": {
      "path": "docs/validation/本版本-codex-install.json",
      "sha256": "该文件实际64位摘要",
      "source_sha": "同一个完整源提交SHA",
      "version": "0.2.0",
      "status": "PASS",
      "host_version": "实际宿主版本",
      "platform": "实际验证平台",
      "date": "实际验证时间",
      "input": "可复现输入或日志定位",
      "observed": "实际观察或日志定位"
    }
  }
}
```

`evidence` 必须同时包含 `codex-install`、`codex-invoke`、`codex-update`、`codex-uninstall`、`claude-install`、`claude-invoke`、`claude-update`、`claude-uninstall`。示例为避免虚构证据只展示一项。每项需指向结构化证据 JSON：主体必须重复并匹配 `source_sha`、`version`、`status`、`host_version`、`platform`、`date`、`input`、`observed`；另需 `operation` 等于该项名、`mode: actual-host-runtime`、`artifact_sha256` 匹配批准包，以及 `log: {"path": "docs/validation/实际日志.txt", "sha256": "实际日志摘要"}`。更新两项还需 `update_scope: remote-candidate-end-to-end`，即从隔离远端候选来源到宿主的真实更新，不是本地目录合成版本测试。门禁核对证据主体和日志摘要，但不能自动鉴别日志真实性。字段非空不是证据真实性的自动证明，人工审阅仍是信任来源。0.1.0 的已批准单次跳过不适用于后续版本；流水线拒绝重发 0.1.0，也拒绝预发布版本、缺项和 SKIPPED。

## 权限与恢复

- 使用 GitHub 内建临时 `GITHUB_TOKEN`；默认只读，仅发布作业 `contents: write`。不创建 PAT，不改变仓库 Actions 设置或保护规则；若组织策略阻止执行，报告阻塞后由所有者决定，不能绕过。
- 第三方 Actions 固定完整提交 SHA；升级需重新核对官方来源。
- 新版本还须大于所有现有稳定版本和正式版 draft 的 SemVer；公开时明确设为 latest。
- 同仓库发布串行，不取消进行中的发布。运行重试若发现 tag/draft，拒绝继续；不会覆盖、清理或移动历史引用。
- 若失败时已生成 tag/draft，这意味着失败也可能已有公开 tag（不是零远端副作用）；保留现场与日志，由维护者核对已上传内容后另行批准恢复。不通过删标签重跑规避检查；本流水线不实现自动回滚或补传。
- 资产摘要核对发生在公开前；成功响应确认 tag 和公开状态。GitHub API 返回的摘要是服务端验证证据，并非下载到用户设备的端到端安装验证。
- 不保证官方目录上架、远端宿主升级传播或游戏引擎兼容；它们需独立证据。

## 本轮检查边界与来源

见[2026-11-15 候选验证](../validation/guarded-release-2026-11-15.md)。尚未在真实 GitHub Actions 执行，未为测试创建任何 tag/Release，也没有更改仓库权限。

核对的官方资料（2026-11-15）：[GITHUB_TOKEN](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token)、[安全使用 Actions](https://docs.github.com/en/actions/reference/security/secure-use)、[Release REST API](https://docs.github.com/en/rest/releases/releases)。固定 Actions 的 v4 引用通过官方仓库 `git ls-remote` 核对。MIT 不改变上游 Actions 许可。
