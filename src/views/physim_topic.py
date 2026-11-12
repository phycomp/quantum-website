"""🔬 物理模擬（physim）— 驗收規格與概念圖。

主題清單顯示於側邊欄（physim_sidebar），內文顯示於主畫面（render_physim）—
與 Quantum / Quant / 拓撲絕緣體同一展示模式（subtopics 一律 sidebar，radio horizontal=True）。

來源：
  ~/物理模擬/docs/acceptance/*.md（驗收規格、概念圖）
  ~/物理模擬/README.md（系統總覽）
  由 push-streamlit/scripts/sync_topics.py 同步進 data/physim_topics/
"""

import glob
import os

import streamlit as st

from src.views.doc_browser import render_doc_browser

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PHYSIM_TOPICS_DIR = os.path.join(REPO_ROOT, "data", "physim_topics")

_LABELS = {
    "physics-simulation-acceptance.md": "01 · 驗收規格（FR/NFR/AC）",
    "concept-diagrams.md": "02 · 概念圖（架構/資料流/渲染管線）",
}


def _list_physim_topics():
    return [
        os.path.basename(f)
        for f in sorted(glob.glob(os.path.join(PHYSIM_TOPICS_DIR, "*.md")))
    ]


def _entries():
    files = _list_physim_topics()
    return [(_LABELS.get(n, n[:-3]), f"data/physim_topics/{n}") for n in files]


def physim_sidebar():
    entries = _entries()
    st.markdown("**🔬 物理模擬（physim）— 驗收與概念圖**")
    labels = [e[0] for e in entries]
    selected = st.radio(
        f"共 {len(labels)} 項", labels, label_visibility="collapsed", horizontal=True
    )
    for label, path in entries:
        if label == selected:
            return path
    return None


def render_physim(sel=None):
    st.title("🔬 物理模擬（physim）")
    st.caption(
        "physim 物理模擬平台：48 模型 / 19 領域 / 渲染 / 電路域 / 驗收規格與概念圖"
    )
    entries = _entries()
    if not entries:
        st.warning(
            "找不到主題檔案：data/physim_topics/（push 前應由 sync_topics.py 同步）"
        )
        return
    if sel is None:
        sel = entries[0][1]
    render_doc_browser(sel, key="physim_doc", caption="physim 驗收規格與概念圖")
