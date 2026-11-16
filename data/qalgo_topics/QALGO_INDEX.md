# Qalgo — 量子算法與密碼學蒸餾成果

> 整合目錄：PQC (後量子密碼) + QKD (量子金鑰分發) + ECC (橢圓加密) + Quantum Algorithms

## 目錄結構

```
qalgo/
├── QALGO_INDEX.md          # 本索引
├── PQC/                    # 後量子密碼 (Post-Quantum Cryptography)
│   ├── 00_索引.md
│   ├── 01_PQC基礎.md
│   ├── 02_QKD量子金鑰分發.md
│   ├── 03_PQC_vs_QKD.md
│   ├── 04_HNDL威脅.md
│   ├── 05_台灣PQC_QKD進展.md
│   ├── 06_多通道平行QKD.md
│   ├── 07_後量子商業應用_PQBridge.md
│   ├── 08_Signal協定PQC優化.md
│   ├── 09_後量子晶片與硬體安全.md
│   ├── 10_HNDL威脅與日常防禦.md
│   ├── 11_台灣PQC_QKD雙軌策略.md
│   ├── 12_橢圓加密.md
│   ├── 13_量子演算法原理與應用.md
│   └── fb_posts/           # 臉書貼文
├── QKD/                    # 量子金鑰分發 (Quantum Key Distribution)
│   ├── 00_索引.md
│   ├── 01_Quantum_Algorithms.md
│   ├── 02_Shors_Algorithm.md
│   ├── 03_QAOA.md
│   ├── 04_QKD_Basics.md
│   ├── 05_QKD_Networks.md
│   ├── 06_QKD_Security.md
│   └── 07_QKD_Verification.md
├── ECC/                    # 橢圓加密 (Elliptic Curve Cryptography)
│   ├── ECC橢圓加密數學原理.md
│   ├── ECC加解密.md
│   ├── ECC教學.py
│   ├── ECC橢圓加密模擬.py
│   ├── ECC實現1.py
│   ├── ECC實現2.py
│   ├── PKI加密算法.md
│   ├── PQC專欄.md
│   ├── PQC演算法為未來作準備.md
│   ├── QKD密鑰分發.md
│   ├── 公鑰標準制定.md
│   ├── 橢圓加密簡介.md
│   ├── 量子密碼學.md
│   ├── 量子密碼學II.md
│   ├── 量子密碼光偏振.md
│   └── 量子圖像加密.md
└── quantum-algorithms/     # 量子算法 (同 QKD 目錄)
```

## 主題概述

### PQC (Post-Quantum Cryptography)
後量子密碼學是為了抵禦量子計算攻擊而設計的密碼算法。NIST 已發布 FIPS 203 (ML-KEM)、FIPS 204 (ML-DSA)、FIPS 205 (SLH-DSA) 標準。

**關鍵威脅**: Shor's algorithm 可在 10,000 原子量子位元上執行，威脅 RSA/ECC。

### QKD (Quantum Key Distribution)
利用量子力學原理實現信息理論安全的密鑰交換。2026 年已部署 4 城市糾纏 QKD 網路。

**主要協議**: BB84, E91, CV-QKD, MDI-QKD, TF-QKD

### ECC (Elliptic Curve Cryptography)
橢圓曲線密碼學，提供比 RSA 更短的密鑰長度和更高的安全性。是當前主流公鑰密碼系統。

**數學基礎**: 橢圓曲線上的離散對數問題 (ECDLP)

### Quantum Algorithms
量子算法利用量子疊加和糾纏實現計算加速。Shor's (指數加速)、Grover's (平方加速)、QAOA (組合優化)。

## 本地來源映射

| 主題 | 來源目錄 | 檔案數 |
|------|----------|--------|
| PQC | /home/sam/量子/PQC/ | ~25 |
| QKD | /home/sam/quantum-algorithms-qkd/ | 8 |
| ECC | /home/sam/量子/橢圓加密/ | ~20 |
| Quantum Algorithms | /home/sam/quantum-algorithms-qkd/ | 8 (同 QKD) |

## Streamlit 展示

已整合至 distill-showcase (http://localhost:8502)

## 相關技能
- quantum-algorithms-qkd
- dao-classics (古典哲學)
- topological-insulator (拓撲絕緣體)
path">
/home/sam/qalgo/QALGO_INDEX.md