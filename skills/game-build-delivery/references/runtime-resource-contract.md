# 运行资源交付合同 / Runtime resource delivery contract

用于独立交付副本缺少运行资源、外观或依赖时；先定位是包内解析失败还是已解析后接入失败。不因此新增模组、下载或资源服务。

## 分流后再排错

1. 列出一个失败资源的来源、导入设置、运行标识、加载 API、实际包内表示及外部依赖。区分引擎导入资源、原样数据文件、用户选择的外部文件和额外资源包。
2. 先验证该类别对应的加载机制，不能用开发机存在源文件证明交付正确，也不要把全部资源改成原样文件绕过导入。
3. 在独立交付目录启动，沿正常操作触发加载，记录被解析的资源与错误；不要从原工程目录启动后宣布通过。只有数据文件存在仍不足以证明图片/模型的传递依赖齐全。
4. 对已支持的外部模型，分别检查从文件和从内存加载时的相对资源根。缺依赖应按项目合同报告或降级；即使默认材质符合降级约定，也应记为预期降级，不等于完整素材加载。
5. 重新进入同一路径，检查恢复和重复加载；加载、包内容、视觉显示和玩法分别记证据。没有引擎/目标环境时，只有静态核查结论。

最小样本：一个已导入资源和一个项目确需的原样数据文件；若外部模型在范围内，再用带相对纹理的模型做文件/缓冲区对照。最小负向控制是在隔离副本移走一个依赖，确认错误被识别，而非删除唯一原件。样本数量随风险决定，不要求所有项目同时具有这些类别。

## Godot 的具体证据，不是跨引擎 API 配方

所读 Import process 文档区分 ResourceLoader 的导入映射与 FileAccess 的原始文件访问，并区分 Keep File 与 Skip File。原始文件在编辑器存在，导出后可能只剩导入表示。所读运行加载文档不建议将外部文件加载方式用于普通项目资源；glTF 从缓冲区读取时需要显式外部资源根。以当前锁定 Godot 版本重新核实这些行为；其他引擎映射到各自的构建资源数据库和解析机制。

## English procedure

Use only for missing runtime content or an already-supported external-content path. Classify each asset as imported, raw data, an external user file, or an additional resource pack. Record source, import settings, runtime identity, loader, packaged representation and dependencies. Validate the loader appropriate to the category before changing export filters. Do not bypass the import pipeline wholesale.

Launch the delivered copy independently of the source project and trigger loading with normal input. For supported external models, compare file and buffer loading with relative dependencies. In an isolated copy, withhold a dependency and check the declared error/fallback contract. Re-enter the same path to check recovery and duplicate loads. Mark a declared fallback as a fallback, not full-content success. Report packaging, loading, rendering and gameplay separately; without the runtime or target environment, report static checks only. The reviewed Godot documents describe import remapping and explicit base paths for buffer-loaded glTF; other engines require their own version-specific mapping, not these API names.

## 来源与范围 / Provenance and scope

2026-11-16 阅读 Godot contributors 文档提交 `2c6cc131ac13f14443e052ccc91393986f37ae26`（提交时间 2026-11-14T19:57:30Z），全文文本，未查看图片、未执行示例；master 快照不代表特定稳定版。新增价值是把既有“导出包可能缺资源”提示拆成资源类别、加载路径与传递依赖的检查合同。属于文档依据与原创流程推断，非运行 PASS。

- [Import process](https://github.com/godotengine/godot-docs/blob/2c6cc131ac13f14443e052ccc91393986f37ae26/tutorials/assets_pipeline/import_process.rst)
- [Runtime file loading and saving](https://github.com/godotengine/godot-docs/blob/2c6cc131ac13f14443e052ccc91393986f37ae26/tutorials/io/runtime_file_loading_and_saving.rst)

Only original paraphrase and source links are included. Godot documentation's own license remains applicable; this package's MIT does not relicense it. No upstream code, screenshots or assets are redistributed. No issue was used as proof of an engine defect, and no engine or upstream demo was executed. Format decoders, untrusted file security, platform packaging variations and large-resource performance need separate scoped validation.
