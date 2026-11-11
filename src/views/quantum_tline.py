"""🔗 量子傳輸線 — 多導體傳輸線高頻自動化分析儀（互動區塊）。

改寫自 ~/軟體/代理人/pages/03擴充自動化.py（舊架構獨立頁面）：
  - 移除 set_page_config 與模組級副作用（改由 app.py 統一配置）
  - 參數輸入由 sidebar 改為主畫面左欄（sidebar 為全站共用）
  - 蒙地卡羅改為純函式 + @st.cache_data 快取
  - 新增「📐 內容模板」頁籤（量子傳輸線視頻腳本模板）

物理模型（與原始版本一致）：
  - 2 導體 RLGC 矩陣導出（邊緣場微擾近似）
  - 電報方程矩陣指數解（scipy.linalg.expm）→ NEXT/FEXT 串擾
  - 高斯製造公差蒙地卡羅 → 阻抗良率（50Ω ±10%）
"""

import os

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from plotly.graph_objects import Box, Figure, Histogram
from scipy.linalg import expm

from src.views.doc_browser import REPO_ROOT

DK_NOMINAL = 4.3  # FR4 介電常數名義值
DF_NOMINAL = 0.02  # 損耗角正切


# ==============================================================================
# 核心電磁計算引擎（多導體矩陣）
# ==============================================================================
def derive_rlgc_matrices(w, h, t, s, dk, df, freq):
    """導出 2 導體系統的 2x2 RLGC 矩陣（2D 場求解近似）。"""
    w_m, h_m, t_m, s_m = w * 1e-6, h * 1e-6, t * 1e-6, s * 1e-6
    omega = 2 * np.pi * freq

    # 互容與自容矩陣（考慮邊界場微擾）
    c_self = 8.854e-12 * dk * (w_m / h_m + 1.2)
    c_mutual = 8.854e-12 * dk * (0.5 / (s_m / h_m + 0.1))
    C = np.array([[c_self + c_mutual, -c_mutual], [-c_mutual, c_self + c_mutual]])

    # 互感與自感矩陣（光速不變性與空間微擾）
    L = 1.256e-6 * 8.854e-12 * 1.0 / C
    L[0, 1] = L[1, 0] = L[0, 0] * (0.2 / (s_m / h_m + 0.5))

    # 高頻趨膚效應電阻 R 與介電損耗導納 G
    r_skin = 1.0 / (5.8e7 * t_m * w_m) * np.sqrt(freq / 1e9)
    R = np.array([[r_skin, 0.0], [0.0, r_skin]])
    G = omega * C * df

    return R, L, G, C


def sqrt_matrix(mat):
    """矩陣開平方根（特徵值分解）。"""
    evals, evecs = np.linalg.eig(mat)
    return np.dot(evecs, np.dot(np.diag(np.sqrt(evals)), np.linalg.inv(evecs)))


def analyze_crosstalk(R, L, G, C, freq, length):
    """電報方程矩陣指數解 → NEXT/FEXT 串擾（dB）。"""
    omega = 2 * np.pi * freq
    Z_mat = R + 1j * omega * L
    Y_mat = G + 1j * omega * C

    prop_mat = expm(-sqrt_matrix(np.dot(Y_mat, Z_mat)) * length)
    next_xtalk = 20 * np.log10(max(1e-6, abs(prop_mat[0, 1] * 0.3)))  # 近端串擾
    fext_xtalk = 20 * np.log10(max(1e-6, abs(prop_mat[1, 0])))  # 遠端串擾
    return next_xtalk, fext_xtalk


@st.cache_data(show_spinner=False)
def run_monte_carlo(w, h, t, s, w_sigma, h_sigma, dk_sigma, freq, length, samples):
    """高斯製造公差蒙地卡羅掃描 → 阻抗與串擾分佈。"""
    z0_list, next_list, fext_list = [], [], []
    w_samples = np.random.normal(w, w_sigma, samples)
    h_samples = np.random.normal(h, h_sigma, samples)
    dk_samples = np.random.normal(DK_NOMINAL, dk_sigma, samples)

    for i in range(samples):
        R, L, G, C = derive_rlgc_matrices(
            w_samples[i], h_samples[i], t, s, dk_samples[i], DF_NOMINAL, freq
        )
        z0 = np.sqrt(L[0, 0] / C[0, 0])
        nxt, fxt = analyze_crosstalk(R, L, G, C, freq, length)
        z0_list.append(z0)
        next_list.append(nxt)
        fext_list.append(fxt)

    return np.array(z0_list), np.array(next_list), np.array(fext_list)


