"""Quantum Website — Streamlit 入口。"""

import sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import streamlit as st
from src.content_loader import load_topic_files, search_content

st.set_page_config(page_title="Quantum Website", layout="wide")
st.title("Quantum Website — 量子傳輸線 / PQC / QKD / ECC")

# 載入所有主題（PQC/QKD + Quant）
pqc_topics = load_topic_files()

# 載入 Quant 主題
quant_topics = []
quant_dir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "data", "quant_topics"
)
if not os.path.isdir(quant_dir):
    quant_dir = os.path.join(os.path.expanduser("~"), "量化", "topics")
if os.path.isdir(quant_dir):
    for f in sorted(os.listdir(quant_dir)):
        if f.endswith(".md"):
            path = os.path.join(quant_dir, f)
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
                quant_topics.append({"name": f, "title": title, "content": content})
            except Exception:
                pass

# Sidebar: 搜尋 + 主題列表
with st.sidebar:
    st.markdown("### 🔍 搜尋")
    search_query = st.text_input("搜尋關鍵字", key="main_search")

    st.markdown("### 📚 Quantum 主題")
    pqc_labels = []
    for t in pqc_topics:
        title = t["title"]
        if title.startswith("Topic ") and "：" in title:
            title = title.split("：", 1)[-1].strip()
        pqc_labels.append(title)

    selected_pqc = st.radio(
        "Quantum",
        pqc_labels,
        label_visibility="collapsed",
        key="pqc_radio",
    )

    st.markdown("### 📊 Quant 主題")
    quant_labels = [t["title"] for t in quant_topics]
    selected_quant = st.radio(
        "Quant",
        quant_labels,
        label_visibility="collapsed",
        key="quant_radio",
    )

# 判斷選中的是哪個主題
selected_topic = None
for t, label in zip(pqc_topics, pqc_labels):
    if label == selected_pqc:
        selected_topic = t
        break
if selected_topic is None:
    for t in quant_topics:
        if t["title"] == selected_quant:
            selected_topic = t
            break

# 主內容區
if search_query:
    st.markdown(f"## 🔍 搜尋結果：{search_query}")
    res = []
    for t in pqc_topics:
        if (
            search_query.lower() in t["content"].lower()
            or search_query.lower() in t["title"].lower()
        ):
            res.append(
                {"source": "Quantum", "file": t["name"], "snippet": t["content"][:300]}
            )
    for t in quant_topics:
        if (
            search_query.lower() in t["content"].lower()
            or search_query.lower() in t["title"].lower()
        ):
            res.append(
                {"source": "Quant", "file": t["name"], "snippet": t["content"][:300]}
            )
    st.write(f"找到 {len(res)} 筆結果")
    for r in res:
        st.markdown(f"**{r['source']} / {r['file']}**")
        st.text(r["snippet"])
elif selected_topic:
    st.markdown(f"## {selected_topic['title']}")
    st.markdown(selected_topic["content"])
