# 01 Literature Matrix

> 目标：把真正支撑论文的参考文献、官方工程文章、公开资源统一整理成一张“可直接落仓库”的矩阵。

| 类别 | 参考 | 核心结论 | 对本论文的直接价值 | 公开代码/资源状态 |
|---|---|---|---|---|
| Customer-support benchmark | Beyond IVR: Benchmarking Customer Support LLM Agents for Business-Adherence (EACL 2026 Industry) | customer support 的关键不只是 task completion，而是对 graph-based SOP / policy 的 adherence；提出 UJCS；Dynamic-Prompt Agent 优于 static prompt | 决定论文主轴必须从“回复质量”升级为“服务结果控制 + 路径合规” | 论文公开；未在论文中直接给出官方代码链接 |
| Process evaluation | Process Evaluation for Agentic Systems (EACL 2026 Findings) | agent 评估必须覆盖完整 trajectory、tool calls、high-risk step；支持 weighted compliance | 决定评估层不能只看 final answer，而要做 trace-level 审计 | 论文公开；未直接给出官方代码 |
| Clarification | Scaling Intent Understanding with Clarification Questions (EACL 2026 Industry) | intent understanding 应显式建模“是否需要澄清、问什么、何时问”；轻量模型可工业化落地 | 支撑 clarification-before-action 模块 | 论文公开；未直接给出官方代码 |
| Simulator / benchmark | SAGE (EACL 2026 Findings) | 高质量 user simulator 能系统发现 agent 错误，且比简单方案更有效 | 支撑仿真评估与 bug-finding factory | 论文公开；未直接给出官方代码 |
| Memory benchmark | Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions (OpenReview / ICLR 2026) | memory 需同时看准确检索、测试时学习、长程理解、选择性遗忘 | 支撑经验回流与策略记忆层设计 | 论文公开；代码未在公开页面显式展示 |
| Self-improving context | Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models (OpenReview / ICLR 2026) | agent 可以利用自然执行反馈持续优化 system context 与 memory，而非只靠人工重写 prompt | 支撑“持续进化”增强轴 | 论文公开；代码未在公开页面显式展示 |
| Continual learning agent | CLIN: A Continually Learning Language Agent for Rapid Task Adaptation and Generalization (OpenReview / ICLR 2026) | frozen model 也可通过持久化文本记忆持续改进并迁移 | 支撑“非参数持续进化”方案 | 双盲阶段公开页未提供代码链接 |
| Dialogue self-play | Towards conversational diagnostic artificial intelligence (Nature, 2025) | 多轮对话系统可以通过 self-play simulation + automated feedback 扩展能力 | 支撑 service simulator / automated feedback learning | 论文公开；无完整开源系统 |
| Frontier engineering | Building effective agents (Anthropic) | 最成功的 agent 实现通常依赖 simple, composable patterns，而不是复杂框架 | 支撑仓库整体设计哲学：低复杂度、强可组合 | 官方工程文章 |
| Frontier engineering | Effective context engineering for AI agents (Anthropic) | context 是有限资源；工程重点从 prompt engineering 转向 context engineering | 支撑 context pack / memory / compaction 设计 | 官方工程文章 |
| Tooling | Writing effective tools for AI agents (Anthropic) | tool interface / documentation 直接影响 agent 可用性与可靠性 | 支撑 Tool Contract Layer 设计 | 官方工程文章 |
| Harness | Effective harnesses for long-running agents (Anthropic) | 长任务 agent 的真正难点在 harness：任务组织、工件、上下文管理、恢复与可控性 | 直接支撑论文题目里的“执行 Harness” | 官方工程文章 |
| Permissions / autonomy | Claude Code auto mode (Anthropic) | 高自治下需要 classifier-driven permission gating；授权应按真实世界影响判断 | 支撑 Action Gating / Permission Model | 官方工程文章 |
| Evals | Testing Agent Skills Systematically with Evals (OpenAI) | skill/能力必须被系统化评估：trigger、steps、results、efficiency | 支撑 process-aware eval factory | 官方工程文章 |

## 本论文最终吸收的 5 条主线
1. **Policy-aware service execution**：来自 JourneyBench。
2. **Process-level auditing**：来自 Process Evaluation。
3. **Clarification-before-action**：来自 EACL clarification 论文。
4. **Harness-first runtime**：来自 Anthropic long-running harness 工程路线。
5. **Experience-driven continual improvement**：来自 ACE / CLIN / self-play + feedback 路线。

## 明确不直接照搬的部分
- 不做复杂多 agent 群体系统作为论文主线。
- 不以 leaked source code 为实现依据。
- 不把“持续进化”写成在线底模自我训练。
- 不把“AI 客服系统设计”做成大而全白皮书。
