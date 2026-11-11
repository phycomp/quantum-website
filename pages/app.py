"""Quantum 主題頁面（PQC/QKD/ECC）。"""

import sys, os

sys.path.insert(0, "/home/sam/quantum_website")
import streamlit as st
from src.content_loader import load_topic_files, search_content

st.set_page_config(page_title="Quantum 主題", layout="wide")
st.title("Quantum — PQC / QKD / ECC 量子主題")

topics = load_topic_files()

# Sidebar: 搜尋 + 主題列表
with st.sidebar:
    st.markdown("### 🔍 搜尋")
    search_query = st.text_input("搜尋關鍵字", key="quantum_search")

    st.markdown("### 📚 主題")
    topic_labels = []
    for t in topics:
        title = t["title"]
        if title.startswith("Topic ") and "：" in title:
            title = title.split("：", 1)[-1].strip()
        topic_labels.append(title)

    selected_topic_label = st.radio(
        "選擇主題",
        topic_labels,
        label_visibility="collapsed",
    )

    selected_topic = None
    for t, label in zip(topics, topic_labels):
        if label == selected_topic_label:
            selected_topic = t
            break

# 主內容區
if search_query:
    st.markdown(f"## 🔍 搜尋結果：{search_query}")
    res = search_content(search_query)
    st.write(f"找到 {len(res)} 筆結果")
    for r in res:
        st.markdown(f"**{r['source']} / {r['file']}**")
        st.text(r["snippet"])
elif selected_topic:
    st.markdown(f"## {selected_topic['title']}")
    st.markdown(selected_topic["content"])
