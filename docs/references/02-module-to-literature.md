# 02 Module to Literature Mapping

## 目标
说明仓库中的每个核心模块，对应哪条研究问题与哪篇参考文献。

## 1. PolicyGraph
### 作用
- 将履约异常处理流程显式化为可执行图。
- 让系统知道允许做什么、必须先做什么、何时升级。

### 主要来源
- JourneyBench
- Process Evaluation for Agentic Systems

### 仓库对应
- `src/aikefu/policy_graph.py`

### 后续扩展
- 节点 schema
- guard expression
- transition evaluator
- risk hooks

## 2. ClarificationRouter
### 作用
- 判断当前信息是否足够进入下一步。
- 在动作前触发最小必要澄清。

### 主要来源
- Scaling Intent Understanding with Clarification Questions
- Effective context engineering for AI agents

### 仓库对应
- `src/aikefu/clarification.py`

### 后续扩展
- clarification scoring
- 澄清模板库
- multi-turn clarification memory

## 3. HarnessRuntime
### 作用
- 编排 policy graph、clarification、动作授权与 trace 记录。
- 构成真正可运行的 execution loop。

### 主要来源
- Effective harnesses for long-running agents
- Building effective agents
- Claude Code auto mode

### 仓库对应
- `src/aikefu/harness.py`

### 后续扩展
- checkpoint
- artifact handoff
- recovery strategy
- permission tiers

## 4. Tool Contract and Action Gating
### 作用
- 规定每个工具和动作的允许范围、输入约束、风险等级和执行前提。
- 对高风险动作做授权控制。

### 主要来源
- JourneyBench 中 task 和 tool 的区分
- Writing effective tools for AI agents
- Claude Code auto mode

### 仓库对应
- 当前未拆独立模块

### 后续扩展
- `action_gating.py`
- `tool_contracts.py`

## 5. Process Trace and Eval Factory
### 作用
- 保存每一步节点、决策、动作、理由和结果。
- 支持审计、回放、评估和指标计算。

### 主要来源
- Process Evaluation for Agentic Systems
- Testing Agent Skills Systematically with Evals
- SAGE

### 仓库对应
- 当前 trace 在 `HarnessRuntime` 内部

### 后续扩展
- trace schema
- replay runner
- weighted compliance scorer
- judge interface

## 6. ExperienceStore and Evolution Loop
### 作用
- 把执行反馈、评估反馈和仿真反馈转成可复用经验。
- 支持策略记忆更新和澄清策略优化。

### 主要来源
- Agentic Context Engineering
- CLIN
- AMIE

### 仓库对应
- `src/aikefu/experience.py`

### 后续扩展
- experience extractor
- strategy memory store
- offline optimizer

## 7. Simulator
### 作用
- 生成正常路径、缺字段、工具失败、用户改口和高情绪等场景。
- 为离线评估和缺陷发现服务。

### 主要来源
- SAGE
- AMIE
- JourneyBench 的数据生成思想

### 仓库对应
- 当前未建模块

### 后续扩展
- `simulator/scene_generator.py`
- `simulator/user_simulator.py`
- `simulator/fault_injector.py`
