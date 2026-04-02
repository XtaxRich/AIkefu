# 20 Literature Matrix

## 1. 使用原则
本文件不是简单罗列论文，而是回答三个问题：
1. 这篇论文或文章在解决什么问题？
2. 它对本题目的直接启发是什么？
3. 它应该落到仓库里的哪个模块或评估环节？

## 2. 核心参考矩阵

### A. JourneyBench / Beyond IVR
**主题**：customer support agent 的 business adherence 评估。  
**关键启发**：客服系统不应只按“回复对不对”评估，而应按是否遵循业务策略、是否覆盖正确旅程来评估。  
**对本论文的价值**：直接决定论文主目标要从“对话质量”升级成“服务执行质量”。  
**映射模块**：Policy Graph、Eval Factory。  
**在实验中的作用**：为“合规解决率 / 路径合规率”提供理论依据。

### B. Process Evaluation for Agentic Systems
**主题**：agent 评估不能只看 final answer，要看完整过程轨迹。  
**关键启发**：必须检查 tool calls、step order、关键高风险节点有没有按要求执行。  
**对本论文的价值**：直接支撑 trace-first 的评估体系。  
**映射模块**：Process Trace、Eval Factory。  
**在实验中的作用**：支撑 replay、compliance score、step-level error analysis。

### C. Scaling Intent Understanding with Clarification Questions
**主题**：意图理解不仅是分类，还包括是否需要澄清、该问什么。  
**关键启发**：在高风险服务场景中，澄清是动作前置，而不是对话修辞。  
**对本论文的价值**：支撑 ClarificationRouter 作为独立模块存在。  
**映射模块**：Clarification Router。  
**在实验中的作用**：可以定义 clarification usefulness、clarification hit rate 等指标。

### D. SAGE
**主题**：用 simulator 和业务知识驱动方式发现 agent 系统缺陷。  
**关键启发**：离线仿真不只是造数据，而是缺陷发现基础设施。  
**对本论文的价值**：支撑 simulator 成为论文实验层的一部分，而不是额外附件。  
**映射模块**：Simulator、Eval Factory。  
**在实验中的作用**：构建扰动场景、回归测试和错误聚类。

### E. Memory benchmark for LLM agents
**主题**：memory 需要被单独评估，不能把它等同于长上下文。  
**关键启发**：系统需要区分即时上下文、持久记忆和可更新经验。  
**对本论文的价值**：解释为什么“持续进化”应优先走外层记忆和经验更新。  
**映射模块**：Experience Loop。  
**在实验中的作用**：支撑连续场景下的表现提升分析。

### F. Agentic Context Engineering
**主题**：通过执行反馈持续优化 context，而不是只靠人手工改 prompt。  
**关键启发**：系统可以从自然反馈中更新外层策略。  
**对本论文的价值**：给“持续进化”提供方法论支点。  
**映射模块**：Experience Loop、Harness Runtime。  
**在实验中的作用**：支撑 experience-driven improvement 设计。

### G. CLIN
**主题**：在不更新模型参数的前提下，通过持久化文本记忆实现持续学习。  
**关键启发**：持续进化未必要改底模参数，完全可以先做非参数路径。  
**对本论文的价值**：帮助收窄论文范围，让系统更易落地。  
**映射模块**：Experience Loop。  
**在实验中的作用**：为“策略记忆更新”提供理论支持。

### H. AMIE
**主题**：利用 self-play 和 automated feedback 改进多轮对话系统。  
**关键启发**：仿真反馈可以成为长期进化的重要来源。  
**对本论文的价值**：说明 simulator 不只是测系统，也可以服务经验回流。  
**映射模块**：Simulator、Experience Loop。  
**在实验中的作用**：支撑 synthetic feedback 的使用。

### I. Anthropic: Building effective agents
**主题**：现实系统中最有价值的是简单、可组合的 agent 模式。  
**关键启发**：本论文不该从一开始就做复杂多 agent。  
**对本论文的价值**：约束总体系统复杂度。  
**映射模块**：整体架构。

### J. Anthropic: Effective harnesses for long-running agents
**主题**：长任务 agent 的关键问题是 harness，而不是单次推理。  
**关键启发**：任务组织、上下文压缩、恢复、工件交接和权限边界是系统主轴。  
**对本论文的价值**：直接决定论文题目中的“执行 Harness”不是包装词，而是研究对象。  
**映射模块**：Harness Runtime、Action Gating、Experience Loop。

### K. Anthropic: Claude Code auto mode
**主题**：高自治系统需要 classifier-driven permission gating。  
**关键启发**：高风险动作必须有显式授权层，不能完全由主模型随意触发。  
**对本论文的价值**：支撑 ActionGating 模块独立存在。  
**映射模块**：Action Gating。

### L. OpenAI: Testing Agent Skills Systematically with Evals
**主题**：能力必须能被系统化评估，不能只靠人工感觉。  
**关键启发**：模块开发不能脱离 eval 契约。  
**对本论文的价值**：把评估从“附属品”变成系统主干。  
**映射模块**：Eval Factory。

## 3. 文献吸收后的总判断
这些文献共同指向一个结论：

本论文最值得研究的，不是“怎么让客服更像人”，而是：
- 怎么让服务智能体按业务策略执行
- 怎么在动作前做澄清控制
- 怎么记录和评估完整过程
- 怎么从反馈中逐步改进

## 4. 当前仓库里的落地方式
这些论文不会被直接翻译成代码，而是被翻译成：
1. 模块定义
2. 数据契约
3. 评估协议
4. 实验设计
5. 开发 handoff

这五类文档，就是当前仓库存在的意义。
