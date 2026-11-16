# 02 Shor's Algorithm

> arXiv 來源：arXiv:2603.28627 (2026-03)

## 概述

Shor's algorithm 是量子計算中最著名的算法之一，用於整數因數分解。它對 RSA 和 ECC 等公鑰加密系統構成威脅。

## 2026 年關鍵突破

### 10,000 原子量子位元實現 Shor's Algorithm

**論文**：arXiv:2603.28627
**標題**：Shor's algorithm is possible with as few as 10,000 reconfigurable atomic qubits

**核心成果**：
- 使用量子纠错码 (quantum error-correcting codes)
- 高效逻辑指令集 (efficient logical instruction sets)
- 电路设计优化
- 在加密相關規模上執行 Shor's algorithm
- 僅需 10,000 個可重配置原子量子位元

### 技術細節

1. **量子纠错码**
   - 表面码 (Surface codes)
   - 色码 (Color codes)
   - 低密度奇偶校验码 (LDPC codes)

2. **逻辑指令集**
   - Clifford + T 门集合
   - Magic state distillation
   - 逻辑门合成

3. **电路设计**
   - 模块化 Shor 电路
   - 优化的量子傅立葉变换 (QFT)
   - 资源估算与优化

### 影響

- **RSA-2048**: 需要 ~2000 万物理量子位元 (传统估算)
- **新估算**: 仅需 10,000 个逻辑量子位元
- **时间线**: 密码学相关规模的量子计算可能比预期更早实现

### 後量子密碼 (PQC) 的緊迫性

Shor's algorithm 的可行性降低意味着：
- RSA/ECC 将在可预见的未来被破解
- 后量子密码 (ML-KEM, ML-DSA) 的迁移更加紧迫
- NIST PQC 标准 (FIPS 203/204/205) 需要加速部署

## 來源
- arXiv:2603.28627