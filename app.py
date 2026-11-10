"""Quantum Website — Streamlit 入口。"""

import sys

sys.path.insert(0, "/home/sam/quantum_website")
import streamlit as st
from src.content_loader import load_all, search_content

st.set_page_config(page_title="Quantum Website", layout="wide")
st.title("Quantum Website — 量子傳輸線 / PQC / QKD / ECC")

page = st.sidebar.radio(
    "頁面", ["首頁", "搜尋", "PQC", "QKD", "ECC", "量子演算法", "Oloid 3D"]
)

if page == "首頁":
    st.markdown("## 量子網站")
    st.write("整合 PQC、QKD、ECC、量子傳輸線內容。")
    data = load_all()
    for k, v in data.items():
        st.subheader(k)
        st.write(f"找到 {len(v)} 個 Markdown 檔案。")
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
    st.write("Shor 大數分解、Grover 搜尋加速、量子傅立葉變換 (QFT)、量子糾纏與疊加。")
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
    st.video("/home/sam/Oloid/video_oloid.mp4")
