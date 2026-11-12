# 09 · QuantX 平台與量化課程（新創平台研究）

> 來源：網路公開資訊（查證日期 2026-11-12）+ 本機量化資料夾（`~/量化/`）內既有量化平台/決策節點蒸餾
>   - QuantX 官網：https://quantx.com.tw/（首頁為 WordPress WooCommerce 示範模板，內容稀疏；實際資訊散見於 Podcast/YouTube/社群）
>   - QuantX.asia（大陸站，面向個人投資者）：https://quantx.asia/ — 「讓複雜的量化變得簡單」
>   - YouTube 頻道「Quant X 量化思維」：https://www.youtube.com/@QuantXTW（58 訂閱 / 2 影片，規模初階）
>   - Apple Podcast「#18 創業系列：股票量化交易新創 QuantX」（Moonshot 射月計畫 Tony & Jason 主持，feat. 清交小學弟組合）
> 相關本機蒸餾：`references/06_開源量化工具鏈.md`、`references/07_量化投資平台架構.md`、`references/08_自動化實盤決策節點.md`
> ⚠️ 本檔為「平台/課程研究」，非投資建議；QuantX 績效宣稱未經第三方稽核，僅作參考。

---

## 一、QuantX 是什麼

**QuantX（量化思維）** 是由「海內外致力於數據探索金融市場的量化交易開發者」創立的**量化交易新創**（2021 年創立），定位為：

- **個人投資者導向**的量化教育/社群平台（非券商、非投顧持牌機構）
- 核心主張：「投資邏輯而非複雜操作」— 用 AI 建立自己的交易策略，提升長期投資績效
- 公開活動：量化投資實戰分享會（含 AI 建立交易策略、提升長期績效邏輯）
- 聯絡：team@quantx.com.tw；客服專線 02-2508-0945（台灣）

**規模線索**（公開可查，2026-11-12）：
- YouTube 頻道「Quant X 量化思維」：58 訂閱 / 2 支影片（初階、非主流）
- QuantX.asia（大陸站）：面向個人投資者，QMT / PTrade 工具學習 + 知識/開發/研究生態
- Podcast 曝光：Moonshot 射月計畫 EP12「大學就能創造被動收入！！！如何踏入量化交易」（討論從零到一進入量化交易、新手 Q&A）
- Podcast EP18「創業系列：股票量化交易新創 QuantX 如何從 2 人到 10 人團隊」（feat. 清交小學弟組合）

**宣稱績效**：「從 2021 年創立至今績效持續優於大盤」— **未附回測/稽核細節**，需自行求證；所有交易均有風險，過往績效不保證未來獲利。

---

## 二、QuantX vs 本機「流光選股」平台 vs 其他量化平台

| 維度 | QuantX（新創課程/社群） | 流光選股（本機平台，`~/量化/`） | XQ 全球贏家 | TEJ TQuant Lab |
|------|------------------------|------------------------------|------------|----------------|
| 定位 | 量化教育/社群/分享會 | 台股高資產投資人自用 Python 量化系統 | 台灣第一套自主研發自動化程式交易平台 | TEJ 採 Quantopian 架構延伸的回測平台 |
| 目標客群 | 個人投資者（新手～進階） | 資金 1,000 萬+、進階、45–55 歲資產鞏固期 | 一般散戶/程式交易者 | 量化研究者/法人 |
| 技術棧 | AI 建立策略（具體未公開） | Python + yfinance + Streamlit + 多券商 API | XQ 語法平台 + 券商下單 | Python + TEJ 資料庫 |
| 數據源 | 未公開 | 免費（yfinance + 台灣證交所），無需 Token | 即時報價（XQ） | TEJ 付費資料 |
| 回測 | 未公開 | backtrader + 多因子權重優化 | 模擬交易 | TQuant Lab 回測引擎 |
| 風控 | 未公開 | RiskGate + VaR/夏普/最大回撤/Beta | 依策略自設 | 依策略自設 |
| 成本 | 課程/分享會（費用未公開） | 自建（免費數據源） | 平台費/券商手續費 | 資料費 + 平台費 |
| 公開透明度 | 低（官網模板化、YouTube 2 影片） | 高（本機 8,279 行蒸餾導覽） | 中（老牌、文件齊） | 中（學術/法人導向） |

**判讀**：QuantX 目前公開可得資訊極少（官網為 WooCommerce 示範模板、YouTube 2 影片），**無法驗證其績效與技術深度**；本機「流光選股」平台反而有完整蒸餾導覽（`references/07`）可追溯。投資者若要學習量化，建議先走開源工具鏈（`references/06`）+ 本機平台架構，再視需求付費課程。

---

## 三、量化平台選型 checklist（給個人投資者）

1. **數據源**：免費（yfinance/TEJ 免費層）vs 付費（TEJ/Bloomberg）；台股需注意 TWSE BWIBBU、法人買賣超。
2. **回測引擎**：backtrader / vnpy / TQuant Lab；注意存活者偏差、前視偏差、滑價/手續費。
3. **執行層**：券商 API（富邦/Shioaji/永豐/群益/IB）；HFT 需 C++ + 共置；散戶用 Python 輪詢即可。
4. **風控**：VaR、夏普、最大回撤、Beta、相關性矩陣、RiskGate 閘道。
5. **部署**：本機/Streamlit/Cloudflare；實盤三坑見 `references/08`。
6. **透明度**：是否公開回測程式碼與績效稽核；QuantX 目前未公開 → 需自行求證。

---

## 四、QuantX 相關公開資源索引

- 官網：https://quantx.com.tw/（首頁為 WordPress WooCommerce 示範模板，內容稀疏）
- 大陸站：https://quantx.asia/（「讓複雜的量化變得簡單」，QMT/PTrade 工具學習）
- YouTube：https://www.youtube.com/@QuantXTW（Quant X 量化思維，58 訂閱 / 2 影片）
- Instagram：@quantx_official
- Podcast EP12（Moonshot 射月計畫）：https://www.youtube.com/watch?v=891_iIt2s4M
- Podcast EP18（創業系列，feat. 清交小學弟組合）：Apple Podcasts
- 聯絡：team@quantx.com.tw / 02-2508-0945

---

## 五、網路充實（2026-11-12）

- QuantX 官網首頁為 WooCommerce 示範模板（YITH Wonder 主題），實際內容極少；`/about`、`/blog` 皆為 placeholder 文字。
- QuantX.asia（大陸站）較完整，定位「面向個人投資者的量化技術生態」，提供 QMT/PTrade 工具學習。
- 公開可查的 QuantX 績效宣稱「持續優於大盤」**未附回測/稽核細節**，不可當定案事實（爭議標註）。
- 本機 `~/量化/` 已有完整量化平台蒸餾（8,279 行）+ 決策節點實錄，是更可靠的學習起點。
- 相關 ETF/標的：QTUM（Defiance Quantum ETF，NASDAQ，管理費 0.40%，89 檔持股，追蹤 BlueStar Quantum Computing and Machine Learning Index）— 詳見 `stock-analysis` 報告。

---

## 六、與其他 references 的關係

- `references/06_開源量化工具鏈.md`：FinMind/yfinance/TuShare/backtrader/vnpy/TEJ 開源 API
- `references/07_量化投資平台架構.md`：流光選股平台五層模組導覽
- `references/08_自動化實盤決策節點.md`：D0–D7 決策節點、Shioaji、HFT、實盤三坑
- 本檔（09）：外部量化平台/課程研究（QuantX）+ 選型 checklist

 Base directory note: 本檔新增後，stock_topics 應同步為 10 檔（原 9 + 本檔）。
