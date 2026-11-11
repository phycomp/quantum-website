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

## 附錄：Shioaji 實盤自動交易範例程式碼

> 來源：~/量化/自動化.py（RealTimeTradingBot 完整實作）

```python
# 💻 台灣市場實盤自動化交易範例
import time
from datetime import datetime
import shioaji as sj
from shioaji.constant import Action, StockOrderLot, OrderType, PriceType

class RealTimeTradingBot:
    def __init__(self):
        # 1. 初始化 Shioaji API 引擎
        self.api = sj.Shioaji()
        self.target_code = "2330"  # 交易標的：台積電
        
        # 2. 策略變數設定
        self.price_history = []    # 存放最新收盤價的陣列
        self.fast_window = 5       # 實盤短均線（例如：以最新 5 筆 Tick 價格計算）
        self.slow_window = 10      # 實盤長均線
        self.has_position = False  # 簡易持倉狀態追蹤（實盤中應由券商帳務查詢更新）

    def login_and_activate(self, user_id, password, certificate_path, cert_password):
        """步驟一：帳號登入與 TWCA 電子憑證啟用"""
        print(f"[{datetime.now()}] 正在登入永豐金 API...")
        self.api.login(person_id=user_id, password=password)
        
        print(f"[{datetime.now()}] 正在啟用下單憑證...")
        self.api.activate_ca(
            ca_path=certificate_path,
            ca_passwd=cert_password,
            person_id=user_id
        )
        print("系統初始化成功，準備進入市場。")

    def execute_order(self, action: Action, price: float, qty: int = 1):
        """步驟四：下單執行模組"""
        # 尋找台股現貨合約
        contract = self.api.Contracts.Stocks[self.target_code]
        
        # 建立委託單設定 (設定買賣動作、張數、限價、整股交易、當日有效)
        order = self.api.Order(
            action=action,
            price=price,
            quantity=qty,
            order_lot=StockOrderLot.Common,
            order_type=OrderType.ROD,
            price_type=PriceType.LMT
        )
        
        print(f"🚨 [策略訊號觸發] 動作: {action.name}, 價格: {price}, 數量: {qty} 張")
        
        # 透過券商帳戶（預設第一個帳戶）送出委託
        trade = self.api.place_order(contract, order, account=self.api.stock_account[0])
        return trade

    def on_tick_callback(self, exchange, tick):
        """步驟三：即時行情回報接收 (每當市場有最新成交，API 會自動觸發此函式)"""
        # 排除非交易期間的雜訊
        if tick.close == 0:
            return
            
        current_price = float(tick.close)
        self.price_history.append(current_price)
        
        # 維持陣列長度，避免記憶體無限膨脹
        if len(self.price_history) > self.slow_window:
            self.price_history.pop(0)
            
        # 檢查資料量是否足夠計算均線
        if len(self.price_history) < self.slow_window:
            print(f" 正在收集即時數據... ({len(self.price_history)}/{self.slow_window}) 目前價: {current_price}", end="\r")
            return

        # 計算當前的快線與慢線
        fast_ma = sum(self.price_history[-self.fast_window:]) / self.fast_window
        slow_ma = sum(self.price_history[-self.slow_window:]) / self.slow_window
        
        print(f"[{datetime.now().strftime('%H:%M:%S')}] 價格: {current_price} | 快線: {fast_ma:.2f} | 慢線: {slow_ma:.2f}")

        # 核心策略邏輯判斷
        if fast_ma > slow_ma and not self.has_position:
            # 黃金交叉 ──> 限價買進（以當前成交價加 1 檔做為滑價保護）
            target_price = current_price + 0.5 
            self.execute_order(Action.Buy, target_price)
            self.has_position = True
            
        elif fast_ma < slow_ma and self.has_position:
            # 死亡交叉 ──> 限價賣出（以當前成交價減 1 檔）
            target_price = current_price - 0.5
            self.execute_order(Action.Sell, target_price)
            self.has_position = False

    def start_trading(self):
        """步驟二：訂閱即時行情，啟動自動交易"""
        contract = self.api.Contracts.Stocks[self.target_code]
        if not contract:
            print("找不到該股票代碼，請確認市場是否開盤或代碼正確。")
            return
            
        print(f"\n📡 開始訂閱 {contract.name} ({self.target_code}) 即時逐筆行情...")
        
        # 設定回撥函式：當有最新成交 (Ticks) 時，呼叫 self.on_tick_callback
        self.api.quote.set_on_tick_fop_cb(self.on_tick_callback)
        self.api.quote.subscribe(contract, quote_type=sj.constant.QuoteType.Tick, version=sj.constant.QuoteVersion.v1)

        # 讓主程式持續運行，直到手動中斷 (Ctrl+C)
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n關閉交易程式，解除行情訂閱...")
            self.api.quote.unsubscribe(contract, quote_type=sj.constant.QuoteType.Tick, version=sj.constant.QuoteVersion.v1)
            self.api.logout()

# ─── 執行區塊 ───
if __name__ == "__main__":
    # 請替換為您的真實券商與憑證資訊
    USER_ID = "YOUR_ROC_ID"             # 身分證字號
    PASSWORD = "YOUR_API_PASSWORD"       # API 密碼
    CERT_PATH = "C:/Cert/sinotrade.pfx"  # 憑證絕對路徑
    CERT_PASS = "YOUR_CERT_PASSWORD"     # 憑證密碼

    # 實例化機器人
    bot = RealTimeTradingBot()
    
    # 啟動系統 (注意：若要在非盤中時間測試，可切換至永豐金的 Simulation 模擬環境)
    # bot.api.simulation = True # 如需模擬測試請打開此行
    
    bot.login_and_activate(USER_ID, PASSWORD, CERT_PATH, CERT_PASS)
    bot.start_trading()
"""
💡 程式碼關鍵亮點解析
    1. set_on_tick_fop_cb (非同步事件驅動)：這與回測程式碼不同。實盤時，我們不用 while True 去頻繁向券商伺服器要價格（那會導致 API 被封鎖），而是採用訂閱模式，當交易所一有最新成交，券商會主動將資料推送到您的 on_tick_callback 函式。
    2. shioaji.constant 的嚴格型別：實盤下單若參數代錯（例如整股買賣代成零股），券商伺服器會直接拒絕。範例中使用了 StockOrderLot.Common（整股）和 OrderType.ROD（當日有效單），確保完全符合台股交易規範。
    3. 滑價與限價保護：在範例的下單模組中，買進時將 current_price + 0.5。這是因為在即時行情中，若用精準的「當前價」下限價單，很可能因為價格跳動而無法立刻成交，稍微加價能提高實盤的撮合成功率。
請問您想將這個範例改為模擬環境（Simulation Mode）進行無風險測試，還是需要幫您加入自動停損與停利（Take Profit / Stop Loss）的風控機制呢？
AI 回覆可能有誤。如需財務建議，請諮詢專業人士。 瞭解詳情
"""

```

---
