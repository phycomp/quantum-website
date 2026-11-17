# 04 QSVT (Quantum Singular Value Transform)

> 來源：arXiv:2406.04305 Section 3

## 概述

Quantum Singular Value Transform (QSVT) 是一種量子算法原語，用於對量子態的奇異值應用多項式變換。在 Quixer 中，QSVT 用於對 LCU 準備的疊加態應用非線性變換。

## QSVT 原理

### 奇異值變換
給定一個矩陣 $A$，QSVT 可以計算 $P(A)$，其中 $P$ 是一個多項式。

### 多項式應用
- 透過 $\Pi_\phi$ 閘的相位指定多項式
- 多項式次數決定變換的複雜度
- 可模擬各種非線性函數

### 在 Quixer 中的應用
1. LCU 準備疊加態 $M = \sum b_j U_j$
2. QSVT 應用多項式 $P(M)$
3. 產生非線性 token mixing

## QSVT vs 古典非線性

| 特性 | 古典 (ReLU, GELU) | QSVT |
|------|-------------------|------|
| 變換類型 | 逐元素非線性 | 矩陣奇異值變換 |
| 參數 | 無 (固定函數) | 多項式係數 (可訓練) |
| 實現 | 古典計算 | 量子電路 |
| 表達力 | 有限 | 可模擬多種函數 |

## 來源
- arXiv:2406.04305