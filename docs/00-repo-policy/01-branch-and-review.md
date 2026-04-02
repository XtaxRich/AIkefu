# 01 Branch and Review

## Branch policy
- `main`：稳定文档与通过门槛的实现
- `exp/*`：单模块试验
- `eval/*`：评估与 judge
- `sim/*`：模拟器与故障注入

## Merge policy
任何实现进入 `main` 前，至少需要：
1. 对应的模块说明
2. 输入输出契约
3. 最小评估样例
4. trace 设计
5. 失败路径说明
