"""App 端到端 smoke test — 驗證「subtopics 一律 sidebar」統一展示。

用 streamlit.testing.v1.AppTest 模擬側邊欄分區切換，檢查每個主題型
區塊都把主題清單放進 sidebar radio，且主畫面渲染不拋例外。
"""

import os
import sys

sys.path.insert(0, "/home/sam/quantum_website")
os.chdir("/home/sam/quantum_website")

from streamlit.testing.v1 import AppTest


def _run_section(section):
    at = AppTest.from_file("app.py", default_timeout=60)
    at.run()
    assert not at.exception, f"初始渲染例外：{[str(e.value) for e in at.exception]}"
    at.sidebar.radio[0].set_value(section).run()
    assert not at.exception, (
        f"「{section}」渲染例外：{[str(e.value) for e in at.exception]}"
    )
    return at


def test_quantum_section_sidebar():
    at = _run_section("📚 Quantum 主題")
    radios = at.sidebar.radio
    assert len(radios) >= 2, "Quantum 主題的 sidebar 應有分區 radio + 主題 radio"
    labels = radios[1].options
    assert len(labels) == 14, f"Quantum 主題應 14 項，實際 {len(labels)}"
    print(f"Quantum sidebar: PASS ({len(labels)} 項)")


def test_quant_section_sidebar():
    at = _run_section("📊 Quant 主題")
    radios = at.sidebar.radio
    assert len(radios) >= 2, "Quant 主題的 sidebar 應有分區 radio + 主題 radio"
    labels = radios[1].options
    assert len(labels) == 9, f"Quant 主題應 9 項，實際 {len(labels)}"
    print(f"Quant sidebar: PASS ({len(labels)} 項)")


def test_youtube_section_sidebar():
    at = _run_section("📺 YouTube 上傳貼文")
    radios = at.sidebar.radio
    assert len(radios) >= 2, "YouTube 的 sidebar 應有分區 radio + 清單 radio"
    labels = radios[1].options
    assert len(labels) == 14, f"YouTube 應 14 項（分析+13 貼文），實際 {len(labels)}"
    assert labels[0].startswith("📊 頻道市場分析"), f"首項應為市場分析：{labels[0]}"
    print(f"YouTube sidebar: PASS ({len(labels)} 項)")


def test_ti_section_sidebar():
    at = _run_section("🧪 拓撲絕緣體")
    radios = at.sidebar.radio
    assert len(radios) >= 2, "TI 的 sidebar 應有分區 radio + 清單 radio"
    labels = radios[1].options
    assert len(labels) == 8, f"TI 應 8 項（7 主題+部署包），實際 {len(labels)}"
    assert labels[-1].startswith("📦 快速材料預測部署包"), (
        f"末項應為部署包：{labels[-1]}"
    )
    print(f"TI sidebar: PASS ({len(labels)} 項)")


def test_ti_sidebar_switch_renders():
    """TI：切換主題 → 部署包，主畫面都應正常渲染（章節 selectbox 出現）。"""
    at = _run_section("🧪 拓撲絕緣體")
    labels = at.sidebar.radio[1].options
    at.sidebar.radio[1].set_value(labels[0]).run()  # 00 主題總覽
    assert not at.exception
    assert at.selectbox, "主題導讀應出現章節 selectbox"
    at.sidebar.radio[1].set_value(labels[-1]).run()  # 部署包
    assert not at.exception
    assert at.selectbox, "部署包應出現章節 selectbox"
    print("TI sidebar switch: PASS")


if __name__ == "__main__":
    test_quantum_section_sidebar()
    test_quant_section_sidebar()
    test_youtube_section_sidebar()
    test_ti_section_sidebar()
    test_ti_sidebar_switch_renders()
    print("All app smoke tests passed.")
