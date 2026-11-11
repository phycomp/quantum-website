# Topic 6：多通道平行 QKD（設備、製程、廠商）

> 來源：本機 PQC/QKD 相關文件精簡整理
> 日期：2026-11-11

---

## 四維度多工架構

1. **波長多工（WDM）**：16-64 通道
2. **空間多工（SDM）**：多芯光纖 / 自由空間
3. **時間多工（TDM）**：時槽交錯
4. **偏振/模式多工（PDM）**：雙偏振 / 軌道角動量

## 關鍵設備與廠商

| 設備 | 主要廠商 |
|------|---------|
| 量子點單光子源陣列 | Quandela（法）、QD Laser（日）、Single Quantum（荷） |
| 弱相干光脈衝雷射 | ID Quantique（瑞）、Toshiba（日）、QuantumCtek（中） |
| SNSPD 陣列 | 上海微系統所、MIT Lincoln Lab、NIST |
| DWDM 多工器 | Coherent、Lumentum、NeoPhotonics |
| 多芯光纖 | NTT、Prysmian、長飛光纖 |
| FPGA 處理板 | Xilinx（AMD）、Altera（Intel） |
| 低溫冷卻系統 | Bluefors、Janis Research |

## 製程整合

- **矽光子整合製程**：SOI 晶圓 → 波導蝕刻 → 多工器製作 → 調變器整合 → 光纖耦合
- **超導電路製程（SNSPD）**：NbN/WSi 薄膜 → 電子束微影 → 蝕刻 → 光學腔體

## 效能預估

| 配置 | 通道數 | 總金鑰率 | 傳輸距離 |
|------|--------|---------|---------|
| 基礎型 | 4 通道 WDM | 4 Mbps | 50 km |
| 標準型 | 16 通道 WDM + 4 芯 MCF | 640 Mbps | 25 km |
| 高效型 | 64 通道 WDM + SNSPD 陣列 | 3.2 Gbps | 10 km |
| 旗艦型 | 256 通道混合多工 + 量子中繼 | 25.6 Gbps | 100+ km |

## 來源文件

- QKD密鑰分發.md（多通道平行 QKD 章節）