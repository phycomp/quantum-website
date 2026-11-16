# Topic 1：後量子密碼學（PQC）是什麼？

> 來源：本機 PQC/QKD 相關文件精簡整理
> 日期：2026-11-11

---

## 核心概念

- **PQC**（Post-Quantum Cryptography）：研究能抵禦量子電腦攻擊的密碼學分支
- 傳統公鑰密碼（RSA、ECC）的數學難題（大整數分解、離散對數）正是量子電腦最擅長解決的問題型態（Shor 演算法 1994）
- NIST 自 2016 年起舉辦 PQC 標準化競賽，2024 年 8 月完成三項標準

## NIST 三大標準（2024/8/13 正式發布）

| 標準 | 演算法 | 用途 | 重新命名 |
|------|--------|------|---------|
| **FIPS 203** | CRYSTALS-Kyber | 金鑰封裝（KEM） | ML-KEM |
| **FIPS 204** | CRYSTALS-Dilithium | 數位簽章 | ML-DSA |
| **FIPS 205** | SPHINCS+ | 數位簽章（雜湊基礎） | SLH-DSA |

## PQC 五大類別

1. **晶格密碼系統**（Lattice-based）— Kyber、Dilithium
2. **編碼密碼系統**（Code-based）— Classic McEliece
3. **雜湊函數密碼系統**（Hash-based）— SPHINCS+
4. **多變量密碼系統**（Multivariate）— Rainbow（已淘汰）
5. **超奇異橢圓曲線同源密碼系統**（Isogeny-based）— SIKE（已淘汰）

## NIST 競賽重點

- 2016 年開始徵集，82 組投稿，69 件合格
- 中研院團隊參與：Rainbow（多變量簽章）、Classic McEliece（編碼）、SPHINCS+（雜湊）、NTRU Prime
- Kyber 因專利爭議，NIST 最終花錢買下專利並選擇 Kyber 為勝利者
- 中研院倪儒本老師為 SPHINCS+ 共同提出者

## 實作重點

- PQC 演算法運行在傳統運算平台上，同時抵擋傳統與量子攻擊
- 混合式方案：ECDSA + ML-DSA 雙重簽章（如 nQrux 安全開機）
- Xiphera、SiFive/PQShield 等廠商已提供 PQC IP 核心
- 台灣：工研院開發國產 PQC 硬體 IP，華邦電子推出 PQC-Safe 安全晶片

## 來源文件

- PQC專欄.md（數理科學 科普專欄，楊柏因研究員）
- PQC演算法為未來作準備.md（EDN 主編 Majeed Ahmad）
- PQC軟硬體基礎建設.md（KEM 混合建構技術架構）