"""搜尋模組：網頁搜尋 + 本地內容搜尋。"""

import sys

sys.path.insert(0, "/home/sam/quantum_website")
from src.content_loader import search_content


def web_search(query):
    """使用 websearch 工具的替代：回傳搜尋建議。"""
    # 本地內容搜尋
    local = search_content(query)
    return {"query": query, "local_results": local, "web_results": []}


def search_all(keyword):
    return search_content(keyword)
