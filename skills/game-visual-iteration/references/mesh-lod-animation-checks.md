# 网格统计、LOD 切换与动画接缝

[English](mesh-lod-animation-checks.en.md)。只在资产优化、LOD 或循环导出问题中按需使用；不要求无关项目新增 3D、LOD 或动画系统。

## 数清统计对象

记录源网格、modifier 评估网格、导出网格与运行时可取得的统计及工具口径。UV、法线、颜色等属性断点可能造成导出或 GPU 顶点拆分；减少源顶点不保证减少运行开销。不盲删 UV、硬边或顶点色，它们可能承担法线、遮罩或动画用途。

最小输入是代表资产、前后导出结果与实际使用场景。比较同一外观要求下的导出顶点/三角面和目标运行测量；无法取得运行数据就标未测，统计减少不单独证明加速。

## LOD 验收包含切换过程

逐级核对轮廓、UV、材质映射、shader 所需属性、枢轴和边界。蒙皮资产额外检查代表动作与简化骨架的变形。按项目相机和实际切换条件，在玩家视角跨越阈值并返回，观察闪变、遮罩丢失、材质跳变或姿态异常。

每一级静帧正确不能证明过渡正确。保留级别/切换条件与画面关联；不照搬固定屏幕占比、面数或压缩收益。阈值往返是本包综合验证建议，本轮未实测。

## 循环分别核姿态与速度

连续播放跨越接缝，分开检查姿态连续性与位移/旋转速度突变。根运动应符合累计位移合同，不强制末帧世界坐标回到首帧。核对重复端帧、采样率、片段范围与目标播放器的循环规则，防止短暂停顿。

约束、驱动器、预览循环修饰器不自动变成导出动作；检查所需运动是否采样/烘焙、目标约束是否重复覆盖。目标环境连续播放并观察根运动、接触与接缝，不能只比首末截图。采样率、骨骼缩放和动作组织方式依项目工具链决定，不统一采用来源习惯。

## 来源与证据

- [EL4CTEO game-optimization](https://github.com/EL4CTEO/blender-skills/blob/3e481ad1b8e301defced7369e4254022abe0821e/skills/blender-game-optimization/SKILL.md)：顶点拆分、批次与 LOD。
- [EL4CTEO animation](https://github.com/EL4CTEO/blender-skills/blob/3e481ad1b8e301defced7369e4254022abe0821e/skills/blender-animation/SKILL.md)：游戏动画、烘焙与循环。
- [arjun988 lod-pipeline](https://github.com/arjun988/blender-skills/blob/904f095d8f36a6e72adaebb08d07f884a074743d/.claude/skills/lod-pipeline/SKILL.md)：属性与逐级检查。

本轮复读固定正文，不是最新版本声明；未运行 Blender、导出脚本或目标游戏，不把作者测试记成本包 PASS。原创方法转述，不包含上游代码或资产。
