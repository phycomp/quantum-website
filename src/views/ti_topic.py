"""🧪 拓撲絕緣體 — 蒸餾主題導讀（7 檔）＋ 快速材料預測部署包。

主題清單顯示於側邊欄（ti_sidebar），內文顯示於主畫面（render_ti）—
與 Quantum / Quant / YouTube 貼文同一展示模式（subtopics 一律 sidebar）。

來源：
  蒸餾主題 — ~/.opencode/skills/topological-insulator/references/*.md
            （~/物理模擬/topo 119 檔蒸餾 + 2026-11-11 網路充實；
             由 push-streamlit/scripts/sync_topics.py 同步進 data/ti_topics/）
  部署包   — data/docs/topological_insulator.md
            （~/物理模擬/topo/指標/自動化TI.md 2101 行完整部署包，
             含 install.sh、資料庫 schema、服務模組、GNN 預測器）
"""

import glob
import os

import streamlit as st

from src.views.doc_browser import render_doc_browser

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TI_TOPICS_DIR = os.path.join(REPO_ROOT, "data", "ti_topics")
_DEPLOY_PATH = "data/docs/topological_insulator.md"
_DEPLOY_LABEL = "📦 快速材料預測部署包"

# 顯示名稱（新檔案自動 fallback 為檔名去尾）
_LABELS = {
    "00_主題總覽.md": "00 · 主題總覽（入口與路由）",
    "01_基礎物理.md": "01 · 基礎物理（Berry 相位／Z₂／BHZ／TRS）",
    "02_材料系統.md": "02 · 材料系統（Bi₂Se₃ 家族／MnBi₂Te₄）",
    "03_計算與預測.md": "03 · 計算與預測（指標定理／高通量資料庫）",
    "04_量子傳輸線工程.md": "04 · 量子傳輸線工程（TIRC 共面波導／低溫）",
    "05_拓撲超導與量子計算.md": "05 · 拓撲超導與量子計算（Majorana）",
    "06_台灣製造與學術生態.md": "06 · 台灣製造與學術生態（長晶／微影／放量）",
}


def _list_ti_topics():
    """列出 data/ti_topics/*.md（同步後應有 7 檔；動態掃描容納日後新增）。"""
    return [
        os.path.basename(f)
        for f in sorted(glob.glob(os.path.join(TI_TOPICS_DIR, "*.md")))
    ]


def _entries():
    """側邊欄/主畫面共用的 (label, 相對路徑) 清單：7 主題 + 部署包。"""
    files = _list_ti_topics()
    entries = [(_LABELS.get(n, n[:-3]), f"data/ti_topics/{n}") for n in files]
    entries.append((_DEPLOY_LABEL, _DEPLOY_PATH))
    return entries


def ti_sidebar():
    """側邊欄清單；回傳選定項的相對路徑（無主題檔時僅部署包一項）。"""
    entries = _entries()
    st.markdown("**🧪 拓撲絕緣體 — 主題導讀＋部署包**")
    labels = [e[0] for e in entries]
    selected = st.radio(f"共 {len(labels)} 項", labels, label_visibility="collapsed")
    for label, path in entries:
        if label == selected:
            return path
    return None


def render_ti(sel=None):
    """主畫面：顯示選定內容（sel 來自 ti_sidebar；預設第一項）。"""
    st.title("🧪 拓撲絕緣體")
    st.caption(
        "拓撲量子物態完整專區 — 蒸餾主題（~/物理模擬/topo 119 檔）"
        "＋ 快速材料預測部署包（資料庫、高通量篩選、GNN）"
    )
    entries = _entries()
    if not entries:
        st.warning("找不到主題檔案：data/ti_topics/（push 前應由 sync_topics.py 同步）")
        return
    if sel is None:
        sel = entries[0][1]
    label = next((lbl for lbl, p in entries if p == sel), "")
    if sel == _DEPLOY_PATH:
        render_doc_browser(
            sel,
            key="ti_doc",
            caption="📦 部署包依 H2 章節導覽；內含安裝腳本、SQL schema 與 Python 服務完整程式碼",
        )
    else:
        render_doc_browser(
            sel,
            key="ti_ref_chapter",
            caption=f"📂 {label} — 依 H2 章節導覽",
        )
