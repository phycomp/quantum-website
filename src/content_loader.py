"""內容載入器：從家目錄載入量子/PQC/QKD/ECC 內容。"""

import os
import glob

HOME = os.path.expanduser("~")

SOURCES = {
    "PQC": os.path.join(HOME, "量子", "PQC"),
    "ECC": os.path.join(HOME, "量子", "橢圓加密"),
}


def load_markdown_files(source_key):
    base = SOURCES.get(source_key)
    if not base or not os.path.isdir(base):
        return []
    files = []
    for root, _, fs in os.walk(base):
        for f in fs:
            if f.endswith(".md"):
                path = os.path.join(root, f)
                try:
                    with open(path, encoding="utf-8") as fh:
                        content = fh.read()
                    files.append({"path": path, "name": f, "content": content[:2000]})
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