# ==============================================================================
# 檢視
# ==============================================================================
def _render_calculator():
    left, right = st.columns([1, 2])

    with left:
        st.markdown("#### 📁 傳輸線 DSL 與製造公差配置")
        st.radio(
            "結構類型",
            ["Microstrip (微帶線)", "Stripline (帶狀線)"],
            horizontal=True,
            key="tline_type",
        )
        st.slider("線寬 W (μm)", 50, 300, 150, key="w_nominal")
        st.slider("介電厚度 H (μm)", 50, 500, 100, key="h_nominal")
        st.slider("導體厚度 T (μm)", 15, 70, 35, key="t_nominal")
        st.slider("線間距 S (μm)", 50, 400, 150, key="s_nominal")

        st.divider()
        st.markdown("#### 🎲 製造公差波動（Monte Carlo σ）")
        st.slider("σ_W 線寬 (μm)", 0.0, 10.0, 3.0, 0.5, key="w_sigma")
        st.slider("σ_H 厚度 (μm)", 0.0, 10.0, 2.5, 0.5, key="h_sigma")
        st.slider("σ_Dk 介電常數", 0.0, 0.2, 0.05, 0.01, key="dk_sigma")

        st.divider()
        st.markdown("#### ⚡ 模擬條件")
        st.number_input("目標頻率 (GHz)", 1.0, 30.0, 10.0, 1.0, key="freq_ghz")
        st.number_input("線長 (m)", 0.01, 1.0, 0.1, 0.05, key="line_len")
        st.radio(
            "蒙地卡羅抽樣次數",
            [100, 500, 1000],
            index=1,
            horizontal=True,
            key="mc_samples",
        )

    # 讀取 widget 狀態
    w_n, h_n, t_n, s_n = (
        st.session_state["w_nominal"],
        st.session_state["h_nominal"],
        st.session_state["t_nominal"],
        st.session_state["s_nominal"],
    )
    w_s, h_s, dk_s = (
        st.session_state["w_sigma"],
        st.session_state["h_sigma"],
        st.session_state["dk_sigma"],
    )
    freq_hz = st.session_state["freq_ghz"] * 1e9
    line_len = st.session_state["line_len"]
    mc_samples = st.session_state["mc_samples"]

    # 名義值計算
    R_n, L_n, G_n, C_n = derive_rlgc_matrices(
        w_n, h_n, t_n, s_n, DK_NOMINAL, DF_NOMINAL, freq_hz
    )
    z0_nominal = np.sqrt(L_n[0, 0] / C_n[0, 0])
    nominal_next, nominal_fext = analyze_crosstalk(
        R_n, L_n, G_n, C_n, freq_hz, line_len
    )

    # 蒙地卡羅掃描
    z0_s, next_s, fext_s = run_monte_carlo(
        w_n, h_n, t_n, s_n, w_s, h_s, dk_s, freq_hz, line_len, mc_samples
    )
    yield_rate = np.sum((z0_s >= 45) & (z0_s <= 55)) / mc_samples * 100

    with right:
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("特徵阻抗 Z₀", f"{z0_nominal:.2f} Ω")
        m2.metric("近端串擾 NEXT", f"{nominal_next:.2f} dB")
        m3.metric("遠端串擾 FEXT", f"{nominal_fext:.2f} dB")
        m4.metric("阻抗良率 (50Ω±10%)", f"{yield_rate:.1f} %")

        c_a, c_b = st.columns(2)

        with c_a:
            st.markdown("##### 🖼️ 雙導體截面幾何")
            fig, ax = plt.subplots(figsize=(6, 3))
            ax.set_facecolor("#f8f9fa")
            ax.add_patch(
                plt.Rectangle((-500, 0), 1000, h_n, color="#dcd6be", label="Substrate")
            )
            ax.add_patch(
                plt.Rectangle((-500, -t_n), 1000, t_n, color="#b87333", label="GND")
            )
            ax.add_patch(
                plt.Rectangle(
                    (-w_n - s_n / 2, h_n),
                    w_n,
                    t_n,
                    color="#ff4b4b",
                    label="Trace 1 (Aggressor)",
                )
            )
            ax.add_patch(
                plt.Rectangle(
                    (s_n / 2, h_n), w_n, t_n, color="#1f77b4", label="Trace 2 (Victim)"
                )
            )
            ax.set_xlim(-400, 400)
            ax.set_ylim(-50, h_n + 80)
            ax.set_xlabel("Width (μm)")
            ax.set_ylabel("Height (μm)")
            ax.legend(loc="upper right", fontsize="small")
            st.pyplot(fig)
            plt.close(fig)

            st.markdown("##### 📋 導出的 RLGC 矩陣（@ 目標頻率）")
            st.markdown("**單位長度電感矩陣 L (nH/m):**")
            st.dataframe(L_n * 1e9)
            st.markdown("**單位長度電容矩陣 C (pF/m):**")
            st.dataframe(C_n * 1e12)

        with c_b:
            st.markdown("##### 🎲 蒙地卡羅阻抗良率預測")
            fig_hist = Figure()
            fig_hist.add_trace(
                Histogram(x=z0_s, name="阻抗分佈", marker_color="#ff4b4b", opacity=0.75)
            )
            fig_hist.add_vline(
                x=45, line_dash="dash", line_color="red", annotation_text="下限 45Ω"
            )
            fig_hist.add_vline(
                x=55, line_dash="dash", line_color="red", annotation_text="上限 55Ω"
            )
            fig_hist.update_layout(
                title="隨機製造抽樣阻抗分佈",
                xaxis_title="Impedance (Ω)",
                yaxis_title="Count",
                template="plotly_white",
                height=320,
            )
            st.plotly_chart(fig_hist, use_container_width=True)

            st.markdown("##### ⚡ 公差引起的串擾波動")
            fig_xtalk = Figure()
            fig_xtalk.add_trace(
                Box(y=next_s, name="NEXT (近端)", marker_color="#ab63fa")
            )
            fig_xtalk.add_trace(
                Box(y=fext_s, name="FEXT (遠端)", marker_color="#00cc96")
            )
            fig_xtalk.update_layout(
                title="串擾波動範圍 (dB)",
                yaxis_title="Crosstalk (dB)",
                template="plotly_white",
                height=320,
            )
            st.plotly_chart(fig_xtalk, use_container_width=True)

            with st.expander("💡 多導體分析備忘錄"):
                st.markdown(
                    """
1. **互感與互容矩陣**：自導體的邊緣場（Fringing Field）是引起多導體串擾的主要物理成因，當線距 `S` 縮小時，`L[0,1]` 與 `C[0,1]` 將顯著增大。
2. **NEXT (近端串擾)**：主要受電磁耦合總量影響，在長度達到飽和長度後不再隨長度增加。
3. **FEXT (遠端串擾)**：受微帶線不均勻介電質環境（空氣與 FR4）影響，高頻下損耗會隨傳輸線長度呈現線性惡化。
                    """
                )


def _render_template():
    tpl_path = os.path.join(REPO_ROOT, "data", "docs", "quantum_tline_template.md")
    if not os.path.isfile(tpl_path):
        st.warning("找不到 data/docs/quantum_tline_template.md")
        return
    with open(tpl_path, encoding="utf-8") as fh:
        st.markdown(fh.read())
    st.divider()
    st.caption(
        "模板來源：~/軟體/代理人/content_templates/quantum.md — "
        "量子傳輸線主題的視頻腳本結構、關鍵字與目標平台"
    )


def render_tline():
    st.title("🔗 量子傳輸線 — 多導體高頻分析儀")
    st.caption(
        "幾何 DSL 輸入 → RLGC 矩陣導出 → 電磁計算 → 蒙地卡羅良率掃描 → 近/遠端串擾分析"
    )
    tab_calc, tab_tpl = st.tabs(["⚡ 互動分析儀", "📐 內容模板"])
    with tab_calc:
        _render_calculator()
    with tab_tpl:
        _render_template()
