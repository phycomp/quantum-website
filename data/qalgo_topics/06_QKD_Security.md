# 06 QKD 安全性與攻擊防禦

> arXiv 來源：arXiv:2605.22580, 2610.25203

## Detection Efficiency Mismatch 攻擊防禦 (arXiv:2605.22580)

**標題**：Practical Countermeasure Against Attacks Exploiting Detection Efficiency Mismatch in Quantum Key Distribution

### 攻擊原理
- 接收端 (Bob) 的 detector 效率不匹配
- 攻擊者 (Eve) 利用效率差異進行攻擊
- 導致密鑰洩漏

### 防禦措施
- 實用的 countermeasure
- 偵測效率匹配校準
- 安全密鑰率計算

## 量子取證 (Quantum Forensics) (arXiv:2610.25203)

**標題**：Simulation-Based Quantum Forensics for QKD: Machine Learning Attack Detection and Signature Extraction

### 核心內容
- **機器學習攻擊偵測**：使用 ML 識別 QKD 攻擊模式
- **簽名提取**：提取攻擊的特徵簽名
- **模擬基礎**：基於模擬的量子取證

### 應用
- QKD 系統的安全監控
- 攻擊事件的事後分析
- 安全事件的自動化偵測

### 會議
- International Conference on Quantum Computing Infrastructure & Technologies (QUANCOM 2026)
- Trento, Italy, September 2026

## QKD 常見攻擊類型

| 攻擊類型 | 目標 | 防禦 |
|----------|------|------|
| Intercept-Resend | 量子通道 | BB84 基礎防禦 |
| Photon Number Splitting (PNS) | 多光子脈衝 | SARG04, 誘騙態 |
| Detector Blinding | 偵測器 | MDI-QKD, 偵測器校準 |
| Detection Efficiency Mismatch | 偵測器效率 | 效率匹配校準 |
| Trojan Horse | 光學元件 | 光學隔離 |
| Side-Channel | 實作漏洞 | 安全認證 |

## 來源
- arXiv:2605.22580, 2610.25203