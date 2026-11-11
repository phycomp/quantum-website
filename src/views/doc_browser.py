"""共用大檔瀏覽器：以 H2 章節切割 markdown，selectbox 導覽。

用於 Arduino 風力發電機組（25 章）與拓撲絕緣體（10 章）等大檔，
避免一次渲染數千行造成頁面遲緩。
"""

import os
import re

import streamlit as st

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

_H2 = re.compile(r"^##\s+(.+)$")


def split_sections(md_text):
    """以 H2（## ）標題切割 markdown；首段（第一個 H2 之前）為「簡介」。"""
    sections = []
    title = "📄 簡介"
    buf = []
    for line in md_text.split("\n"):
        m = _H2.match(line)
        if m:
            sections.append((title, "\n".join(buf).strip()))
            title = m.group(1).strip()
            buf = []
        else:
            buf.append(line)
    sections.append((title, "\n".join(buf).strip()))
    return [(t, c) for t, c in sections if c]


def render_doc_browser(rel_path, key, caption=None):
    """渲染章節式文件瀏覽器。

    rel_path: 相對 repo 根目錄的 markdown 路徑（如 data/docs/xxx.md）
    key:      selectbox 的唯一 key
    """
    path = os.path.join(REPO_ROOT, rel_path)
    if not os.path.isfile(path):
        st.warning(f"找不到文件：{rel_path}")
        return
    with open(path, encoding="utf-8") as fh:
        text = fh.read()

    sections = split_sections(text)
    if not sections:
        st.warning("文件沒有可顯示的章節。")
        return

    if caption:
        st.caption(caption)

    titles = [t for t, _ in sections]
    selected = st.selectbox(f"章節（共 {len(titles)} 章）", titles, key=key)

    for t, content in sections:
        if t == selected:
            if t != "📄 簡介":
                st.markdown(f"## {t}")
            st.markdown(content)
            break
