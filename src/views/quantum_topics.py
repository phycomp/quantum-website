"""Quantum 主題檢視（PQC / QKD / ECC，共 14 個主題）。

主題清單顯示於側邊欄（quantum_sidebar），內文顯示於主畫面（render_quantum）—
與 Quant 主題 / 拓撲絕緣體 / YouTube 貼文同一展示模式（subtopics 一律 sidebar）。
"""

import streamlit as st

from src.content_loader import load_topic_files


def _strip_topic_prefix(title: str) -> str:
    """去除標題的「Topic N：」前綴。"""
    if title.startswith("Topic ") and "：" in title:
        return title.split("：", 1)[-1].strip()
    return title


def quantum_sidebar():
    """側邊欄主題清單；回傳選定的主題 dict（無主題時回 None）。"""
    topics = load_topic_files()
    if not topics:
        return None
    st.markdown("**📚 Quantum 主題 — PQC / QKD / ECC**")
    labels = [_strip_topic_prefix(t["title"]) for t in topics]
    selected = st.radio(
        f"共 {len(topics)} 個主題", labels, label_visibility="collapsed", horizontal=True
    )
    for t, label in zip(topics, labels):
        if label == selected:
            return t
    return None


def render_quantum(topic=None):
    """主畫面：顯示選定主題內文（topic 來自 quantum_sidebar）。"""
    st.title("📚 Quantum 主題 — PQC / QKD / ECC")
    if topic is None:
        topics = load_topic_files()
        topic = topics[0] if topics else None
    if topic is None:
        st.warning("未找到量子主題檔案（data/topics/）。")
        return
    st.markdown(f"## {_strip_topic_prefix(topic['title'])}")
    st.markdown(topic["content"])
