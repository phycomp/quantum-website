# Topic 1：台股實盤自動化交易（Shioaji API）

> 來源：本機量化交易、自動化相關文件精簡整理
> 日期：2026-11-11

---

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
