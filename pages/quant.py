"""Quant 量化交易主題頁面。"""

import sys, os

# Use relative path for Streamlit Cloud compatibility
_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, _REPO_ROOT)
import streamlit as st

st.set_page_config(page_title="Quant 量化交易", layout="wide")
st.title("Quant — 量化交易 & 自動化主題")

QUANT_TOPICS_DIR = os.path.join(_REPO_ROOT, "data", "quant_topics")
if not os.path.isdir(QUANT_TOPICS_DIR):
    QUANT_TOPICS_DIR = os.path.join(os.path.expanduser("~"), "量化", "topics")

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

with st.sidebar:
    st.markdown("### 🔍 搜尋")
    search_query = st.text_input("搜尋關鍵字", key="quant_search")

    st.markdown("### 📊 主題")
    topic_labels = [t["title"] for t in topics]

    selected_topic_label = st.radio(
        "選擇主題",
        topic_labels,
        label_visibility="collapsed",
    )

    selected_topic = None
    for t in topics:
        if t["title"] == selected_topic_label:
            selected_topic = t
            break

if search_query:
    st.markdown(f"## 🔍 搜尋結果：{search_query}")
    results = []
    for t in topics:
        if (
            search_query.lower() in t["content"].lower()
            or search_query.lower() in t["title"].lower()
        ):
            results.append(t)
    st.write(f"找到 {len(results)} 筆結果")
    for r in results:
        with st.expander(r["title"]):
            st.markdown(r["content"][:1000])
elif selected_topic:
    st.markdown(f"## {selected_topic['title']}")
    st.markdown(selected_topic["content"])
