# 量化交易 & 自動化 — 主題整理
> 來源：本機所有量化交易、自動化相關文件精簡整理
> 日期：2026-11-11

---

## Topic 1：台股實盤自動化交易（Shioaji API）

### 核心概念
- 使用**永豐金 Shioaji API** 進行台股即時自動交易
- 事件驅動架構：`set_on_tick_fop_cb` 訂閱即時行情，券商主動推送 Tick 資料
- 策略：移動平均線黃金交叉/死亡交叉（MA Crossover）

### 系統架構
```
登入認證 → TWCA 憑證啟用 → 訂閱即時行情 → on_tick_callback → 策略判斷 → 下單執行
```

### 關鍵技術
- **非同步事件驅動**：不頻繁輪詢，由券商主動推送，避免 API 被封鎖
- **嚴格型別**：`StockOrderLot.Common`（整股）、`OrderType.ROD`（當日有效）、`PriceType.LMT`（限價）
- **滑價保護**：買進時 `current_price + 0.5`，賣出時 `current_price - 0.5`
- **持倉追蹤**：`has_position` 布林值追蹤持倉狀態

### 程式碼範例
```python
import shioaji as sj
from shioaji.constant import Action, StockOrderLot, OrderType, PriceType

api = sj.Shioaji()
api.login(person_id="YOUR_ID", password="YOUR_PASSWORD")
api.activate_ca(ca_path="cert.pfx", ca_passwd="PASS", person_id="YOUR_ID")

contract = api.Contracts.Stocks["2330"]  # 台積電
order = api.Order(action=Action.Buy, price=100.0, quantity=1,
                  order_lot=StockOrderLot.Common, order_type=OrderType.ROD,
                  price_type=PriceType.LMT)
trade = api.place_order(contract, order, account=api.stock_account[0])
```

### 風控機制（待加入）
- 停損/停利（Take Profit / Stop Loss）
- 最大持倉限制
- 每日交易次數限制

---

## Topic 2：量化分析 API 與工具鏈

### 資料獲取 API
| API | 市場 | 說明 |
|-----|------|------|
| **FinMind** | 台股/美股 | 台灣開源金融大數據 API，50+ 種數據 |
| **yfinance** | 全球 | Yahoo Finance，K 線、除權息、基本面 |
| **TuShare** | A 股 | 免費金融大數據接口 |

### 回測與策略框架
| 框架 | 用途 | 說明 |
|------|------|------|
| **backtrader** | 回測 | 最受歡迎的 Python 量化回測框架 |
| **vnpy** | 交易平台 | 從回測到實盤交易的完整框架 |
| **pyfolio** | 績效分析 | 夏普比率、最大回撤等分析圖表 |
| **TEJAPI** | 台灣市場 | 台灣經濟新報 API 範例庫 |

### 台灣券商 API 串接
- **永豐金 Shioaji**：REST API，支援 Tick 訂閱、下單、帳務查詢
- **群益期貨**：需自行開發 Gateway，繼承 BaseGateway
- **vnpy 整合**：將券商 API 包裝為 VN.PY 的 BaseGateway

### 開發流程
```
資料獲取 → 策略撰寫與回測 → 風險與績效評估 → 實盤部署
```

---

## Topic 3：均線交叉策略（Moving Average Crossover）

### 策略邏輯
- **快線**：最新 N 筆收盤價平均（如 5 筆）
- **慢線**：最新 M 筆收盤價平均（如 10 筆）
- **黃金交叉**：快線 > 慢線 → 買進
- **死亡交叉**：快線 < 慢線 → 賣出

### 實作範例
```python
fast_ma = sum(price_history[-5:]) / 5
slow_ma = sum(price_history[-10:]) / 10

if fast_ma > slow_ma and not has_position:
    execute_order(Action.Buy, current_price + 0.5)
    has_position = True
elif fast_ma < slow_ma and has_position:
    execute_order(Action.Sell, current_price - 0.5)
    has_position = False
```

### 風險考量
- 均線交叉為落後指標，可能在趨勢末端進場
- 需加入停損/停利機制
- 建議加入成交量過濾條件

---

## Topic 4：高頻交易策略（台指期貨）

### 策略特性
- **零預測、高機械化**：不預測市場方向，純機械執行
- **保守估計績效**：平均每分鐘獲利 30 點、每分鐘成交 2.3 筆
- **無保證金下單**：透過群益 API 進行模擬測試

