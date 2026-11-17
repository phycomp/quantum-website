# 05 多量子位元擴展與 QPU 架構

## 檔頭來源註記

- 本地來源：
  - `三目錄/04_量子計算總覽/量子硬體總覽.md`（DiVincenzo 準則第 6 條、效能評估）
  - `三目錄/04_量子計算總覽/基礎.md`（多量子位元、 Scale QPU）
  - `三目錄/04_量子計算總覽/量子硬體總覽.md`（Willow 架構、Scale 比特 QPU）
  - `量子/立體比特/QuantWare架構VIO.md`（VIO 3D 垂直互連）
  - `量子/立體比特/三維比特高密度讀取暨串擾.md`（Flip-Chip、高密度讀取）
  - `量子/立體比特/混合架構.md`（Transmon/Fluxonium/Quarton 混合、製程可行性）
  - `量子/立體比特/多量子串擾最優化.md`、`三維比特高密度讀取暨串擾.md`
  - `量子/超導比特/23比特運算.md`、`量子/超導比特/態演化五功能.md`
  - `量子/量子概念/02qubit製成.md`
- 網路充實（2026-11-17）：Academia Sinica 20-qubit (2026-01)；IOP QST 2025-12；Firgun 2026-07。

## 1. 擴展瓶頸

1. **Wiring bottleneck**：控制/讀取線數量隨 Qubit 數線性成長。
2. **ZZ 串擾**：Qubit 間殘餘耦合。
3. **頻率擁擠**：固定頻率架構的頻率碰撞。
4. **Capacitive loading**：Fluxonium 擴展時耦合電容受限。
5. **良率**：Josephson junction 參數分散。
6. **低溫控制**：Cryo-CMOS 整合。

## 2. 主流 QPU 架構

### 2.1 Google Willow / Sycamore

- **架構**：Transmon，2D 方格，tunable coupler。
- **Willow**：105 qubit，表面碼 QEC 示範。

### 2.2 IBM

- **Eagle/Condor/Heron**：Transmon，heavy-hex 拓撲。
- **Heron**：133 qubit，tunable coupler。

### 2.3 中研院

- **5 qubit → 20 qubit**（2023→2026），T₁ 15-30 μs → 530 μs。
- 8 吋晶圓 QC-Fab，雷射修頻 (laser trimming)。

### 2.4 QuantWare VIO

- **VIO-40K**：垂直互連，單處理器 10,000 qubit，密度提升 100 倍。
- 每個 Qubit 獨立垂直通道，長度一致、無擁擠。

### 2.5 Flip-Chip 3D 整合

- **Q-Chip**：Qubit + coupler。
- **C-Chip**：控制/讀取線路。
- 物理分離，簡化路由、抑制串擾。

## 3. 混合架構擴展

- **Fluxonium-Transmon 混合**（arXiv 2508.09267）：Fluxonium 資料位元 + Transmon 測量位元 + tunable coupler。
- ZZ 串擾 ~1 kHz，CZ ~30 ns，閉系統不忠實度低於相干極限。

## 4. 高密度讀取

- **3D 整合讀取**：Flip-Chip 讀取架構。
- **頻率多工**：單條線讀多 Qubit。
- **Cryo-CMOS**：低溫控制晶片整合。

## 5. 擴展策略比較

| 策略 | 優點 | 缺點 |
|---|---|---|
| 2D 方格 (Google/IBM) | 成熟、易布線 | 串擾、頻率擁擠 |
| Heavy-hex (IBM) | 降低連通度、減少串擾 | 深度增加 |
| VIO 3D (QuantWare) | 高密度、通道獨立 | 製程複雜 |
| 混合架構 | 長相干 + 快讀取 | 製程複雜 |

## 網路充實段（2026-11-17）

- Academia Sinica (2026-01-29)：20-qubit，T₁ 530 μs，雷射修頻、chip-stacking 降串擾。
- IOP QST (2025-12)：Fluxonium + tunable transmon coupler ZZ ~1 kHz，IPR 較 transmon 高。
- Firgun (2026-07)：矽量子點兩條路線擴展分析。

## 與其他子主題的接口

- → 02 超導：Fluxonium capacitive loading
- → 04 讀取：3D 讀取、Flip-Chip
- → 06 製程：TSV、flip-chip、8 吋晶圓
- → 07 控制/串擾：ZZ 串擾、頻率擁擠
- → 08 台灣：中研院 QPU、Phase 2
