"""STL 3D 模型檢視器（Oloid / 軌跡體）+ Arduino 風力發電機組設計文件。

使用 vendored 的 streamlit_stl 元件（repo 根目錄 streamlit_stl/，
含 three.js — 無外部 PyPI 依賴）。元件採 lazy import：
只在實際渲染時載入，避免 import 期副作用。

頁籤：
  1. 🧊 3D 模型檢視 — assets/stl/ 互動檢視
  2. 🌬️ Arduino 風力發電機組 — 3D 列印設計方案（6 輪設計對話，25 章）
"""

import glob
import os

import streamlit as st

from src.views.doc_browser import render_doc_browser

_REPO_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
STL_DIR = os.path.join(_REPO_ROOT, "assets", "stl")


def _render_models():
    st.caption("Oloid / 軌跡體（trajectory body）3D 列印模型 — 可拖曳旋轉與縮放")

    files = sorted(glob.glob(os.path.join(STL_DIR, "*.stl")))
    if not files:
        st.warning("未找到 STL 檔案（assets/stl/）。")
        return

    labels = [os.path.basename(f)[:-4] for f in files]

    c1, c2, c3 = st.columns(3)
    with c1:
        model = st.radio("模型", labels, index=0, horizontal=True)
        color = st.color_picker("顏色", "#FF9900")
    with c2:
        material = st.radio(
            "材質", ["material", "flat", "wireframe"], index=0, horizontal=True
        )
        auto_rotate = st.toggle("自動旋轉", value=True)
    with c3:
        opacity = st.slider("不透明度", 0.0, 1.0, 1.0, 0.05)
        height = st.slider("顯示高度", 300, 900, 500, 50)

    path = files[labels.index(model)]

    # lazy import：元件會自我複製到 temp dir，僅在渲染時載入
    from streamlit_stl import stl_from_file

    stl_from_file(
        file_path=path,
        color=color,
        material=material,
        auto_rotate=auto_rotate,
        opacity=opacity,
        height=height,
        shininess=100,
        cam_v_angle=60,
        cam_h_angle=-90,
        cam_distance=0,
        max_view_distance=1000,
    )


def render_stl():
    st.title("🧊 STL 3D 模型與列印設計")

    tab_models, tab_arduino = st.tabs(["🧊 3D 模型檢視", "🌬️ Arduino 風力發電機組"])
    with tab_models:
        _render_models()
    with tab_arduino:
        render_doc_browser(
            "data/docs/arduino_wind_turbine.md",
            key="arduino_doc",
            caption="🌬️ 家用 Arduino 風力發電機組 3D 列印方案 — "
            "NACA 翼型建模、BEM 模擬、MPPT 控制、Oloid 葉片、CFD/FEM（6199 行）",
        )