### 技術需求
- Python 非同步控制（asyncio）
- 群益期貨 API 串接經驗
- Tick 數據即時處理
- 系統調優與參數最佳化

### 合作模式
- 策略邏輯已由 Python 撰寫完畢
- 徵求群益 API 串接合作夥伴
- 雙方簽署 NDA 與正式合作合約
- 分潤條款由合作夥伴主動提出

---

## Topic 5：量化投資平台架構

### 平台組成
- **資料層**：歷史行情、基本面、籌碼面
- **策略層**：策略開發、回測引擎
- **執行層**：券商 API 串接、下單執行
- **風控層**：停損停利、持倉管理、資金管理
- **監控層**：績效追蹤、警報通知

### 台灣市場特色
- **TEJ API**：台灣經濟新報，提供台股、期貨、選擇權數據
- **FinMind**：開源金融大數據 API
- **Shioaji**：永豐金 API，支援台股現貨與期貨
- **群益 API**：期貨下單與行情

### 部署架構
- Python 3.11+ 後端
- FastAPI / Streamlit 前端
- Docker 容器化
- PostgreSQL 資料庫

---

## Topic 6：自動化交易系統設計

### 核心模組
1. **登入與認證**：券商 API 登入、TWCA 電子憑證啟用
2. **行情訂閱**：即時 Tick 數據接收與處理
3. **策略引擎**：技術指標計算、信號生成
4. **下單執行**：委託單建立與送出
5. **風控管理**：停損停利、持倉追蹤
6. **日誌記錄**：交易紀錄、績效追蹤

### 最佳實踐
- **事件驅動**：使用回調函式而非輪詢
- **嚴格型別**：使用券商 API 定義的常數
- **滑價保護**：限價單加入滑價緩衝
- **記憶體管理**：限制歷史數據陣列長度
- **錯誤處理**：API 斷線重連、下單失敗重試

---

## Topic 7：量化市場分析（YouTube/內容）

### 競爭分析
| 主題 | 主要頻道 | 訂閱數 | 競爭度 |
|------|----------|--------|--------|
| 量子演算法 | Quantum Computing (Hiu-Yung Wong) | 19,700 | 中 |
| PQC | Cryptography 101 | 7,260 | 中 |
| QKD | Ramona Wolf | 1,040 | 低 |

### 內容支柱
- 量子演算法（40%）
- PQC（35%）
- QKD（25%）

### 關鍵字
quantum computing, quantum algorithm, Shor, Grover, PQC, post-quantum cryptography, Kyber, Dilithium, QKD, BB84, quantum key distribution

---

## Topic 8：自動化工程（渲染/製程）

### Arduino 風力發電機組
- 3D 列印葉片（ASA/PETG 材料）
- 無刷馬達/發電機
- Arduino MPPT 控制器
- 儲能系統

### 拓撲量子物態與快速材料預測
- Streamlit 介面
- systemd 定時執行
- 高通量篩選服務

### 渲染自動化
- HyperFrames HTML→MP4 渲染
- FFmpeg 轉場特效
- GSAP 動畫同步

---

## 附錄：關鍵文件清單

| 文件 | 路徑 | 說明 |
|------|------|------|
| 自動化交易範例 | `/home/sam/量化/自動化.py` | Shioaji API 實盤自動交易 |
| 量化 API 推薦 | `/home/sam/量化/量化API.md` | GitHub 量化分析開源項目 |
| 量化開發規格 | `/home/sam/量化/開發量化規格.md` | 期貨策略合作徵求 |
| 量子市場分析 | `/home/sam/軟體/代理人/docs/QUANTUM_MARKET_ANALYSIS.md` | YouTube 頻道競爭分析 |
| 自動化耦合優化 | `/home/sam/渲染邏輯/Oloid/優化自動化全耦合.md` | Arduino 風力發電機組 |
| 拓撲量子物態 | `/home/sam/物理模擬/topo/指標/自動化TI.md` | 快速材料預測部署包 |
| 擴充自動化 | `/home/sam/軟體/代理人/pages/03擴充自動化.py` | Streamlit 擴充頁面 |
| 量子內容模板 | `/home/sam/軟體/代理人/content_templates/quantum.md` | 量子傳輸線內容模板 |

---

*本文件整理自本機所有「自動化、交易、量化、quant」相關文件。*
*整理日期：2026-11-11*