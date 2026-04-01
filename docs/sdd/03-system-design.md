# 03 System Design

## 模块
### PolicyGraph
定义节点、转移条件、允许动作与风险级别。

### ClarificationRouter
识别当前缺失的关键槽位，并生成最小必要澄清问题。

### HarnessRuntime
串联策略图、澄清、动作授权与轨迹记录。

### ExperienceStore
记录执行后反馈，作为持续进化输入。

## 核心数据流
input case -> state normalization -> policy node selection -> clarification or action decision -> trace logging -> experience writeback

## 设计原则
- policy first
- clarification before action
- permission before execution
- trace for every step
- evolution from feedback
