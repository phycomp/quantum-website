# Topic 3：均線交叉策略（Moving Average Crossover）

> 來源：本機量化交易、自動化相關文件精簡整理
> 日期：2026-11-11

---

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
