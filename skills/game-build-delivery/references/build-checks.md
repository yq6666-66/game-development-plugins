# 构建检查与来源 / Build checks and provenance

以下是可迁移判断，不是跨版本可直接运行的配方。/ These are decision aids, not cross-version executable recipes.

## 缓存与有效版本 / Cache and effective versions

将源码身份、实际工具版本、目标和影响导入/编译的配置连接到产物，缓存键只按真实影响因素设计。缓存还原、构建和缓存保存分开报告；共享运行器上的不可信缓存或产物不应自动当作可信发布输入。缓存失效可作为排错样本，但不要删除用户唯一缓存或成功产物来试错。

Tie artifacts to source identity, actual tool versions and output-affecting configuration. Separate cache restore, build and cache save outcomes. Untrusted shared-runner outputs are not automatically trusted release inputs. Test cache invalidation in isolation, not by deleting the user's only useful data.

GameCI 所读版本在 `action.yml` 中说明非 `auto` 的 `unityVersion` 当前被忽略，版本从项目读取；`cliVersion` 默认 `latest`。这说明要核查实际输入生效情况，不意味着所有版本都如此。Windows 测试工作流按配置隔离 Library 缓存，没有前缀回退，并将缓存保存设为独立、有限时、非致命步骤。不要抄其固定超时、重试次数、密钥或 dirty-build 设置。

In the reviewed GameCI revision, `action.yml` says non-auto `unityVersion` is ignored and the CLI reads the project version; `cliVersion` defaults to latest. Recheck the selected version rather than generalizing this behavior. Its Windows workflow separates configuration-specific cache restore/save and bounds an optional save. Do not transplant numeric timeouts, retries, secrets or dirty-build policy.

## 导出边界 / Export boundaries

Godot 所读文档区分可运行导出和只含资源的 PCK/ZIP，指出需要导出预设及匹配平台依赖，命令输出路径相对项目路径而不是调用目录；导出配置与凭据文件也有不同的共享边界。具体 CLI、模板和配置按工程版本核查，不复制到其他引擎。开发环境能运行不能证明导出包包含动态加载资源或必需非资源文件。

The reviewed Godot guide distinguishes runnable exports from data-only packs, requires export presets and platform prerequisites, and describes project-relative output paths and separate credential storage. Check the actual project version. A working editor does not establish that exported runtime-loaded data is included.

## 读取记录 / Reading record

2026-11-14，读取文本，未运行引擎、工作流、构建或上游脚本；未检查教程图片像素。/ Text review only; no engines, upstream workflows or screenshots were exercised.

- GameCI contributors, [unity-builder](https://github.com/game-ci/unity-builder/tree/fc892a0623ba0dba1f2d01b2be52994a57f936f3): full `.github/workflows/build-tests-windows.yml`, `action.yml` inputs through container settings, [MIT license](https://github.com/game-ci/unity-builder/blob/fc892a0623ba0dba1f2d01b2be52994a57f936f3/LICENSE).
- Godot contributors, [Exporting projects](https://github.com/godotengine/godot-docs/blob/c5b3485cb4b6e14ae3d8a45271bcddac7caad66a/tutorials/export/exporting_projects.rst): export modes, templates, resource filters, configuration and CLI sections through pack formats; [CC BY 3.0 license](https://github.com/godotengine/godot-docs/blob/c5b3485cb4b6e14ae3d8a45271bcddac7caad66a/LICENSE.txt). A repository snapshot is not a guarantee for a specific released engine version.

本页及入口为原创综合总结，未搬运代码、图片、素材或模板。MIT 仅适用于本仓库原创内容，不改变来源许可；本技能不自带第三方软件。静态来源判断与项目实际运行证据分别保留。

This is an original synthesis, not copied code, images, assets or templates. This repository's MIT license does not relicense upstream material; no third-party software is bundled. Keep source review separate from project runtime evidence.
