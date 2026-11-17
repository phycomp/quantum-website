# 03 LCU Mixing (Linear Combination of Unitaries)

> 來源：arXiv:2406.04305 Section 3.2

## 概述

LCU 是量子計算中的一個重要原語，用於準備單位矩陣的線性組合。在 Quixer 中，LCU 用於混合 token 資訊。

## LCU 程序

目標：準備混合

$$M := \sum_{j=0}^{n-1} b_j U_j$$

其中 $b_j$ 是複數參數，$\sum |b_j| = 1$，$n$ 是視窗大小。

### 選擇電路 ($U_{SEL}$)

$$U_{SEL} = \sum_{j=0}^{n-1} |j\rangle\langle j| \otimes U_j$$

條件性地應用 $U_k$ 當控制暫存器狀態為 $|k\rangle$。

### 準備電路 ($U_{PREP}$)

$$U_{PREP}|0\rangle = |a\rangle = \sum_{j=0}^{n-1} a_j |j\rangle$$

### 混合電路

$$U_M = (U_{PREP}^\dagger \otimes I) U_{SEL} (U_{PREP} \otimes I)$$

### Postselection

LCU 需要 postselection：控制暫存器必須保持在 $|a\rangle$ 狀態。這意味著：
- 需要多次執行 (shots)
- 成功機率取決於 $|a_j|^2$
- 失敗的執行被丟棄

## 與古典 Attention 的比較

| 特性 | 古典 Self-Attention | Quixer LCU Mixing |
|------|-------------------|-------------------|
| 混合方式 | Dot product | Linear combination of unitaries |
| 複雜度 | $O(n^2)$ | 量子優勢 (理論) |
| 參數 | $Q, K, V$ 矩陣 | $b_j$ 係數 + PQC 角度 |
| 可訓練性 | 全可訓練 | 部分可訓練 |

## 來源
- arXiv:2406.04305