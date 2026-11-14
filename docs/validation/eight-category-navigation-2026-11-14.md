# 八类导航补齐 · 2026-11-14

## 范围与基线

用户要求补齐已有八类导航。在 main `cc09648da6774850f1d76e74ec9be346acee31da` 基础上独立工作，未合并同时进行的 GitHub 研究分支，也未修改其工作区。读取了首页、两种语言的原导航、兼容性、项目约定、既有验证和参考文件清单；本轮无仓库内 AGENTS.md。

八类沿用原导航名称，不新增分类或重排 Skill 路径。新增八组中英文分类页，分别说明触发问题、输入交付、从零/接手两条路径、当前入口、缺口和最小检查。四项正式 Skill 不变。架构、独立 UI 设计、专用构建等缺口没有被包装成已实现能力；工具选择仍按项目需求，不限定引擎、框架或工具名单。本轮没有新增产品推荐、外部脚本、第三方素材或安装依赖。

修改前基线文件通过 Git 历史保留，另从 HEAD 导出原首页、变更记录和导航备份。新文档为既有方法的原创组织与总结，不复制第三方实现，来源边界继续遵循 PROVENANCE。

## 实际执行

Linux / Python 3，仓库根目录：

```sh
python3 scripts/validate_package.py
python3 -m unittest discover -s tests -v
git diff --check
```

- 包结构：PASS。
- 9 项单测：PASS，其中 6 项原包校验，3 项新增导航契约。
- 新测试核对八类双语入口、语言切换、新建/接手及证据/边界章节、导航内本地文件链接。它不检查外部链接、Markdown 锚点渲染或文本语义。
- diff 空白检查：PASS。

## 文档情境检查（不是游戏运行）

- 从零 2D 原型：可以从策划开始，不要求已有工程、3D 美术或特定引擎。
- 接手重开异常：玩法入口定位真实状态与生命周期，不默认重搭架构。
- UI 输入不可达：转界面验证，检查支持的输入与中断；模拟尺寸不写成真机通过。
- 构建完成：仍需要产物启动与操作验证；不自动部署、签名、付费。
- 找免费工具：要求核对许可与当前成本，不将“免费”当作再分发授权。

## 未验证

未安装宿主、运行引擎/游戏、测目标设备或做真实用户易用性测试。未证明完整产品目录、全部英文技术参考或八项独立 Skills 已实现。CI 以远端实际结果为准，本记录不宣称 CI 通过。分支推送不是 main 合并或发布。

## English summary

Eight paired category guides now route new and existing projects through explicit inputs, outputs, available entries, gaps and minimum checks. Four installable Skills remain unchanged. Package checks and nine tests passed; walkthroughs were document-level only. No host, engine, game, hardware or real-user validation is claimed. Navigation completeness is not implementation completeness.
