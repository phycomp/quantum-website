"""📺 YouTube 上傳貼文 — 頻道市場分析 + 13 主題貼文草稿。

頁籤：
  1. 📊 頻道市場分析 — QUANTUM_MARKET_ANALYSIS.md（競爭頻道、熱門視頻、內容建議）
  2. 📝 上傳貼文 — data/yt_posts/（scripts/gen_yt_posts.py 依 quantum.md 模板產生）
"""

import glob
import os

import streamlit as st

from src.views.doc_browser import REPO_ROOT


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


def render_youtube():
    st.title("📺 YouTube 上傳貼文")
    st.caption(
        "量子頻道 — 市場競爭分析與 13 個主題的上傳貼文草稿（依 quantum.md 內容模板產生）"
    )

    tab_analysis, tab_posts = st.tabs(["📊 頻道市場分析", "📝 上傳貼文"])

    with tab_analysis:
        path = os.path.join(REPO_ROOT, "data", "docs", "quantum_market_analysis.md")
        if os.path.isfile(path):
            with open(path, encoding="utf-8") as fh:
                st.markdown(fh.read())
            st.divider()
            st.caption(
                "來源：~/軟體/代理人/docs/QUANTUM_MARKET_ANALYSIS.md（2026-11-11 整合）"
            )
        else:
            st.warning("找不到 data/docs/quantum_market_analysis.md")

    with tab_posts:
        posts = _load_posts()
        if not posts:
            st.warning("未找到貼文（data/yt_posts/）；先執行 scripts/gen_yt_posts.py")
            return
        labels = [p["title"] for p in posts]
        selected = st.selectbox(
            f"主題（共 {len(posts)} 份）", labels, key="yt_post_sel"
        )
        for p in posts:
            if p["title"] == selected:
                st.markdown(p["content"])
                break
