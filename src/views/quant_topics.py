"""Quant 量化交易主題檢視（共 9 個主題：00_索引 ～ 08）。"""

import glob
import os

import streamlit as st

from src.content_loader import SOURCES


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


def render_quant():
    st.title("📊 Quant 主題 — 量化交易與自動化")

    topics = _load_quant_topics()
    if not topics:
        st.warning("未找到量化主題檔案（data/quant_topics/）。")
        return

    selected = st.radio(
        f"共 {len(topics)} 個主題",
        [t["title"] for t in topics],
        label_visibility="collapsed",
    )

    for t in topics:
        if t["title"] == selected:
            st.markdown(f"## {t['title']}")
            st.markdown(t["content"])
            break
