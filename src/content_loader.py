"""內容載入器：載入量子/PQC/QKD/ECC 與量化主題內容。

優先順序（2026-11-11 事故修正）：
  Topics / Quant 一律「repo data/ 優先」— 與 Streamlit Cloud 行為一致。
  原本「家目錄優先、repo 為 fallback」會在本機掩蓋 repo 缺檔
  （本機讀到 ~/量化/topics 的 9 檔，雲端只剩 1 個合併檔），
  導致「quant 主題無法上線」且本機測試永遠看不出來。
  repo data/ 由 push-streamlit 技能的 scripts/sync_topics.py 與家目錄來源保持一致。

PQC / ECC 只存在於家目錄（供本機全文搜尋），雲端不存在時自動為空。
"""

import os

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOME = os.path.expanduser("~")


def _first_dir(*candidates):
    """回傳第一個存在的目錄；皆不存在時回傳最後一個（上層會回空清單）。"""
    for p in candidates:
        if p and os.path.isdir(p):
            return p
    return candidates[-1]


SOURCES = {
    # repo data 優先（同步來源：~/量子/PQC/topics、~/量化/topics）
    "Topics": _first_dir(
        os.path.join(REPO_ROOT, "data", "topics"),
        os.path.join(HOME, "量子", "PQC", "topics"),
    ),
    "Quant": _first_dir(
        os.path.join(REPO_ROOT, "data", "quant_topics"),
        os.path.join(HOME, "量化", "topics"),
    ),
    # 僅本機搜尋用（雲端不存在）
    "PQC": os.path.join(HOME, "量子", "PQC"),
    "ECC": os.path.join(HOME, "量子", "橢圓加密"),
}


def load_markdown_files(source_key):
    """遞迴載入某來源目錄下所有 md（排除隱藏檔）。"""
    base = SOURCES.get(source_key)
    if not base or not os.path.isdir(base):
        return []
    files = []
    for root, _, fs in os.walk(base):
        for f in fs:
            if f.endswith(".md") and not f.startswith("."):
                path = os.path.join(root, f)
                try:
                    with open(path, encoding="utf-8") as fh:
                        content = fh.read()
                    files.append({"path": path, "name": f, "content": content})
                except Exception:
                    pass
    return files


def load_all():
    result = {}
    for key in SOURCES:
        result[key] = load_markdown_files(key)
    return result


def search_content(keyword):
    results = []
    for key, files in load_all().items():
        for f in files:
            if (
                keyword.lower() in f["content"].lower()
                or keyword.lower() in f["name"].lower()
            ):
                results.append(
                    {"source": key, "file": f["name"], "snippet": f["content"][:300]}
                )
    return results


def load_topic_files():
    """載入 Topics 目錄下的主題檔案（編號開頭；排除子目錄如 fb_posts/）。"""
    base = SOURCES["Topics"]
    if not base or not os.path.isdir(base):
        return []
    files = []
    for f in sorted(os.listdir(base)):
        if f.endswith(".md") and f[0].isdigit():
            path = os.path.join(base, f)
            try:
                with open(path, encoding="utf-8") as fh:
                    content = fh.read()
                title = (
                    f.replace(".md", "").split("_", 1)[-1]
                    if "_" in f
                    else f.replace(".md", "")
                )
                for line in content.split("\n"):
                    if line.startswith("# "):
                        title = line[2:].strip()
                        break
                files.append(
                    {"path": path, "name": f, "title": title, "content": content}
                )
            except Exception:
                pass
    return files
