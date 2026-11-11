"""量子主題 → YouTube 上傳貼文產生器。

讀取 data/topics/[0-9]*.md（00_索引 除外，共 13 個主題），
依 quantum.md 內容模板（視頻腳本結構 / 關鍵字 / 目標平台）
產生 data/yt_posts/NN_*.md 上傳貼文草稿。

冪等：重跑覆蓋；主題檔更新後重跑即可同步貼文。
"""

import glob
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOPICS_DIR = os.path.join(REPO, "data", "topics")
OUT_DIR = os.path.join(REPO, "data", "yt_posts")

POST_HEADER = "> 對應主題：data/topics/{topic_file}\n> 產生：scripts/gen_yt_posts.py（模板：quantum.md）\n"


def parse_topic(path):
    """解析主題檔：標題、來源註記、H2 章節、首段摘要。"""
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    lines = text.split("\n")

    title = ""
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            break
    # 去「Topic N：」前綴
    title = re.sub(r"^Topic\s*\d+\s*[：:]\s*", "", title)

    headings = [
        m.group(1).strip() for m in (re.match(r"^##\s+(.+)$", l) for l in lines) if m
    ]
    headings = [h for h in headings if h not in ("來源文件",)]

    # 首段摘要：第一個非標題、非表格、非註記、≥ 20 字的連續文字
    para, buf = [], []
    for line in lines[1:]:
        s = line.strip()
        if s.startswith(("#", ">", "|", "---")):
            if para:
                break
            continue
        if not s:
            if buf:
                para.append("".join(buf))
                buf = []
            continue
        buf.append(s)
        if len("".join(buf)) >= 30:
            para.append("".join(buf))
            break
    summary = (
        (para[0][:160] + "…")
        if para and len(para[0]) > 160
        else (para[0] if para else "")
    )

    return {
        "file": os.path.basename(path),
        "num": os.path.basename(path).split("_", 1)[0],
        "title": title or os.path.basename(path),
        "headings": headings,
        "summary": summary,
    }


def keywords_for(title):
    """依主題標題對應關鍵字（結合市場分析之關鍵字池）。"""
    kws = ["量子", "quantum"]
    checks = [
        (
            ("PQC", "後量子"),
            ["PQC", "post-quantum cryptography", "NIST", "Kyber", "Dilithium"],
        ),
        (("QKD", "金鑰分發"), ["QKD", "quantum key distribution", "BB84"]),
        (("HNDL",), ["HNDL", "harvest now decrypt later", "先竊取後解密"]),
        (("台灣",), ["台灣資安", "Taiwan", "資安政策"]),
        (("橢圓", "ECC"), ["ECC", "elliptic curve", "橢圓曲線加密"]),
        (("演算法",), ["quantum algorithm", "Shor", "Grover"]),
        (("晶片", "硬體"), ["PQC 晶片", "硬體安全", "post-quantum chip"]),
        (("Signal", "協定"), ["Signal protocol", "加密通訊", "end-to-end encryption"]),
        (("商業", "PQBridge"), ["PQC 導入", "企業資安", "PQC migration"]),
        (("多通道",), ["MDI-QKD", "多通道平行", "量子網路"]),
    ]
    for keys, add in checks:
        if any(k in title for k in keys):
            kws.extend(add)
    # 去重保序
    return list(dict.fromkeys(kws))


def build_post(topic):
    kws = keywords_for(topic["title"])
    covers = "\n".join(f"- {h}" for h in topic["headings"][:6]) or "- 核心概念導覽"
    kw_line = ", ".join(kws)
    hashtags = " ".join("#" + k.replace(" ", "") for k in kws[:6])

    return f"""# {topic["num"]} {topic["title"]} — YouTube 上傳貼文

{POST_HEADER.format(topic_file=topic["file"])}

## 🎬 影片標題
3 分鐘看懂{topic["title"]}

## 📝 影片說明
本影片介紹{topic["title"]}的重點：{topic["summary"] or "核心概念、應用情境與最新進展。"}

**本影片涵蓋**
{covers}

**腳本時間軸（依內容模板 quantum.md）**

| 時間 | 段落 | 內容 |
|------|------|------|
| 0:00 | 開場 | 問題引入（30s） |
| 0:30 | 原理 | {topic["title"]}說明（60s） |
| 1:30 | 實作 | 應用與案例展示（60s） |
| 2:30 | 結論 | 重點整理與 CTA（30s） |

**CTA**
訂閱頻道掌握量子資安最新進展，留言告訴我們你想深入了解的主題。

## 🏷️ 關鍵字與標籤
{kw_line}

{hashtags}

## 📱 目標平台
- YouTube（約 3 分鐘完整版）
- YouTube Shorts / TikTok / Instagram Reels（60s 精華版）
"""


def main():
    paths = sorted(glob.glob(os.path.join(TOPICS_DIR, "[0-9]*.md")))
    paths = [p for p in paths if not os.path.basename(p).startswith("00_")]
    if not paths:
        print("[FAIL] data/topics 無主題檔")
        sys.exit(1)

    os.makedirs(OUT_DIR, exist_ok=True)
    for p in paths:
        topic = parse_topic(p)
        name = re.sub(r"[^\w\u4e00-\u9fff（）()\-]+", "_", topic["title"]).strip("_")
        out = os.path.join(OUT_DIR, f"{topic['num']}_{name}.md")
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(build_post(topic))
        print(f"[OK] {os.path.basename(out)}")
    print(f"\n共產生 {len(paths)} 份上傳貼文 → data/yt_posts/")


if __name__ == "__main__":
    main()
