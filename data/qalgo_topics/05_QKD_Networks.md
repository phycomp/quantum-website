# 05 QKD 網路部署

> arXiv 來源：arXiv:2611.17265, 2610.22879, 2602.17227

## 四城市糾纏 QKD 網路 (arXiv:2611.17265)

**標題**：A deployed four-city entanglement-based QKD network with real-time key delivery, benchmarked against finite-key security bounds

### 核心成果
- **4 城市**糾纏型 QKD 網路
- **即時密鑰交付** via ETSI GS QKD 014
- **13.5 bit/s** 密鑰率 (109 km 距離)
- **部分非局部色散補償**
- **有限密鑰安全界限** benchmark

### 技術細節
- 糾纏分發 (Entanglement distribution)
- ETSI GS QKD 014 標準介面
- 色散補償 (Chromatic dispersion compensation)
- 有限密鑰分析 (Finite-key analysis)

## RAMP: QKD as a Service (arXiv:2610.22879)

**標題**：RAMP: Toward Ubiquitous Quantum-Safe Key Distribution as a Service

### 核心概念
- **服務導向框架**：解耦 QKD 材料生成與密鑰消耗
- **QKD-as-a-Service**：將 QKD 作為雲端服務提供
- **基礎設施信任**：機密性僅依賴服務基礎設施的信任度

### 架構
```
QKD Material Generation (Service Provider)
    ↓
Key Consumption (End User)
    ↓
Confidentiality depends on infrastructure trust
```

## 集成光子學 QKD 原型 (arXiv:2602.17227)

**標題**：Quantum key distribution over a metropolitan network using an integrated photonics based prototype

### 核心成果
- **1.25 GHz** 高速 QKD 原型
- **集成光子學** (Integrated photonics)
- **19 英寸機架兼容** (Field-deployable)
- **城域網路**部署

### 技術細節
- 集成光子晶片
- 標準機架安裝
- 城域網路部署
- 高速密鑰生成

## QKD 網路演進

| 階段 | 時期 | 技術 | 規模 |
|------|------|------|------|
| 實驗室 | 2000s | BB84 點對點 | 單鏈路 |
| 城域 | 2010s | MDI-QKD | 城市網路 |
| 骨幹 | 2020s | TF-QKD | 國家網路 |
| 服務化 | 2026 | RAMP/QKDaaS | 全球服務 |

## 來源
- arXiv:2611.17265, 2610.22879, 2602.17227