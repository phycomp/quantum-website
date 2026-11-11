# Topic 4：HNDL 威脅 — 現在收集，以後解密

> 來源：本機 PQC/QKD 相關文件精簡整理
> 日期：2026-11-11

---

## 什麼是 HNDL？

- **H**arvest **N**ow, **D**ecrypt **L**ater
- 攻擊者現在攔截並儲存加密流量
- 等量子電腦成熟後（預計 10-15 年）再解密
- 長期機密（20-30 年）已經在被收集

## 為什麼迫在眉睫？

- 許多高度機密數據的機密生命週期長達 20-30 年
- 等量子電腦誕生後才更換加密技術，已經太晚
- 全球科技巨頭已開始導入 PQC（iMessage PQ3、Signal PQXDH、Chrome TLS）

## 防禦策略

- **PQC 升級**：軟體層面的抗量子演算法
- **QKD 部署**：硬體層面的量子安全通道
- **混合模式**：兩者並用，互為備援

## 日常通訊軟體的 PQC 升級

- **Apple iMessage（PQ3）**：Level 3 安全性，動態金鑰自動更新
- **Signal（PQXDH）**：引入 ML-KEM（Kyber）
- **Google Chrome/Android**：TLS 協定大量啟用 PQC

## 混合加密模式

- 第一層：傳統密碼（X25519/ECC）
- 第二層：後量子密碼（ML-KEM/Kyber）
- 黑客必須同時破解兩種才能偷看訊息

## 來源文件

- QKD密鑰分發.md（HNDL 威脅章節）
- PQC演算法為未來作準備.md（HNDL 威脅說明）