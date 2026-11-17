# 05 Experimental Results

> 來源：arXiv:2406.04305 Section 4

## 實驗設置

- **數據集**：Penn Treebank (語言建模)
- **比較基線**：等效古典模型
- **評估指標**：Perplexity (困惑度)

## 主要結果

Quixer 是第一個應用於實際語言建模任務的量子 Transformer 模型。

### 結果摘要
- 結果與等效古典基線模型競爭
- 展示了量子 Transformer 的可行性
- 提供了量子硬體資源估算

## 資源估算

- 量子位元數量：取決於詞彙大小和視窗大小
- 電路深度：取決於 QSVT 多項式次數
- 測量次數：需要多個 shots

## 限制

1. **梯度問題**：PQC 的梯度可能消失 (barren plateaus)
2. **Postselection**：LCU 需要 postselection，降低成功率
3. **雜訊**：NISQ 設備的雜訊影響結果
4. **規模**：目前僅在小規模上測試

## 來源
- arXiv:2406.04305