"""Content loader tests."""

import sys

sys.path.insert(0, "/home/sam/quantum_website")
from src.content_loader import load_all, search_content


def test_load_all():
    data = load_all()
    assert "PQC" in data and "ECC" in data
    print("load_all: PASS")


def test_search():
    res = search_content("量子")
    assert isinstance(res, list)
    print(f"search: PASS ({len(res)} results)")


if __name__ == "__main__":
    test_load_all()
    test_search()
    print("All tests passed.")
