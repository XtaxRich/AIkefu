# AIkefu

面向本地生活高风险服务场景的执行 Harness 与持续进化服务智能体项目。

## 项目定位
本仓库同时服务两条主线：
1. **毕业论文**：面向本地生活履约异常场景的执行 Harness 与持续进化服务智能体研究。
2. **工程原型**：构建一个可运行的 service-agent runtime，用于验证策略图约束、澄清优先、动作授权、过程评估与经验回流。

## 当前聚焦场景
- 催上门
- 迟到
- 改期
- 爽约

## 核心研究问题
1. 如何让服务智能体在高风险场景中按策略图执行，而不是仅依赖 prompt 自由生成。
2. 如何在信息不充分时触发最小必要澄清，降低误路由与误动作。
3. 如何用过程评估与经验回流，让智能体在不频繁改底模参数的前提下持续进化。

## 仓库结构
```text
AIkefu/
├── docs/
│   └── sdd/
│       ├── 00-charter.md
│       ├── 01-research-question.md
│       ├── 02-requirements.md
│       ├── 03-system-design.md
│       ├── 04-data-contracts.md
│       ├── 05-evaluation-plan.md
│       └── 06-implementation-plan.md
├── src/
│   └── aikefu/
│       ├── __init__.py
│       ├── types.py
│       ├── policy_graph.py
│       ├── clarification.py
│       ├── harness.py
│       └── experience.py
├── tests/
│   ├── test_policy_graph.py
│   └── test_clarification.py
├── pyproject.toml
└── .gitignore
```

## 开发原则（SDD）
- 先写研究问题、约束、输入输出，再写代码。
- 先固化数据契约、动作边界、评估口径，再增加模型复杂度。
- 所有策略必须可追踪、可回放、可审计。
- 持续进化优先走非参数路径：经验回流、策略记忆、澄清策略优化、Harness 配置优化。

## 快速开始
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest
```

## 第一阶段目标
- 跑通履约异常场景最小闭环
- 实现策略图 + 澄清优先 + 动作授权的原型
- 建立 process trace 与 experience log
- 为后续仿真评估和持续进化做数据底座
