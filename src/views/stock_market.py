"""💹 股市主題 — 蒸餾主題導讀（9 檔）＋ 台股本益比 viewer 工具項。

主題清單顯示於側邊欄（stock_market_sidebar），內文顯示於主畫面（render_stock_market）—
與 Quantum / Quant / YouTube / TI 同一展示模式（subtopics 一律 sidebar）。

來源：
  蒸餾主題 — ~/.opencode/skills/stock-market/references/*.md
             （11 本機來源檔 + 流光選股平台 8279 行蒸餾 + 2026-11-11 網路充實；
              由 push-streamlit/scripts/sync_topics.py 同步進 data/stock_topics/）
  工具項   — src/views/stock_vwr.py
             （📈 台股本益比 / 殖利率 / 股價淨值比查詢，TWSE 每日 BWIBBU_d；
              原獨立「📈 台股本益比」區塊併入本主題，避免兩處重複）
"""

import glob
import os

import streamlit as st

from src.views.doc_browser import render_doc_browser
from src.views.stock_vwr import render_stock_vwr

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STOCK_TOPICS_DIR = os.path.join(REPO_ROOT, "data", "stock_topics")
_VIEWER_KEY = "viewer"
_VIEWER_LABEL = "📈 台股本益比查詢（TWSE 每日）"

# 顯示名稱（新檔案自動 fallback 為檔名去尾）
_LABELS = {
    "00_主題總覽.md": "00 · 主題總覽（入口與路由）",
    "01_美股投資管道與標的.md": "01 · 美股投資管道與標的（三管道／VOO／量子ETF）",
    "02_台股基金與ETF比較.md": "02 · 台股基金與 ETF 比較（0050／0056／主動基金）",
    "03_期權入門.md": "03 · 期權入門（Call/Put／TXO／價差策略）",
    "04_投資心法.md": "04 · 投資心法（Klarman 8 鐵律／巴菲特蒙格）",
    "05_配對交易與動態Beta.md": "05 · 配對交易與動態 Beta（Y/X 經典配對／PyMC）",
    "06_開源量化工具鏈.md": "06 · 開源量化工具鏈（FinMind／yfinance／backtrader）",
    "07_量化投資平台架構.md": "07 · 量化投資平台架構（流光選股 8279 行導覽）",
    "08_自動化實盤決策節點.md": "08 · 自動化實盤決策節點（Shioaji／HFT／實盤三坑）",
}


def _list_stock_topics():
    """列出 data/stock_topics/*.md（同步後應有 9 檔；動態掃描容納日後新增）。"""
    return [
        os.path.basename(f)
        for f in sorted(glob.glob(os.path.join(STOCK_TOPICS_DIR, "*.md")))
    ]


def _entries():
    """側邊欄/主畫面共用的 (label, key) 清單：9 主題 + 台股本益比 viewer。

    主題項的 key 為相對 repo 根目錄的路徑；viewer 項為 "_VIEWER_KEY" 哨兵值。
    """
    files = _list_stock_topics()
    entries = [(_LABELS.get(n, n[:-3]), f"data/stock_topics/{n}") for n in files]
    entries.append((_VIEWER_LABEL, _VIEWER_KEY))
    return entries


def stock_market_sidebar():
    """側邊欄清單；回傳選定項 key（無主題檔時僅 viewer 一項）。"""
    entries = _entries()
    st.markdown("**💹 股市主題 — 導讀＋台股本益比**")
    labels = [e[0] for e in entries]
    selected = st.radio(f"共 {len(labels)} 項", labels, label_visibility="collapsed")
    for label, key in entries:
        if label == selected:
            return key
    return None


def render_stock_market(sel=None):
    """主畫面：顯示選定內容（sel 來自 stock_market_sidebar；預設第一項）。"""
    st.title("💹 股市主題（台股／美股／個股）")
    st.caption(
        "股市投資知識系統 — 美股管道、台股基金 ETF、期權、投資心法、配對交易、"
        "開源量化工具鏈、平台架構、實盤決策 ＋ 台股本益比查詢工具"
    )
    if not _list_stock_topics():
        st.warning(
            "找不到主題檔案：data/stock_topics/（push 前應由 sync_topics.py 同步）"
        )
    entries = _entries()
    if sel is None:
        sel = entries[0][1] if entries else _VIEWER_KEY
    if sel == _VIEWER_KEY:
        render_stock_vwr()
        return
    label = next((lbl for lbl, k in entries if k == sel), "")
    render_doc_browser(
        sel,
        key="stock_ref_chapter",
        caption=f"📂 {label} — 依 H2 章節導覽",
    )
