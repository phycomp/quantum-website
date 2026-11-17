"""蒸餾成果展示（Distill Showcase）— 統一展示所有蒸餾主題。

從 topics_index.json 載入主題，側邊欄選擇，主畫面顯示內容。
"""

import json
import streamlit as st
from pathlib import Path

INDEX_PATH = (
    Path(__file__).resolve().parent.parent.parent / "data" / "topics_index.json"
)
REPO_ROOT = Path(__file__).resolve().parent.parent.parent


def _load_index():
    if INDEX_PATH.exists():
        try:
            return json.loads(INDEX_PATH.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def _read_md(path):
    p = Path(path)
    if p.exists():
        try:
            return p.read_text(encoding="utf-8")
        except Exception:
            pass
    # Fallback: try to find in data/ subdirectories
    fname = Path(path).name
    data_dir = REPO_ROOT / "data"
    if data_dir.exists():
        for subdir in data_dir.iterdir():
            if subdir.is_dir():
                candidate = subdir / fname
                if candidate.exists():
                    try:
                        return candidate.read_text(encoding="utf-8")
                    except Exception:
                        pass
    return ""


def distill_sidebar():
    """側邊欄主題清單；回傳選定的主題名稱。"""
    topics = _load_index()
    if not topics:
        return None
    st.markdown("**📚 蒸餾成果 — Distill Showcase**")
    names = sorted(topics.keys())
    selected = st.radio(
        f"共 {len(topics)} 個主題", names, label_visibility="collapsed", horizontal=True
    )
    return selected


def render_distill(selected=None):
    """主畫面：顯示選定主題的內容。"""
    st.title("📚 Distill Showcase — 蒸餾成果展示平台")
    topics = _load_index()
    if not topics:
        st.warning("尚無蒸餾主題。")
        return

    # Check URL query params for pre-selected topic
    query_params = st.query_params
    pre_selected = query_params.get("topic", None)
    names = sorted(topics.keys())
    if pre_selected and pre_selected in names:
        selected = pre_selected

    if selected is None:
        selected = names[0] if names else None

    if selected and selected in topics:
        info = topics[selected]
        md_files = info.get("md_files", [])
        if not md_files:
            st.info("無檔案")
            return

        # Extract title from each md file (first # heading)
        file_labels = []
        for f in md_files:
            c = _read_md(f)
            title = Path(f).name
            for line in c.splitlines():
                if line.startswith("# "):
                    title = line[2:].strip()
                    break
            file_labels.append(title)

        # Left/Right columns layout
        left, right = st.columns([2, 8])

        with left:
            st.subheader("子檔案選擇")
            selected_label = st.radio("選擇檔案", file_labels, key="subfile_radio")
            selected_idx = file_labels.index(selected_label)
            selected_path = md_files[selected_idx]
            selected_file = Path(selected_path).name

        with right:
            st.header(f"📁 {selected}")
            st.caption(
                f"來源：{info.get('source', 'N/A')} | 檔案數：{info.get('count', 0)}"
            )
            st.markdown(f"**路徑**：`{info.get('path', 'N/A')}`")

            if selected_path:
                content = _read_md(selected_path)
                st.markdown(content)
                st.download_button(
                    "下載", content, file_name=selected_file, mime="text/markdown"
                )

    # 搜尋功能
    search_query = st.text_input("🔍 搜尋關鍵字", key="distill_search")
    if search_query:
        st.subheader(f"搜尋結果：{search_query}")
        results = []
        for name, info in topics.items():
            for f in info.get("md_files", []):
                content = _read_md(f)
                if search_query.lower() in content.lower():
                    results.append((name, f, content))
        if results:
            for name, f, content in results:
                with st.expander(f"{name} — {Path(f).name}"):
                    st.markdown(content[:2000])
        else:
            st.info("無搜尋結果")
