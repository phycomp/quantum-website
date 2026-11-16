# 03 QAOA (Quantum Approximate Optimization Algorithm)

> arXiv 來源：arXiv:2611.08646 (2026-11)

## 概述

QAOA 是一种用于组合优化问题的量子算法，通过将组合目标编码为 Ising Hamiltonian 并交替演化来求解。

## Sign-hedged Beam QAOA

**論文**：arXiv:2611.08646v1
**作者**：Anupama Ray, Arush Sharma
**日期**：2026-11-05

### 核心思想

QAOA 编码组合目标为 Ising Hamiltonian，交替进行：
1. **Cost layer**: 应用问题 Hamiltonian
2. **Mixer layer**: 应用混合 Hamiltonian

### Sign-hedged Beam 变体

- 使用 beam search 优化 QAOA 参数
- Sign-hedged 技术提高优化稳定性
- 在大规模组合优化问题上表现优异

### 应用场景

| 问题类型 | QAOA 应用 |
|----------|-----------|
| Max-Cut | 图分割优化 |
| Traveling Salesman | 路径优化 |
| Portfolio Optimization | 投资组合优化 |
| Scheduling | 调度问题 |
| Network Design | 网络设计 |

### 与其他量子优化算法比较

| 算法 | 特点 | 适用场景 |
|------|------|----------|
| QAOA | 近似优化 | 组合优化 |
| VQE | 变分量子本征求解 | 量子化学 |
| Grover | 精确搜寻 | 无序数据库 |
| Quantum Annealing | 模拟退火 | 大规模优化 |

## 來源
- arXiv:2611.08646