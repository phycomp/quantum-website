"""一次性文件整合腳本：把散落本機的關鍵文件複製進 repo data/docs/。

來源（2026-11-11 附錄清單）：
  - ~/渲染邏輯/Oloid/優化自動化全耦合.md      -> data/docs/arduino_wind_turbine.md
      （6 輪 Kimi 設計對話；User:/Kimi: 標記轉為章節標題/內文）
  - ~/物理模擬/topo/指標/自動化TI.md          -> data/docs/topological_insulator.md
      （拓撲量子物態與快速材料預測部署包，加來源註記）
  - ~/軟體/代理人/docs/QUANTUM_MARKET_ANALYSIS.md -> data/docs/quantum_market_analysis.md
  - ~/軟體/代理人/content_templates/quantum.md    -> data/docs/quantum_tline_template.md

注意：與 sync_topics.py（~/量化、~/量子 來源同步）不同，本腳本處理的是
散落本機的單份文件，來源更新後重跑即可覆蓋 repo 副本。
冪等：重複執行結果一致。
"""

import os
import re
import sys

HOME = os.path.expanduser("~")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(REPO, "data", "docs")

SOURCES = {
    "arduino": os.path.join(HOME, "渲染邏輯", "Oloid", "優化自動化全耦合.md"),
    "ti": os.path.join(HOME, "物理模擬", "topo", "指標", "自動化TI.md"),
    "market": os.path.join(
        HOME, "軟體", "代理人", "docs", "QUANTUM_MARKET_ANALYSIS.md"
    ),
    "tline_tpl": os.path.join(
        HOME, "軟體", "代理人", "content_templates", "quantum.md"
    ),
}


def _read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _write(name, text):
    path = os.path.join(DOCS, name)
    os.makedirs(DOCS, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"[OK] -> {path}（{len(text.splitlines())} 行）")


def prepare_arduino():
    text = _read(SOURCES["arduino"])
    # 對話標記轉章節：User: X -> H2「追加需求」；Kimi: 前綴移除
    n_user = len(re.findall(r"^User:\s", text, flags=re.M))
    text = re.sub(r"^User:\s*(.+)$", r"## 💬 追加需求：\1", text, flags=re.M)
    text = re.sub(r"^Kimi:\s*", "", text, flags=re.M)
    header = (
        "# 🌬️ Arduino 風力發電機組 — 3D 列印設計方案\n\n"
        f"> 來源：~/渲染邏輯/Oloid/優化自動化全耦合.md（{n_user} 輪設計對話完整整理）\n"
        "> 整合日期：2026-11-11\n\n"
    )
    _write("arduino_wind_turbine.md", header + text)
    return n_user


def prepare_ti():
    text = _read(SOURCES["ti"])
    lines = text.split("\n")
    # 在 H1 後插入來源註記
    if lines and lines[0].startswith("# "):
        note = [
            "> 來源：~/物理模擬/topo/指標/自動化TI.md（快速材料預測部署包）",
            "> 整合日期：2026-11-11",
        ]
        out = lines[0] + "\n" + "\n".join(note) + "\n" + "\n".join(lines[1:])
    else:
        out = (
            "# 拓撲量子物態與快速材料預測\n\n> 來源：~/物理模擬/topo/指標/自動化TI.md\n"
            + text
        )
    _write("topological_insulator.md", out)


def prepare_plain(src, name):
    _write(name, _read(SOURCES[src]))


if __name__ == "__main__":
    failed = False
    for key, path in SOURCES.items():
        if not os.path.isfile(path):
            print(f"[FAIL] 來源不存在：{path}")
            failed = True
    if failed:
        sys.exit(1)

    n = prepare_arduino()
    prepare_ti()
    prepare_plain("market", "quantum_market_analysis.md")
    prepare_plain("tline_tpl", "quantum_tline_template.md")
    print(f"\n文件整合完成（Arduino 對話 {n} 輪全數保留）。")
