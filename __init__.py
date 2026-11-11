"""Quantum Website — 統一入口：Quantum / Quant / STL 3D / 股市主題 / YouTube / 量子傳輸線 / 拓撲絕緣體。

架構（2026-11-11 重構；同日擴充 3 區塊；股市主題併入台股本益比 viewer）：
  單一 app.py 入口 + 側邊欄分區 + src/views/ 函式模組。
  不使用 pages/ 自動多頁（先前在 Streamlit Cloud 造成 StreamlitAPIException，
  已移除）；st.set_page_config 只在此檔呼叫一次。
  __init__.py 與本檔內容同步（支援 streamlit run __init__.py）。
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import streamlit as st

from src.content_loader import search_content
from src.views.quantum_topics import quantum_sidebar, render_quantum
from src.views.quant_topics import quant_sidebar, render_quant
from src.views.stl_viewer import render_stl
from src.views.stock_market import render_stock_market, stock_market_sidebar
from src.views.yt_posts import render_youtube, yt_sidebar
from src.views.quantum_tline import render_tline
from src.views.ti_topic import render_ti, ti_sidebar

st.set_page_config(page_title="Quantum Website", layout="wide")

SECTIONS = [
    "🏠 首頁",
    "📚 Quantum 主題",
    "📊 Quant 主題",
    "🧊 STL 3D 模型",
    "💹 股市主題",
    "📺 YouTube 上傳貼文",
    "🔗 量子傳輸線",
    "🧪 拓撲絕緣體",
]

with st.sidebar:
    st.title("Quantum Website")
    st.caption("PQC / QKD / 量化交易 / 3D 列印 / 台股 / YouTube / 量子工程")
    section = st.radio("功能", SECTIONS, label_visibility="collapsed")
    st.divider()

    # 分區專屬側邊欄控制 — subtopics 一律 sidebar（*_sidebar 模式，全站統一展示）
    quantum_topic = quantum_sidebar() if section == "📚 Quantum 主題" else None
    quant_topic = quant_sidebar() if section == "📊 Quant 主題" else None
    yt_sel = yt_sidebar() if section == "📺 YouTube 上傳貼文" else None
    ti_sel = ti_sidebar() if section == "🧪 拓撲絕緣體" else None
    stock_sel = stock_market_sidebar() if section == "💹 股市主題" else None

    st.divider()
    search_query = st.text_input(
        "🔍 全站搜尋", key="global_search", placeholder="關鍵字…"
    )

if search_query:
    st.markdown(f"## 🔍 搜尋結果：{search_query}")
    res = search_content(search_query)
    st.write(f"找到 {len(res)} 筆結果")
    for r in res:
        with st.expander(f"{r['source']} / {r['file']}"):
            st.text(r["snippet"])
elif section == "🏠 首頁":
    st.title("Quantum Website")
    st.markdown(
        "統一入口：量子主題（PQC/QKD/ECC）、量化交易主題、"
        "STL 3D 模型檢視器、股市主題（美股/台股/期權/心法）、YouTube 上傳貼文、"
        "量子傳輸線互動分析、拓撲絕緣體材料預測。"
    )
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            "### 📚 Quantum 主題\nPQC 基礎、QKD 金鑰分發、HNDL 威脅、台灣進展、橢圓加密、量子演算法 — 共 14 個主題"
        )
        st.markdown(
            "### 🧊 STL 3D 模型\nOloid / 軌跡體 3D 列印模型互動檢視 + Arduino 風力發電機組設計方案（25 章）"
        )
        st.markdown(
            "### 📺 YouTube 上傳貼文\n量子頻道市場競爭分析 + 13 個主題的上傳貼文草稿（依內容模板產生）"
        )
        st.markdown(
            "### 🔗 量子傳輸線\n多導體傳輸線高頻互動分析儀：RLGC 矩陣、蒙地卡羅良率、NEXT/FEXT 串擾"
        )
    with col2:
        st.markdown(
            "### 📊 Quant 主題\n台股實盤自動化（Shioaji）、均線交叉、高頻交易、平台架構 — 共 9 個主題"
        )
        st.markdown(
            "### 💹 股市主題\n"
            "美股投資管道、台股基金 ETF、期權入門、投資心法、配對交易、"
            "量化平台架構 — 共 9 個主題 ＋ 台股本益比查詢工具"
        )
        st.markdown(
            "### 🧪 拓撲絕緣體\n拓撲量子物態與快速材料預測完整部署包（資料庫、高通量篩選、GNN）"
        )
    st.divider()
    st.caption("👈 左側選單切換功能，或直接於側邊欄輸入關鍵字全站搜尋。")
elif section == "📚 Quantum 主題":
    render_quantum(quantum_topic)
elif section == "📊 Quant 主題":
    render_quant(quant_topic)
elif section == "🧊 STL 3D 模型":
    render_stl()
elif section == "💹 股市主題":
    render_stock_market(stock_sel)
elif section == "📺 YouTube 上傳貼文":
    render_youtube(yt_sel)
elif section == "🔗 量子傳輸線":
    render_tline()
else:
    render_ti(ti_sel)
