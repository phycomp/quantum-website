# 04 QKD 基礎與協議

> arXiv 來源：arXiv:2601.06772, 2605.04650, 2607.17690, 2611.14044

## QKD 基礎

Quantum Key Distribution (QKD) 利用量子力學原理實現信息理論安全 (ITS) 的密鑰交換。

### 核心原理
- **量子不可克隆定理**：未知量子態無法完美複製
- **測量擾動**：測量量子態會改變其狀態
- **糾纏**：量子糾纏提供安全保證

### 主要協議

| 協議 | 年份 | 類型 | 特點 |
|------|------|------|------|
| BB84 | 1984 | Prepare-and-measure | 最基礎，使用偏振態 |
| E91 | 1991 | Entanglement-based | 使用量子糾纏 |
| B92 | 1992 | Prepare-and-measure | 簡化版 BB84 |
| SARG04 | 2004 | Prepare-and-measure | 抗 PNS 攻擊 |
| CV-QKD | 2000s | Continuous variable | 使用相干態 |
| MDI-QKD | 2012 | Measurement-device-independent | 免除 detector 攻擊 |
| TF-QKD | 2018 | Twin-field | 超越 repeaterless bound |

### 2026 年最新進展

#### 1. Experimental Coherent One-Way QKD (arXiv:2601.06772)
- 簡化實作，實用安全性
- Cao et al., 2026
- 引用 15 次

#### 2. Unconditional Authentication in QKD (arXiv:2605.04650)
- 信息理論安全的認證
- 解決 QKD 中的認證問題
- 免除對古典認證的依賴

#### 3. QKD Beyond Stationary Channels (arXiv:2607.17690)
- Mannalath et al., 2026
- 衛星鏈路等非穩態通道
- 短時間、高損耗、快速變化的通道

#### 4. CV-TF-QKD (arXiv:2611.14044)
- 連續變量雙場 QKD
- 提高傳輸距離和密鑰率

### QKD vs Post-Quantum Cryptography

| 特性 | QKD | PQC |
|------|-----|-----|
| 安全性基礎 | 量子力學 | 數學難題 |
| 密鑰分發 | 量子通道 | 古典通道 |
| 距離限制 | 需要量子中繼器 | 無限制 |
| 基礎設施 | 專用硬體 | 軟體更新 |
| 成本 | 高 | 低 |
| 標準化 | ETSI, ITU-T | NIST (FIPS 203/204/205) |

## 來源
- arXiv:2601.06772, 2605.04650, 2607.17690, 2611.14044