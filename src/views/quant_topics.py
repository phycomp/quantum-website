"""Quant 量化交易主題檢視（共 9 個主題：00_索引 ～ 08）。

主題清單顯示於側邊欄（quant_sidebar），內文顯示於主畫面（render_quant）。
顯示標題一律去除「Topic N：」前綴。
"""

import glob
import os
import re

import streamlit as st

from src.content_loader import SOURCES

_TOPIC_PREFIX = re.compile(r"^Topic\s*\d+\s*[：:]\s*")


def _strip_topic_prefix(title: str) -> str:
    """去除標題的「Topic N：」前綴（全形/半形冒號皆支援）。"""
    return _TOPIC_PREFIX.sub("", title).strip()


def _strip_leading_heading(content: str) -> str:
    """內文開頭若為 H1 則移除（頁面已顯示標題，避免重複與前綴殘留）。"""
    lines = content.split("\n")
    idx = next((i for i, line in enumerate(lines) if line.strip()), None)
    if idx is None or not lines[idx].startswith("# "):
        return content
    return "\n".join(lines[:idx] + lines[idx + 1 :]).lstrip("\n")


def _load_quant_topics():
    base = SOURCES["Quant"]
    if not base or not os.path.isdir(base):
        return []
    topics = []
    for path in sorted(glob.glob(os.path.join(base, "0*.md"))):
        try:
            with open(path, encoding="utf-8") as fh:
                content = fh.read()
        except Exception:
            continue
        name = os.path.basename(path)
        title = (
            name.replace(".md", "").split("_", 1)[-1]
            if "_" in name
            else name.replace(".md", "")
        )
        for line in content.split("\n"):
            if line.startswith("# "):
                title = line[2:].strip()
                break
        topics.append({"title": title, "content": content})
    return topics


def quant_sidebar():
    """側邊欄主題清單；回傳選定的主題 dict（無主題時回 None）。"""
    topics = _load_quant_topics()
    if not topics:
        return None
    st.markdown("**📊 Quant 主題 — 量化交易與自動化**")
    labels = [_strip_topic_prefix(t["title"]) for t in topics]
    selected = st.radio(
        f"共 {len(topics)} 個主題", labels, label_visibility="collapsed", horizontal=True
    )
    for t, label in zip(topics, labels):
        if label == selected:
            return t
    return None


def render_quant(topic=None):
    """主畫面：顯示選定主題內文（topic 來自 quant_sidebar）。"""
    st.title("📊 Quant 主題 — 量化交易與自動化")
    if topic is None:
        topics = _load_quant_topics()
        topic = topics[0] if topics else None
    if topic is None:
        st.warning("未找到量化主題檔案（data/quant_topics/）。")
        return
    st.markdown(f"## {_strip_topic_prefix(topic['title'])}")
    st.markdown(_strip_leading_heading(topic["content"]))
