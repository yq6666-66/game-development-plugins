# 边界决策 / Boundary decisions

以下是本项目的通用推演，不是上游代码或已运行模板。

| 问题 / Question | 决策依据 / Decision evidence | 小样本 / Small check |
| --- | --- | --- |
| 本地还是全局 / Local or global | 实际共享范围与存活时间，而非方便访问 / actual sharing and lifetime | 两个关卡实例是否意外共用计数 / do two instances share a counter unintentionally? |
| 方法还是事件 / Call or event | 是否需要即时结果、顺序或一对多通知 / response, ordering, fan-out | 退出后旧订阅是否仍处理新事件 / stale subscriber after exit |
| 父子还是外部依赖 / Child or external reference | 删除父对象是否应删除依赖 / destruction ownership | 替换房间但保留玩家时检查引用 / replace room while retaining player |
| 是否拆分模块 / Split a module | 一次真实变化是否影响无关职责 / actual change coupling | 保持外观不变替换规则实现 / replace rule while preserving presentation |

启动契约记录版本来源、入口、必要配置与不含秘密的依赖说明。若暂不实现，交付接口草图和可验证假设，不能把文档伪装为工程。
Record the version source, entry, required configuration and non-secret dependency instructions. A design artifact is not a runnable project.
