"""量子位元架構主題檢視（蒸餾自 topic-distill pipeline，共 9 個主題）。

主題清單顯示於側邊欄（qubit_arch_sidebar），內文顯示於主畫面（render_qubit_arch）。
"""

import streamlit as st

from src.content_loader import load_qubit_arch_files


def _strip_topic_prefix(title: str) -> str:
    if title.startswith("Topic ") and "：" in title:
        return title.split("：", 1)[-1].strip()
    return title


def qubit_arch_sidebar():
    topics = load_qubit_arch_files()
    if not topics:
        return None
    st.markdown("**⚛️ 量子位元架構**")
    labels = [_strip_topic_prefix(t["title"]) for t in topics]
    selected = st.radio(
        f"共 {len(topics)} 個主題",
        labels,
        label_visibility="collapsed",
        horizontal=True,
    )
    for t, label in zip(topics, labels):
        if label == selected:
            return t
    return None


def render_qubit_arch(topic=None):
    st.title("⚛️ 量子位元架構")
    if topic is None:
        topics = load_qubit_arch_files()
        topic = topics[0] if topics else None
    if topic is None:
        st.warning("未找到量子位元架構主題檔案（data/qbit_arch_topics/）。")
        return
    st.markdown(f"## {_strip_topic_prefix(topic['title'])}")
    st.markdown(topic["content"])
