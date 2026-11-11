"""🧪 拓撲絕緣體 — 快速材料預測部署包（獨立區塊）。

來源：~/物理模擬/topo/指標/自動化TI.md（2101 行完整部署包，
含 install.sh、資料庫 schema、服務模組、GNN 預測器）。
"""

import streamlit as st

from src.views.doc_browser import render_doc_browser


def render_ti():
    st.title("🧪 拓撲絕緣體 — 快速材料預測")
    st.caption(
        "拓撲量子物態與快速材料預測完整部署包 — "
        "資料庫、高通量篩選服務、GNN 圖神經網路預測器"
    )
    render_doc_browser(
        "data/docs/topological_insulator.md",
        key="ti_doc",
        caption="📦 部署包依 H2 章節導覽；內含安裝腳本、SQL schema 與 Python 服務完整程式碼",
    )
