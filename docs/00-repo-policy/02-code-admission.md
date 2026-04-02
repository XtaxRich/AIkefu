# 02 Code Admission

## Why docs first
先文档后实现，避免“占位代码看起来像已完成系统”。

## Current rule
当前阶段主分支优先收敛：
- 研究问题
- 模块边界
- 数据对象
- 评估协议
- 实验设计

## Code gate
未来代码只有满足以下条件才应进入 `main`：
- 有对应模块 brief
- 有输入输出定义
- 有 trace 字段
- 有最小评估 case
- 有失败模式说明
