"""台股本益比 / 殖利率 / 股價淨值比查詢（TWSE 每日 BWIBBU_d）。

原始版本（phycomp/vwrStock pages/本益比II.py）為 Colab notebook 匯出，
含 google.colab / !pip 指令無法在 Streamlit 執行 — 此為乾淨重寫版。
"""

from datetime import date, timedelta
from io import StringIO

import pandas as pd
import requests
import streamlit as st

BASE_URL = "https://www.twse.com.tw/exchangeReport/BWIBBU_d"
METRICS = ["本益比", "殖利率(%)", "股價淨值比"]
_HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}


@st.cache_data(ttl=3600, show_spinner=False)
def fetch_bwibbu(day: date):
    """抓取 TWSE 個股日本益比資訊；該日無資料時自動往前找（最多 7 天）。

    回傳 (DataFrame, 實際使用日期)。
    """
    for _ in range(7):
        datestr = day.strftime("%Y%m%d")
        try:
            resp = requests.get(
                BASE_URL,
                params={"response": "csv", "date": datestr, "selectType": "ALL"},
                headers=_HEADERS,
                timeout=15,
            )
            resp.raise_for_status()
        except requests.RequestException as e:
            raise RuntimeError(f"TWSE 連線失敗：{e}") from e

        try:
            df = pd.read_csv(StringIO(resp.text), header=1)
        except Exception:
            df = pd.DataFrame()

        if len(df) > 0 and "證券代號" in df.columns:
            return _clean(df), day

        day = day - timedelta(days=1)

    return pd.DataFrame(), day


def _clean(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # 過濾說明列 / 合計列：證券代號須為純數字
    df = df[df["證券代號"].astype(str).str.strip().str.isdigit()]
    for col in METRICS:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    keep = (
        ["證券代號", "證券名稱"]
        + [c for c in METRICS if c in df.columns]
        + (["財報日期"] if "財報日期" in df.columns else [])
    )
    return df[keep].reset_index(drop=True)


def render_stock_vwr():
    st.title("📈 台股本益比 / 殖利率 / 股價淨值比")
    st.caption("資料來源：TWSE 每日個股日成交資訊（BWIBBU_d）")

    day = st.date_input("日期", value=date.today())

    try:
        df, used = fetch_bwibbu(day)
    except RuntimeError as e:
        st.error(str(e))
        return

    if df.empty:
        st.info(f"{used} 與其前 7 天皆無資料（假日或 TWSE 尚未更新），請換個日期試試。")
        return
    if used != day:
        st.info(f"{day} 當日無資料，已自動改用最近交易日：{used}")

    c1, c2, c3, c4 = st.columns([1.4, 1, 1, 1.6])
    with c1:
        metric = st.radio("指標", METRICS, index=0, horizontal=True)
    with c2:
        n = st.slider("Top N", 5, 50, 10)
    with c3:
        direction = st.radio("排序", ["最高", "最低"], horizontal=True)
    with c4:
        query = st.text_input("搜尋（代號或名稱）", "")

    st.divider()

    if query.strip():
        q = query.strip()
        mask = df["證券代號"].astype(str).str.contains(q, na=False) | df[
            "證券名稱"
        ].astype(str).str.contains(q, na=False)
        shown = df[mask]
        st.markdown(f"符合「{q}」：**{len(shown)} 檔**")
    else:
        valid = df.dropna(subset=[metric])
        shown = (
            valid.nlargest(n, metric)
            if direction == "最高"
            else valid.nsmallest(n, metric)
        )
        st.markdown(f"{metric} **{direction} {n} 檔**（{used}，全市場共 {len(df)} 檔）")

    if shown.empty:
        st.info("沒有符合的資料。")
        return
    st.dataframe(shown, use_container_width=True)
