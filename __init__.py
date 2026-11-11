"""Quantum Website — Streamlit 入口。"""

import streamlit as st

st.set_page_config(page_title="Quantum Website", layout="wide")
st.title("Quantum Website — 量子傳輸線 / PQC / QKD / ECC")

st.markdown("## 歡迎")
st.write("請從左側 sidebar 選擇頁面：")
st.markdown("- **app** — PQC / QKD / ECC 量子主題（13 個主題）")
st.markdown("- **quant** — 量化交易 & 自動化主題（8 個主題）")

st.markdown("---")
st.markdown("### 快速連結")
st.markdown("- [GitHub Repo](https://github.com/phycomp/quantum-website)")
