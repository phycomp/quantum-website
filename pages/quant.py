"""Quant 量化交易主題頁面。"""

import sys, os

sys.path.insert(0, "/home/sam/quantum_website")
import streamlit as st
from src.content_loader import load_markdown_files, search_content

st.set_page_config(page_title="Quant 量化交易", layout="wide")
st.title("Quant 量化交易 & 自動化")

# 載入量化主題
QUANT_TOPICS_DIR = os.path.join(os.path.expanduser("~"), "量化", "topics")
if not os.path.isdir(QUANT_TOPICS_DIR):
    # Fallback to repo-local data
    QUANT_TOPICS_DIR = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "..", "data", "quant_topics"
    )

# 載入主題檔案
topics = []
if os.path.isdir(QUANT_TOPICS_DIR):
    for f in sorted(os.listdir(QUANT_TOPICS_DIR)):
        if f.endswith(".md"):
            path = os.path.join(QUANT_TOPICS_DIR, f)
            try:
                with open(path, encoding="utf-8") as fh:
                    content = fh.read()
                title = (
                    f.replace(".md", "").split("_", 1)[-1]
                    if "_" in f
                    else f.replace(".md", "")
                )
                for line in content.split("\n"):
                    if line.startswith("# "):
                        title = line[2:].strip()
                        break
                topics.append({"name": f, "title": title, "content": content})
            except Exception:
                pass

if not topics:
    st.warning("未找到量化主題檔案。")
    st.stop()

# Sidebar: 主題列表
selected = st.sidebar.radio(
    "選擇主題",
    [t["title"] for t in topics],
    label_visibility="collapsed",
)

# 主內容區
for t in topics:
    if t["title"] == selected:
        st.markdown(t["content"])
        break

# 搜尋
st.sidebar.markdown("---")
q = st.sidebar.text_input("搜尋關鍵字", key="quant_search")
if q:
    st.markdown(f"## 🔍 搜尋結果：{q}")
    # Search in quant topics
    results = []
    for t in topics:
        if q.lower() in t["content"].lower() or q.lower() in t["title"].lower():
            results.append(t)
    st.write(f"找到 {len(results)} 筆結果")
    for r in results:
        with st.expander(r["title"]):
            st.markdown(r["content"][:1000])
