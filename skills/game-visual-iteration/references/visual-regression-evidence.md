# 自动截图：确定性不等于完整验收

[English](visual-regression-evidence.en.md)

用于自动截图、基线比较或偶发像素差异。只在项目已授权该检查时使用，不要求安装 Three.js/Puppeteer，不默认更改浏览器安全设置。

## 分开两条证据路径

1. **像素比较**：记录构建、渲染后端、设备、viewport/DPR、相机、随机种子、动画时刻。定义资源/着色器/视频帧的就绪条件和超时结果；有 worker 时确认控制范围，而非假设页面注入覆盖全部线程。网络空闲或固定延时本身不证明全部内容就绪。
2. **真实交互**：移除截图专用的禁输入、冻结时钟、隐藏UI等处理，使用正常输入检查HUD、遮挡、菜单、焦点和暂停恢复。像素轨道通过不能替代这条路径；不相关系统标为范围外。

掩膜区域和隐藏元素必须预先声明。画面更稳定可能仅因为关键内容被排除；对被排除区域不作通过结论。

## 结果完整性与基线

每个计划用例必须对应终态和原因，分别记录计划、执行、实际比较、通过、失败、跳过、阻塞数量。缺参考图、设备丢失、黑屏、资源错误、超时或浏览器重启，不能自动算通过。重试保留每次结果，次数按项目预算而非上游常量。

预期美术修改、环境变化、真实回归分开审查；确认差异原因后才更新参考图。不能通过调大容差、排除未知失败或重新生成基线来证明修复。跨GPU/后端比较需可解释的基线或容差；阈值来自实际误差与重要区域，不复制示例数字。

## 最小检查建议，尚未执行

- 同环境同状态重复采集，量化自然变化；有差异先定位clock/seed/worker/video/后端。
- 隔离副本故意改一项可见材质，要求实际diff和失败，保留原基线。
- 制造一个缺参考或资源错误，要求非PASS且终态数量完整。
- 清除截图夹具后用正常输入走菜单、移动、暂停恢复；单独记录交互证据。

## 来源与证据边界

2026-11-15 静态阅读全文，未运行上游、未查看渲染截图。mrdoob/three.js 与贡献者，固定提交 `b529cbbda2ba956a8444545a5634f6db22b68385`（2026-11-14T16:26:36Z），package 0.187.0：

- [E2E README](https://github.com/mrdoob/three.js/blob/b529cbbda2ba956a8444545a5634f6db22b68385/test/e2e/README.md) 与 [执行器](https://github.com/mrdoob/three.js/blob/b529cbbda2ba956a8444545a5634f6db22b68385/test/e2e/puppeteer.js)：输入被禁用、例外列表和结果汇总。
- [确定性注入](https://github.com/mrdoob/three.js/blob/b529cbbda2ba956a8444545a5634f6db22b68385/test/e2e/deterministic-injection.js)、[页面清理](https://github.com/mrdoob/three.js/blob/b529cbbda2ba956a8444545a5634f6db22b68385/test/e2e/clean-page.js)、[package](https://github.com/mrdoob/three.js/blob/b529cbbda2ba956a8444545a5634f6db22b68385/package.json)：时钟/worker/视频就绪及隐藏UI的夹具范围。
- [Issue #33559](https://github.com/mrdoob/three.js/issues/33559)，gkjohnson，2026-05-11 原始正文：设备丢失可能漏计结果。固定源码分支重启浏览器却未给当前用例加入失败集合，提示结果缺失风险；是静态判断与作者报告，未独立运行复现。

以上流程为原创综合，不是跨引擎API承诺。冻结时序会遮蔽动画/音频问题；上游安全flags、Linux驱动路径和阈值不得当通用配置。仅总结与链接，不复制代码或素材；MIT声明不自动覆盖素材和依赖。
