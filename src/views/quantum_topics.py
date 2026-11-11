"""Quantum 主題檢視（PQC / QKD / ECC，共 14 個主題）。"""

import streamlit as st

from src.content_loader import load_topic_files


def render_quantum():
    st.title("📚 Quantum 主題 — PQC / QKD / ECC")

    topics = load_topic_files()
    if not topics:
        st.warning("未找到量子主題檔案（data/topics/）。")
        return

    labels = []
    for t in topics:
        title = t["title"]
        if title.startswith("Topic ") and "：" in title:
            title = title.split("：", 1)[-1].strip()
        labels.append(title)

    selected = st.radio(
        f"共 {len(labels)} 個主題", labels, label_visibility="collapsed"
    )

    for t, label in zip(topics, labels):
        if label == selected:
            st.markdown(f"## {t['title']}")
            st.markdown(t["content"])
            break
