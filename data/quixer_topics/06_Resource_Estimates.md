# 06 Resource Estimates

> 來源：arXiv:2406.04305 Section 4

## 量子硬體資源需求

### 量子位元數量

| 元件 | 量子位元數 |
|------|-----------|
| Token register | $\log_2(V)$ (V = 詞彙大小) |
| Control register (LCU) | $\log_2(n)$ (n = 視窗大小) |
| Ancilla (QSVT) | 額外 ancilla qubits |
| Feed-forward | 資料暫存器 |

### 電路深度

- PQC 深度：取決於電路設計
- LCU 深度：$O(n)$ controlled unitaries
- QSVT 深度：$O(d)$ 其中 d = 多項式次數

### 測量 (Shots)

- 需要多個 shots 來估計期望值
- Shot 數量影響統計精度
- Postselection 降低有效 shot 數

## 實現考量

- **古典模擬**: 開源實現可用於古典模擬
- **量子硬體**: 需要容錯量子電腦
- **NISQ 限制**: 當前設備無法運行大規模 Quixer

## 來源
- arXiv:2406.04305