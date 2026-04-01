# 03 Reproduction Chain

## 目标
本仓库不复刻单篇论文，而是组合多篇论文与官方工程文章，形成适合本地生活高风险服务场景的研究链路。

## 链路
### 1. 任务定义
来源：JourneyBench

定义方式：
- 任务不是回复生成
- 任务是路径合规与服务结果推进

### 2. 前置澄清
来源：Scaling Intent Understanding with Clarification Questions

定义方式：
- 信息不足时先澄清
- 澄清是执行前置，不是话术补充

### 3. 运行时
来源：Anthropic harness 系列文章

定义方式：
- Harness 负责组织执行
- 包括状态、动作、轨迹、恢复、授权

### 4. 评估
来源：Process Evaluation for Agentic Systems

定义方式：
- 评估看完整轨迹
- 不只看最终回复
- 重点看步骤、动作顺序和升级

### 5. 仿真
来源：SAGE、AMIE

定义方式：
- 构造扰动样本
- 用 simulator 发现问题
- 用 simulated feedback 补充数据

### 6. 持续进化
来源：ACE、CLIN

定义方式：
- 不频繁改底模
- 优先更新经验、策略记忆、澄清偏好

## 实验顺序建议
1. rule baseline
2. static prompt baseline
3. harness only
4. harness with process feedback
5. harness with experience loop
