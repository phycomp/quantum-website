"""Quantum Website — Streamlit 入口。"""

import sys, os

sys.path.insert(0, "/home/sam/quantum_website")
import streamlit as st
from src.content_loader import load_all, search_content, load_topic_files

st.set_page_config(page_title="Quantum Website", layout="wide")
st.title("Quantum Website — 量子傳輸線 / PQC / QKD / ECC")

topics = load_topic_files()

# Sidebar: 整合頁面導航與主題列表
with st.sidebar:
    st.markdown("### 📍 導航")

    # 頁面選項
    page_options = ["首頁", "搜尋", "PQC", "QKD", "ECC", "量子演算法", "Oloid 3D"]

    # 主題選項
    topic_labels = [f"📄 {t['title']}" for t in topics]
    topic_names = [t["name"] for t in topics]

    # 整合所有選項（移除分隔線）
    all_options = page_options + topic_labels

    # 預設選項
    if "selected_page" not in st.session_state:
        st.session_state.selected_page = "首頁"

    selected = st.radio(
        "選擇頁面或主題",
        all_options,
        index=all_options.index(st.session_state.selected_page)
        if st.session_state.selected_page in all_options
        else 0,
        label_visibility="collapsed",
    )

    st.session_state.selected_page = selected

# 判斷是頁面還是主題
is_topic = selected.startswith("📄 ")
selected_topic = None
if is_topic:
    topic_idx = topic_labels.index(selected)
    selected_topic = topics[topic_idx]

# 主內容區
if is_topic and selected_topic:
    st.markdown(f"## {selected_topic['title']}")
    st.markdown(selected_topic["content"])
else:
    page = selected

    if page == "首頁":
        st.markdown("## 量子網站")
        st.write("整合 PQC、QKD、ECC、量子傳輸線內容。")
        data = load_all()
        for k, v in data.items():
            st.subheader(k)
            st.write(f"找到 {len(v)} 個 Markdown 檔案。")
        st.markdown("---")
        st.markdown(f"### 📚 主題總覽（{len(topics)} 個主題）")
        for t in topics:
            st.markdown(f"- **{t['title']}** (`{t['name']}`)")

    elif page == "搜尋":
        q = st.text_input("搜尋關鍵字")
        if q:
            res = search_content(q)
            st.write(f"找到 {len(res)} 筆結果")
            for r in res:
                st.markdown(f"**{r['source']} / {r['file']}**")
                st.text(r["snippet"])

    elif page == "PQC":
        files = load_all().get("PQC", [])
        for f in files[:5]:
            st.subheader(f["name"])
            st.text(f["content"][:500])

    elif page == "QKD":
        files = load_all().get("PQC", [])
        for f in files:
            if "QKD" in f["name"] or "QKD" in f["content"]:
                st.subheader(f["name"])
                st.text(f["content"][:500])

    elif page == "ECC":
        files = load_all().get("ECC", [])
        for f in files[:5]:
            st.subheader(f["name"])
            st.text(f["content"][:500])

    elif page == "量子演算法":
        st.markdown("## 量子演算法")
        st.write(
            "Shor 大數分解、Grover 搜尋加速、量子傅立葉變換 (QFT)、量子糾纏與疊加。"
        )
        st.markdown("### 相關視頻")
        st.video("https://www.youtube.com/watch?v=YSFPRSeHlNo")
        st.markdown("### 參考資料")
        files = load_all().get("PQC", [])
        for f in files:
            if "QKD" in f["name"] or "量子" in f["content"]:
                st.subheader(f["name"])
                st.text(f["content"][:300])

    elif page == "Oloid 3D":
        st.markdown("## Oloid 3D 列印產品")
        st.write("比價報告、視頻、行銷通路。")
        video_path = "assets/video_oloid.mp4"
        if os.path.exists(video_path):
            st.video(video_path)
        else:
            st.info("視頻檔案未找到。")
