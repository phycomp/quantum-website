# 01 Quixer 架構總覽

> 來源：arXiv:2406.04305 (Quixer: A Quantum Transformer Model)
> 作者：Nikhil Khatri, Gabriel Matos, Luuk Coopmans, Stephen Clark (Quantinuum)

## 高階架構

Quixer 模型包含以下元件：

1. **Token Embedding** ($W_E$): 將 classical token 向量映射為角度 $\vec{\theta}_w$
2. **Unitary Token Representation** ($U_w$): 參數化量子電路 (PQC) 準備單位矩陣表示
3. **LCU Mixing** ($U_M$): Linear Combination of Unitaries 混合 token 資訊
4. **QSVT**: Quantum Singular Value Transform 應用非線性變換
5. **Feed-Forward** ($U_{FF}$): 量子前饋網路
6. **Measurement**: 讀取量子態，古典處理產生最終輸出

## 資料流

```
Token → Embedding → Unitary → LCU Mixing → QSVT → Feed-Forward → Measurement → Output
```

## Figure 1: Quixer 模型架構

Token embeddings 線性映射為角度 → 角度參數化量子電路 → LCU 準備疊加 → QSVT 應用多項式 → Feed-forward → 測量 → 古典處理

## 與古典 Transformer 的比較

| 特性 | 古典 Transformer | Quixer |
|------|-----------------|--------|
| Attention | Dot product self-attention | LCU + QSVT |
| 複雜度 | $O(n^2)$ | 量子優勢 (理論) |
| 參數 | 大量 | 參數化量子電路 |
| 訓練 | 梯度下降 | 參數化量子電路訓練 |
| 實現 | 古典硬體 | 量子硬體 (模擬) |

## 關鍵創新

1. **非 dot-product attention**: 不量化點積自注意力，而是提出新型 token mixing
2. **LCU + QSVT**: 使用量子算法原語建構 attention
3. **實用語言建模**: 第一個應用於實際語言任務的量子 Transformer

## 來源
- arXiv:2406.04305