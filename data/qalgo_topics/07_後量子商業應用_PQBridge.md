# Topic 7：後量子商業應用 — PQBridge 計畫

> 來源：本機 PQC/QKD 相關文件精簡整理
> 日期：2026-11-11

---

## 產品定位

- **PQBridge**：台灣金融科技與支付業者的 PQC 遷移平台
- 一個平台、四個模組：Assess（盤點）、Sandbox（SDK）、Advise（顧問）、Integrate（轉介）
- 灘頭堡客戶：金融科技與支付新創（20-200 人）

## 第一個 Golden Path

- 商戶 API 請求簽章 + 金鑰輪替
- ML-DSA 簽章 + X25519+ML-KEM 混合會話金鑰
- 7 天重疊期、可回滾

## 商業模式

- 固定價 PQC 就緒度評估：15-25 萬/案（30-40 小時）
- 遷移整合：30-50 萬/案
- 工作坊：5-8 萬/場
- 月度顧問 retainer：3-8 萬/月

## 12 個月目標

- 20 場訪談、3 個設計夥伴、5-8 個付費評估
- 2 個遷移整合案、1-2 個 retainer
- 營收 150-250 萬台幣
- SBIR 補助 150-250 萬

## 技術棧

- PQC 原語：liboqs / OpenSSL 3.5
- SDK：Python 3.11+ / TypeScript
- API：FastAPI
- Demo UI：Streamlit
- 容器：Docker

## 來源文件

- PQC金融商業計畫書.md
- 決策節點收斂表.md