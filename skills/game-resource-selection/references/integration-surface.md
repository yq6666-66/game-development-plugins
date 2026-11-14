# 工具接入面与决策寿命

[English](integration-surface.en.md)。候选涉及宿主插件、自动化、本地服务或生成管线时按需使用。不是安全认证，也不是安装指令。

## 从可读说明到实际执行

列出入口→依赖文件/配置→触发时机（加载、调用、构建、运行）→读写范围→外部服务/账号/费用→目标宿主替代或缺失项。动态 shell、hooks、配置解析器和 Agent 工具不能因 SKILL.md 可读就视为可移植，也不能原样导入权限、模型与自动执行配置。

静态扫描只发现线索；内容可读、元数据发现、调用链执行、目标效果分别验证。源宿主存在的工具在目标宿主缺失时，应标功能缺口，而非跨宿主 PASS。

## 分阶段追踪数据

区分输入、生成、后处理、导出与提交。界面/服务在本机，不等于生成离线；产物离线打开，不等于无需服务。核对实际发送的提示词、图像/URL和 worker 路由，以及导出旁文件、JSON、日志与来源 URL。不能只检查模型本体而忽略私有提示词或有时效访问参数的 URL。

先只读接口和写入逻辑；获准运行后可用公开样本观察真实请求与产物。没有运行时只报告静态流向，不宣称已经泄密或通过安全测试。运行与分享仍须在授权范围内。

## 轻量决策记录

按需要记录拟议/试验/采纳/替代/撤回、需求与前提、替代项、已验证范围、复查触发、受影响产物及退出成本，可复用已有 ADR。推荐不是采纳，文档完成不自动解锁依赖工作。新增目标设备、版本或用途时重查受影响假设，未变范围保留。

检索未发现已登记引用，不证明没有影响；新需求首次入库也可能影响现存代码。小项目不强制完整架构审批体系。

## 固定来源与读取范围

- [Studio compat-inventory](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/abc0de79d6ceb0b5d7aa693945849b3937afbe6a/.claude/scripts/compat-inventory.sh)：前190行；[skill-improve](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/abc0de79d6ceb0b5d7aa693945849b3937afbe6a/.claude/skills/skill-improve/SKILL.md)：全文。
- [变更传播](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/abc0de79d6ceb0b5d7aa693945849b3937afbe6a/.claude/skills/propagate-design-change/SKILL.md)：全文；[决策模板](https://github.com/Donchitos/Claude-Code-Game-Studios/blob/abc0de79d6ceb0b5d7aa693945849b3937afbe6a/.claude/skills/architecture-decision/references/5-generate.md)：前120行。未沿用零引用等于无影响的推断。
- [prompt2rig server.mjs](https://github.com/blendi-remade/prompt2rig/blob/218ce2adff35a7c04657768a85ff002ebd461c78/server.mjs)及[NOTICE](https://github.com/blendi-remade/prompt2rig/blob/218ce2adff35a7c04657768a85ff002ebd461c78/NOTICE)：全文。静态显示生成请求发送至外部服务、导出记录提示词等元数据；本轮未运行或作完整安全审计。

为原创方法总结，不复制脚本；来源许可不等于整个依赖/输出链可商用。
