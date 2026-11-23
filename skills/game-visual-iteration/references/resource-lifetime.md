# 运行资产生命周期：卸载不是从场景树移除

## 来源、版本及实际阅读

研究日期：2026-11-16（Asia/Shanghai）。来源作者为 Three.js 项目作者与贡献者。固定参考提交 `ab6386854db0dcebd9800b95a9a5effde6071b19`（2026-11-15T11:16:20Z，package.json 版本 `0.187.0`）；它是读取时 dev 的版本，不建议项目因此升级。

- 全文读 [How to dispose of Objects](https://github.com/mrdoob/three.js/blob/ab6386854db0dcebd9800b95a9a5effde6071b19/manual/pages/how-to-dispose-of-objects.html)：GPU 资源释放、共享资源、ImageBitmap、统计余量。
- 全文读 [Cleanup](https://github.com/mrdoob/three.js/blob/ab6386854db0dcebd9800b95a9a5effde6071b19/manual/pages/cleanup.html)：创建时登记资源与卸载时扫描场景树的差别；动态挂载子对象的边界。
- 全文读 [webgl_test_memory 示例](https://github.com/mrdoob/three.js/blob/ab6386854db0dcebd9800b95a9a5effde6071b19/examples/webgl_test_memory.html)：每帧创建、渲染、移除并释放几何/材质/纹理；这是示例机制，不是建议游戏每帧创建释放。
- 全文读 [WebGLGeometries.js](https://github.com/mrdoob/three.js/blob/ab6386854db0dcebd9800b95a9a5effde6071b19/src/renderers/webgl/WebGLGeometries.js)，局部读 [Texture.dispose](https://github.com/mrdoob/three.js/blob/ab6386854db0dcebd9800b95a9a5effde6071b19/src/textures/Texture.js)：前者监听 dispose 并清理属性、绑定与计数；后者派发事件。未检查 WebGPU 全路径。
- 查看 Issue [#32969](https://github.com/mrdoob/three.js/issues/32969) 正文（2026-02-08，报告版本 r182），包含 storage texture 释放后复用的异常及修复链接；未读完整讨论或复现。只证明不同后端/资源类型需要另验，不能当作当前版本仍有同一 bug。
- 检查根 LICENSE 为 MIT；仅原创方法与链接，不复制源码、素材或全文。官方旧路径 `/manual/en/how-to-dispose-of-objects.html` 获取 404，随后改读固定源码文档，没有把不可取页面算已读。

## 问题与增量

适用于换关、模型替换、预览窗口关闭后内存上涨或再次进入卡顿。现有 asset-runtime-gates 只有“共享资产卸载前查所有者”，本次将其细化为资源分类、登记时点、稳定余量和坏样本检出，不重复导入同机位截图原则。

来源可确认：场景移除与资源释放不同；材质释放不等于纹理释放。ImageBitmap 的 CPU 生命周期由应用管理；骨架、纹理可以被多个对象共享。renderer.info 的内部资源数可能保留可复用余量，不能要求无条件归零。Cleanup 的资源追踪在加载时登记，避免卸载时误把后来挂在角色手上的道具一起释放；它也不自动覆盖后来新增的资源。

本包综合判断：把“场景中可达”与“由这个场景拥有”分开。资源记录至少包含创建者、当前消费者、最后释放条件和是否属于跨场景缓存。释放顺序由依赖决定，不能全局遍历 dispose 作为通用修复。资源计数下降也不等于 CPU 引用、worker、监听或全部显存均释放。

## 最小流程（建议，未实际运行）

1. 锁定实际引擎版本、渲染后端、资源加载器与测量口径。选一个能正常输入进入、退出并再次进入的场景。
2. 记录冷启动与预热后基线；区分对象数量、GPU 资源数量、可取得的内存和帧时间。下载文件大小不作运行内存替代。
3. 登记独占资源、共享资源、应用级缓存与异步加载任务。关闭场景后阻止迟到加载结果重新挂入已退出场景；这是异步生命周期的组合建议，须按现有取消/代际规则实现。
4. 重复同一路径，检查在约定清理时点后的稳定区间及增长趋势，而不是任意一次快照是否归零。循环数和允许余量由项目风险、资源与设备确定。
5. 两个同时使用同一纹理的对象，卸载其中一个后另一个仍应正确显示；仅在最后消费者结束且所有者的保留/缓存策略允许回收时才释放。额外检查卸载前后动态挂载的道具归属。
6. 隔离副本故意漏掉一项独占纹理释放，确认监测能识别相对基线增长；恢复后再次比较。不要在共享正式工程破坏资源。
7. 重进后正常交互并测首帧尖峰。避免把“释放后重建没有报错”当作无代价。不可取得的指标标未验证，不用强制 GC 后的单点数字证明游戏无泄漏。

## 条件与局限

需要已有加载/卸载路径及允许执行的测试副本；没有动态资源的项目不必新增系统。Three.js WebGL 的具体 dispose / info 名称不能直接套到 Unity、Godot 或 WebGPU。其他引擎迁移的是所有权和证据方法，API 与自动引用管理另核。缓存稳定不证明所有泄漏不存在；漏释放坏样本只能证明对应指标具有检出力。控制器和渲染器的 dispose 后可用性与几何材质不同，不能一律复用。

本轮只有固定文档、示例和局部源码检查，未安装、运行 Three.js 或执行真实游戏；Issue 是作者报告，不是本包实测。未对上游作完整安全或性能审计。

## 落地建议

在 `game-visual-iteration/references/` 新增中英资源生命周期检查，入口按“换场景后内存增长/重进卡顿”路由；不新增 Skill。保留现有共享所有者原则，补充稳定余量、CPU/GPU 分层、动态挂载归属和最小负向控制。有效性以项目正常切换、共享资源保留、已知漏释放可检出三类证据衡量；包校验 PASS 不代表它们通过。

## English procedure

Use for memory growth or re-entry stalls in an existing load/unload path, not to add a new streaming system. Record the actual engine, renderer and measurements. Separate scene reachability from ownership: register exclusive resources, shared consumers, persistent caches and late asynchronous results when they are created or loaded. Persistent caches are reclaimed according to their own lifetime policy, not merely when the last visible object disappears. Removing an object is not the same as releasing its GPU resources; material cleanup does not necessarily release textures or CPU image data.

Measure cold and warmed-up baselines and repeated normal entry/exit/re-entry. Look for a stable post-cleanup range or growth trend rather than demanding zero counters. Keep another consumer of a shared resource alive while unloading one owner, and check dynamically attached objects separately. In an isolated test copy, deliberately omit one exclusive release to verify that the chosen metric detects it, then restore and repeat. Check re-entry rendering and frame-time spikes, not merely absence of exceptions. Do not force garbage collection to manufacture a clean gameplay result.

The pinned sources above cover Three.js WebGL documentation, one memory example and local disposal implementation; WebGPU paths were not comprehensively checked. Issue reports are not reproduced failures. Apply ownership reasoning across engines but verify actual APIs, cache semantics and disposal contracts. No runtime, device, leak-freedom or performance PASS is claimed. Source text/code/assets are not redistributed; this is original synthesis.
