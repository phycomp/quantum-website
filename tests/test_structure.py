"""Repo 結構完整性測試 — 防範主題檔/資產缺漏再次發生。

背景：2026-11-11 事故 — 9 個量化主題檔從未進 repo
（只放了一個合併檔），而本機 fallback 掩蓋了問題，health check 也測不出。
"""

import glob
import os
import py_compile
import sys

sys.path.insert(0, "/home/sam/quantum_website")

REPO = "/home/sam/quantum_website"


def test_quant_topics_present():
    files = glob.glob(os.path.join(REPO, "data", "quant_topics", "0*.md"))
    assert len(files) == 9, f"quant topics 應有 9 檔，實際 {len(files)}"
    print("quant_topics: PASS (9 檔)")


def test_quantum_topics_present():
    files = glob.glob(os.path.join(REPO, "data", "topics", "[0-9]*.md"))
    assert len(files) == 14, f"quantum topics 應有 14 檔，實際 {len(files)}"
    print("quantum topics: PASS (14 檔)")


def test_stl_assets():
    files = glob.glob(os.path.join(REPO, "assets", "stl", "*.stl"))
    assert len(files) == 4, f"STL 應有 4 檔，實際 {len(files)}"
    print("stl assets: PASS (4 檔)")


def test_streamlit_stl_vendored():
    base = os.path.join(REPO, "streamlit_stl")
    assert os.path.isfile(os.path.join(base, "__init__.py")), (
        "缺 streamlit_stl/__init__.py"
    )
    assert os.path.isfile(os.path.join(base, "index.html")), (
        "缺 streamlit_stl/index.html"
    )
    for js in ("three.min.js", "OrbitControls.js", "STLLoader.js", "stl-viewer.js"):
        path = os.path.join(base, "three_js_scripts", js)
        assert os.path.isfile(path), f"缺 {path}"
    print("streamlit_stl vendored: PASS")


def test_views_compile():
    views = glob.glob(os.path.join(REPO, "src", "views", "*.py"))
    assert len(views) >= 5, f"views 應有 5 個 py（含 __init__），實際 {len(views)}"
    for v in views:
        py_compile.compile(v, doraise=True)
    py_compile.compile(os.path.join(REPO, "app.py"), doraise=True)
    py_compile.compile(os.path.join(REPO, "__init__.py"), doraise=True)
    print("views + app.py + __init__.py compile: PASS")


def test_entrypoints_in_sync():
    with open(os.path.join(REPO, "app.py"), encoding="utf-8") as fh:
        a = fh.read()
    with open(os.path.join(REPO, "__init__.py"), encoding="utf-8") as fh:
        b = fh.read()
    assert a == b, "app.py 與 __init__.py 不同步"
    print("entrypoints sync: PASS")


if __name__ == "__main__":
    test_quant_topics_present()
    test_quantum_topics_present()
    test_stl_assets()
    test_streamlit_stl_vendored()
    test_views_compile()
    test_entrypoints_in_sync()
    print("All structure tests passed.")
