# Topic 10：HNDL 威脅與日常防禦

> 來源：本機 PQC/QKD 相關文件精簡整理
> 日期：2026-11-11

---

## HNDL（Harvest Now, Decrypt Later）

- 攻擊者現在攔截並儲存加密流量
- 等量子電腦成熟（10-15 年）再解密
- 長期機密（20-30 年）正在被收集
- 國家級黑客的現實威脅

## 為什麼迫在眉睫？

- 許多高度機密數據的機密生命週期長達 20-30 年
- 等量子電腦誕生後才更換加密技術，已經太晚
- 全球科技巨頭已開始導入 PQC（iMessage PQ3、Signal PQXDH、Chrome TLS）

## 日常通訊軟體的 PQC 升級

### Apple iMessage（PQ3）
- Level 3 安全性
- 動態金鑰自動更新
- 即使某一條訊息的金鑰被破解，後續訊息也會立刻更換新金鑰

### Signal（PQXDH）
- 將傳統的 X3DH 升級為 PQXDH
- 直接引入 ML-KEM（Kyber）演算法

### Google Chrome/Android
- 網頁傳輸協定（TLS）大量啟用 PQC
- 雙方默默在使用抗量子密碼保護流量

## 混合加密模式

- 第一層：傳統密碼（X25519/ECC）
- 第二層：後量子密碼（ML-KEM/Kyber）
- 黑客必須同時破解兩種才能偷看訊息

## 密碼敏捷性（Crypto-agility）

- 讓系統能像換外殼一樣快速抽換演算法
- 企業在升級系統時會遇到的工程挑戰
- 美國 NIST 公布的 ML-KEM / ML-DSA 標準演算法

## 來源文件

- QKD密鑰分發.md（HNDL 威脅章節）
- PQC演算法為未來作準備.md（HNDL 威脅說明）