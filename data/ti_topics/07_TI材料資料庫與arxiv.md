# 子主題 07：TI 材料資料庫與近期 arXiv 論文

> 本地來源：`拓撲/拓撲絕緣體材料分析.md`、`拓撲/高拓撲絕緣體.md`、`拓撲/三維拓撲絕緣體.md`、`指標/高通量TI.md`、`指標/自動化TI.md`、`指標/dftTI.md`
> 網路來源：arXiv (2023-2026)
> 日期：2026-11-12

## 1. 本地 TI 材料資料庫

### 1.1 已知 TI 材料家族

| 家族 | 代表材料 | 體隙 | 特性 | 來源 |
|------|----------|------|------|------|
| Bi₂Se₃ 家族 | Bi₂Se₃, Bi₂Te₃, Sb₂Te₃ | 0.15-0.3 eV | 第一代 3D TI，表面態 Dirac 錐 | 本地 `拓撲/mTI與afTI.md` |
| 磁性 TI | MnBi₂Te₄, MnBi₄Te₇, MnBi₆Te₁₀ | — | A 型反鐵磁，QAHE 候選 | 本地 `拓撲/mTI與afTI.md` |
| 拓撲晶體絕緣體 (TCI) | SnTe, Pb₁₋ₓSnₓTe | — | 鏡像對稱保護 | 本地 `拓撲/高拓撲絕緣體.md` |
| 量子自旋霍爾 (QSH) | HgTe/CdTe 量子阱, WTe₂ | — | 2D TI，helical edge states | 本地 `拓撲/三維拓撲絕緣體.md` |
| 拓撲半金屬 | Na₃Bi, Cd₃As₂ | — | Dirac/Weyl 點，費米弧 | 本地 `拓撲/拓撲三維.md` |

### 1.2 台灣製造生態
- **工研院**：國產 PQC 硬體 IP、TI 材料研究
- **華邦電子**：PQC-Safe 安全快閃記憶體 (W77Q)
- **中研院**：密碼學團隊 (Dilithium/Kyber)、FFT/NTT 實作
- **清華大學 + 中華電信**：QKD 商用光纖測試 (新竹→龍潭 10km)

### 1.3 高通量篩選方法
- 指標定理 (Fu-Kane-Mele Z₂, Wilson loop)
- DFT 計算 (VASP/Quantum ESPRESSO)
- 機器學習預測 (topological materials database)
- 本地腳本：`拓撲/指標/高通量TI.md`、`自動化TI.md`、`dftTI.md`

## 2. 近期 arXiv 論文 (2023-2026)

### 2.1 TI 材料資料庫與高通量篩選

| arXiv ID | 標題 | 作者 | 日期 | 重點 |
|----------|------|------|------|------|
| 2503.16276 | Machine Learning on Multiple Topological Materials Datasets | He, De Breuck, Weng, Giantomassi | 2025-03 | 多資料集 ML 預測 TI |
| 2311.18276 | 3D carbon allotropes: Topological quantum materials | Wang, Zhang, Zhang, Cheng | 2023-11 | 3D 碳同素異形體 TI |
| 2412.14296 | Theory of intervalley-coherent AFM order in tWSe₂ | Fischer, Klebl, Crépel, Ryee | 2024-12 | 扭轉 WSe₂ 拓撲超導 |

### 2.2 磁性 TI 與 QAHE

| arXiv ID | 標題 | 作者 | 日期 | 重點 |
|----------|------|------|------|------|
| 2503.13397 | Type-II quantum spin Hall insulator | Feng, Tan, Gao | 2025-03 | Type-II QSH 絕緣體 |
| 2303.06303 | (MnBi₂Te₄ 相關) | — | 2023-03 | MnBi₂Te₄ 磁性 TI |

### 2.3 TI 檢測與量測

| arXiv ID | 標題 | 作者 | 日期 | 重點 |
|----------|------|------|------|------|
| 2603.05025 | Topological Surface Charge Detection via Active Capacitive Compensation | Li, Wang, Zhang | 2026-03 | 4D 量子霍爾效應路徑 |
| 2603.11688 | Machine Learning of TI and Anderson Insulator in 1D SSH Chain | Yin, Ong | 2026-03 | ML 辨識 TI vs Anderson |

### 2.4 高通量計算

| arXiv ID | 標題 | 作者 | 日期 | 重點 |
|----------|------|------|------|------|
| 2509.13204 | High-throughput screening of spin Hall conductivity in 2D materials | Li, Liu, Chaudhary | 2025-09 | 2D 材料自旋霍爾電導篩選 |
| 2509.25371 | Design Principles for Topological Thermoelectrics | Skinner, Chakraborty, Scales | 2025-09 | 拓撲熱電設計原則 |
| 2501.02110 | High-throughput calculations of spin Hall conductivity | Zhou, Poncé, Charlier | 2025-01 | 非磁性 2D 材料自旋霍爾計算 |

## 3. 中國科研 (大陸) TI 研究

### 3.1 主要研究機構
- **清華大學** (北京)：拓撲材料實驗與理論
- **中國科學院物理研究所**：高品質 TI 薄膜 MBE 生長
- **復旦大學**：表面態 ARPES 量測
- **南京大學**：磁性 TI 與 QAHE
- **浙江大學**：拓撲相變與量子計算

### 3.2 代表性成果
- MnBi₂Te₄ QAHE 觀測（南京大學/清華大學合作）
- Bi₂Se₃ 高品質薄膜生長（中科院物理所）
- 拓撲超導體研究（復旦/浙大）
- 高通量 DFT 篩選（計算物理方向）

### 3.3 大陸研究特色
- 強調實驗與理論結合
- MBE/MOCVD 薄膜生長技術成熟
- ARPES/STM 量測能力強
- 與台灣（中研院/清華/交大）有合作空間

## 4. 台灣 TI 研究生態

### 4.1 主要機構
- **中研院**：密碼學 + 量子計算基礎研究
- **陽明交通大學**：半導體 + 量子元件
- **清華大學** (新竹)：QKD 實驗 + TI 材料
- **台灣大學**：理論物理

### 4.2 供應鏈
- **台積電**：先進製程，潛在 TI 元件製造
- **華邦電子**：PQC-Safe 安全晶片
- **工研院**：PQC 硬體 IP、TI 材料研究

## 5. TI 材料篩選工作流 (本地)

```python
# 本地高通量篩選流程 (指標/高通量TI.md)
1. DFT 計算 (VASP) → 能帶結構
2. Wilson loop / Z₂ 指標 → 拓撲分類
3. 表面態計算 → Dirac 錐確認
4. 熱力學穩定性 → 形成能 < 0
5. 實驗驗證 → ARPES/STM
```

## 6. 更新日誌
- 2026-11-12: 新增 TI 材料資料庫 + arXiv 論文 + 中國/台灣研究生態
