"""Quantum Website — 統一入口：Quantum / Quant / STL 3D / 台股本益比。

架構（2026-11-11 重構）：
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
from src.views.quantum_topics import render_quantum
from src.views.quant_topics import quant_sidebar, render_quant
from src.views.stl_viewer import render_stl
from src.views.stock_vwr import render_stock_vwr

st.set_page_config(page_title="Quantum Website", layout="wide")

SECTIONS = [
    "🏠 首頁",
    "📚 Quantum 主題",
    "📊 Quant 主題",
    "🧊 STL 3D 模型",
    "📈 台股本益比",
]

with st.sidebar:
    st.title("Quantum Website")
    st.caption("PQC / QKD / 量化交易 / 3D 列印 / 台股")
    section = st.radio("功能", SECTIONS, label_visibility="collapsed")
    st.divider()

    # 分區專屬側邊欄控制：Quant 主題清單（標題已去除「Topic N：」前綴）
    quant_topic = quant_sidebar() if section == "📊 Quant 主題" else None

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
        "STL 3D 模型檢視器、台股本益比查詢。"
    )
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            "### 📚 Quantum 主題\nPQC 基礎、QKD 金鑰分發、HNDL 威脅、台灣進展、橢圓加密、量子演算法 — 共 14 個主題"
        )
        st.markdown(
            "### 🧊 STL 3D 模型\nOloid / 軌跡體 3D 列印模型互動檢視（旋轉、縮放、換色）"
        )
    with col2:
        st.markdown(
            "### 📊 Quant 主題\n台股實盤自動化（Shioaji）、均線交叉、高頻交易、平台架構 — 共 9 個主題"
        )
        st.markdown(
            "### 📈 台股本益比\nTWSE 每日本益比 / 殖利率 / 股價淨值比查詢（Top N、搜尋）"
        )
    st.divider()
    st.caption("👈 左側選單切換功能，或直接於側邊欄輸入關鍵字全站搜尋。")
elif section == "📚 Quantum 主題":
    render_quantum()
elif section == "📊 Quant 主題":
    render_quant(quant_topic)
elif section == "🧊 STL 3D 模型":
    render_stl()
else:
    render_stock_vwr()
