"""Quant 主題檢視測試：標題「Topic N：」前綴去除與清單載入。"""

import sys

sys.path.insert(0, "/home/sam/quantum_website")

from src.views.quant_topics import (
    _load_quant_topics,
    _strip_leading_heading,
    _strip_topic_prefix,
)


def test_strip_topic_prefix():
    assert _strip_topic_prefix("Topic 1：台股實盤自動化交易") == "台股實盤自動化交易"
    assert _strip_topic_prefix("Topic 12: 半形冒號") == "半形冒號"
    assert (
        _strip_topic_prefix("量化交易 & 自動化 — 主題索引")
        == "量化交易 & 自動化 — 主題索引"
    )
    print("strip_topic_prefix: PASS")


def test_quant_topics_loaded():
    topics = _load_quant_topics()
    assert len(topics) == 9, f"應載入 9 個主題，實際 {len(topics)}"
    for t in topics:
        label = _strip_topic_prefix(t["title"])
        assert not label.startswith("Topic"), f"前綴未去除：{label}"
        assert label, "去除前綴後標題為空"
    print("quant topics loaded: PASS (9)")


def test_strip_leading_heading():
    content = "# Topic 1：標題\n\n內文第一行\n內文第二行"
    out = _strip_leading_heading(content)
    assert not out.startswith("# "), "H1 未移除"
    assert "內文第一行" in out and "內文第二行" in out
    content2 = "沒有標題的內文"
    assert _strip_leading_heading(content2) == content2
    print("strip_leading_heading: PASS")


if __name__ == "__main__":
    test_strip_topic_prefix()
    test_quant_topics_loaded()
    test_strip_leading_heading()
    print("All quant view tests passed.")
