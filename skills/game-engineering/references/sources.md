# 来源与取舍 / Sources and decisions

读取 / Read: 2026-11-14。本文是原创流程综合，不复制或翻译上游段落、脚本、图像；项目 MIT 不改变来源条款。
Original synthesis, no upstream prose/code/assets copied. Our MIT license does not replace source licenses.

- Godot Engine contributors, [Scene organization](https://github.com/godotengine/godot-docs/blob/c5b3485cb4b6e14ae3d8a45271bcddac7caad66a/tutorials/best_practices/scene_organization.rst), commit `c5b3485cb4b6e14ae3d8a45271bcddac7caad66a`。实际读完整正文及 [LICENSE.txt](https://github.com/godotengine/godot-docs/blob/c5b3485cb4b6e14ae3d8a45271bcddac7caad66a/LICENSE.txt)，CC BY 3.0。来源强调依赖由组装环境提供、生命周期与节点关系相符；本 Skill 将其作为所有权与依赖检查依据。Godot 的节点组织不直接等于其他引擎的实体系统，文中的 OOP、单例与“无依赖”建议不设为普遍硬规则。
- OpenAI [web-game-foundations](https://github.com/openai/plugins/blob/d420d13051bffe4543ed39e30fa46b87148e47dd/plugins/game-studio/skills/web-game-foundations/SKILL.md)，完整入口已读。该提交根与 game-studio 目录清单未见许可证，复用许可未确认，仅作为资料线索；未复用文字或代码。其特定引擎、DOM和GLB默认选择未采用。

The Godot document supports explicit dependencies and lifetime-aware scene relationships, not an engine-neutral architecture mandate. OpenAI's entry was read as a lead only; no license was found in the inspected root/plugin listings, and no material was copied. Its engine/DOM/GLB defaults are not adopted.

本轮只核对文档，未运行这些项目或目标引擎。模块切片、双实例反例与交付格式是本项目推导的工作方法，不是作者已验证结果。
Document review only. Vertical slices, two-instance counterexamples and delivery fields are our synthesis, not upstream runtime evidence.
