# 经验来源与限制

整理日期：2026-11-13。只蒸馏方法，没有附带第三方代码、图片、模型或完整文章。

## 《黄铜之心》

依据用户提供的《BRASSHEART_黄铜之心(2).html》画面分析：统一风格、场景分层、主光与补光、近景机械优先、有原因的磨损、效果逐项比较。

本次技能整理未重新读取原 HTML、未运行或取得实际截图。分析中的 Unity 对应方式、纹理通道与渲染管线能力不作为已验证配方；采用前须核对实际工程与对应官方文档。不要将参考作品配色、武器系统或大场景布局变成本项目要求。

## FPS 复现实验

来源：[wquguru/fable52-fps-repro](https://github.com/wquguru/fable52-fps-repro)，本轮研究检查版本 `a7e1df3ce32eb2bb05e23ae457fe5fe2bffab961`；读取说明、许可与部分源码，未运行演示。

- [材质样本](https://github.com/wquguru/fable52-fps-repro/blob/a7e1df3ce32eb2bb05e23ae457fe5fe2bffab961/demos/02-materials/index.html)：借鉴局部材质变化及独立样本方法。
- [FPS 样本](https://github.com/wquguru/fable52-fps-repro/blob/a7e1df3ce32eb2bb05e23ae457fe5fe2bffab961/demos/04-fps/index.html)：借鉴灯光分区、质量档位及诊断量。
- [录屏控制](https://github.com/wquguru/fable52-fps-repro/blob/a7e1df3ce32eb2bb05e23ae457fe5fe2bffab961/scripts/rec/auto04.js)：使用调试朝向、自动瞄准及生命值保底，提示必须分开“画面展示”与“正常操作验收”。
- [许可](https://github.com/wquguru/fable52-fps-repro/blob/a7e1df3ce32eb2bb05e23ae457fe5fe2bffab961/LICENSE)：仓库为 MIT；实际复用实质代码时保留版权与许可，并分别检查第三方依赖。
- 用户另提供的教程经验补充了同光照并排、掠射角和近远景观察的方法；这些用于组织诊断，不代表本次已实测教程的所有效果。
- 作者的成本和性能属于其单次实验，不是本项目保证。不要运行其付费/自动权限脚本来替代项目的确认点。

[Saltline 原作入口](https://claude.ai/artifact/BGY1SztrAYcJQHSsnHHGmp)本次无法读取，未运行、未审计；上述复现仓库不是 Saltline 源码。不得把复现实验的细节归为 Saltline 已验证实现。
