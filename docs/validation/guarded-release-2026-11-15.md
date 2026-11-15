# 自动发布候选验证 · 2026-11-15

基线 `e1317d98e4d4dccd9e4f9250a20a9cb6250ca30e` 保留全部修改前文件；独立 worktree / 分支 `feat/guarded-auto-release`，不改现有发行版或技能。范围是既有双宿主方案的后续 GitHub 自动发行，不涉及商店上架、研究自动合并、凭据或权限设置。

## 实际命令与结果

- `python3 scripts/validate_package.py`：PASS。
- `python3 scripts/build_plugin.py --check`：PASS。
- `python3 -m unittest discover -s tests -v`：PASS，40 项（原27项+发布门槛与模拟API 13项）。
- `git diff --check`：PASS。
- 官方 actions/checkout、actions/upload-artifact、actions/download-artifact `refs/tags/v4` 使用 `git ls-remote` 核对完整 SHA 后固定。

## 负向与情境检查

PASS（本地自动化）：缺少 Claude 真实调用项、SKIPPED、结构结果冒充运行结果、旧版本/旧提交证据、摘要篡改、目录逃逸、预发布/注入版本、无批准、非 main 祖先、已有tag/draft、资产摘要不符，以及上传失败后不公开。成功路径是 mock API，不是真实发布。静态检查仅主分支触发、无 pull_request_target/workflow_run、只有发布作业写权限、Actions固定完整SHA。

推演：研究分支不触发；修改旧审批拒绝；0.1.0 例外不延续；权限阻塞不改设置；中途失败留下tag/draft，维护者复核后再决定恢复；不自动删除或覆盖。

未运行：真实 GitHub Actions、真实 Release/tag 创建、宿主运行、新平台兼容、官方目录上架。独立初审发现任意证据正文可通过、local synthetic 更新口径及非递增版本风险；已改为结构化证据与日志摘要、真实远端候选更新门槛和版本递增保护，待复审。该记录不是任何未来版本的宿主验收证据，不可复制字段伪造 PASS。
