"""📺 YouTube 上傳貼文 — 頻道市場分析 + 13 主題貼文草稿。

清單顯示於側邊欄（yt_sidebar），內文顯示於主畫面（render_youtube）—
與 Quantum / Quant / 拓撲絕緣體同一展示模式（subtopics 一律 sidebar）。

內容：
  📊 頻道市場分析 — QUANTUM_MARKET_ANALYSIS.md（競爭頻道、熱門視頻、內容建議）
  📝 上傳貼文     — data/yt_posts/（scripts/gen_yt_posts.py 依 quantum.md 模板產生）
"""

import glob
import os

import streamlit as st

from src.views.doc_browser import REPO_ROOT

_ANALYSIS_PATH = "data/docs/quantum_market_analysis.md"
_ANALYSIS_LABEL = "📊 頻道市場分析"


def _load_posts():
    base = os.path.join(REPO_ROOT, "data", "yt_posts")
    posts = []
    for path in sorted(glob.glob(os.path.join(base, "[0-9]*.md"))):
        try:
            with open(path, encoding="utf-8") as fh:
                content = fh.read()
        except Exception:
            continue
        title = os.path.basename(path)[:-3]
        for line in content.split("\n"):
            if line.startswith("# "):
                title = line[2:].strip()
                break
        posts.append({"title": title, "content": content})
    return posts


def _entries():
    """側邊欄/主畫面共用清單：市場分析（path）+ 各貼文（post）。"""
    entries = [{"label": _ANALYSIS_LABEL, "path": _ANALYSIS_PATH}]
    entries += [{"label": p["title"], "post": p} for p in _load_posts()]
    return entries


def yt_sidebar():
    """側邊欄清單；回傳選定項 dict（{"label", "path"} 或 {"label", "post"}）。"""
    entries = _entries()
    st.markdown("**📺 YouTube 上傳貼文**")
    labels = [e["label"] for e in entries]
    selected = st.radio(f"共 {len(labels)} 項", labels, label_visibility="collapsed", horizontal=True)
    for e in entries:
        if e["label"] == selected:
            return e
    return None


def render_youtube(sel=None):
    """主畫面：顯示選定內容（sel 來自 yt_sidebar；預設市場分析）。"""
    st.title("📺 YouTube 上傳貼文")
    st.caption(
        "量子頻道 — 市場競爭分析與 13 個主題的上傳貼文草稿（依 quantum.md 內容模板產生）"
    )
    if sel is None:
        sel = {"label": _ANALYSIS_LABEL, "path": _ANALYSIS_PATH}
    if "post" in sel:
        st.markdown(f"## {sel['post']['title']}")
        st.markdown(sel["post"]["content"])
        return
    path = os.path.join(REPO_ROOT, sel.get("path", _ANALYSIS_PATH))
    if os.path.isfile(path):
        with open(path, encoding="utf-8") as fh:
            st.markdown(fh.read())
        st.divider()
        st.caption(
            "來源：~/軟體/代理人/docs/QUANTUM_MARKET_ANALYSIS.md（2026-11-11 整合）"
        )
    else:
        st.warning("找不到 data/docs/quantum_market_analysis.md")
