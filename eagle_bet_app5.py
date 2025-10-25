import streamlit as st
import pandas as pd

# -------------------------------------------
# 2025.10.25 最新版（セル色付き）
# -------------------------------------------

# -------------------------
# CSSで number_input の数字を大きく
# -------------------------
st.markdown("""
<style>
input[type=number] {
    font-size: 24px !important;
}
table.dataframe td {
    font-size: 20px;
    text-align: center;
}
table.dataframe th {
    font-size: 16px;
    background-color:#f5deb3;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# タイトル表示（装飾あり）
# -------------------------
st.markdown("""
<div style='
    display:flex;
    justify-content:center;
    align-items:center;
    height:120px;
    background-color:#e0f7fa;
    border-radius:15px;
'>
    <h1 style='font-size:28px; color:#00796b; margin:0; line-height:1;'>🏌️‍♂️イーグル会ベット計算機🏌️‍♂️</h1>
</div>
""", unsafe_allow_html=True)

# -------------------------
# プレイヤー名と結果用データフレーム
# -------------------------
players = ["菅井", "辻", "木村", "霜田"]
categories = ["優勝", "ベスト", "ドラニヤ", "バーディ", "ストローク"]
results = pd.DataFrame(0, index=categories, columns=players)

# -------------------------
# 優勝
# -------------------------
st.subheader("🏆 優勝（1000）")
winner_victory = st.radio("優勝者を選択", players)
for p in players:
    results.loc["優勝", p] = 1000*3 if p == winner_victory else -1000

# -------------------------
# ベスト・ドラニヤ・バーディ
# -------------------------
awards = [("ベスト", 200), ("ドラニヤ", 300), ("バーディ", 500)]
for cat, value in awards:
    st.subheader(f"{cat}（単価 {value}）")
    inputs = [st.number_input(f"{p} の {cat} 数", min_value=0, value=0) for p in players]
    for i, p in enumerate(players):
        others_sum = sum(inputs) - inputs[i]
        results.loc[cat, p] = (inputs[i]*3 - others_sum) * value

# -------------------------
# ストローク
# -------------------------
st.subheader("⛳ ストローク（単価100）")
scores = [st.number_input(f"{p} のスコア", min_value=0, value=75) for p in players]
for i, p in enumerate(players):
    diff_sum = sum(scores[i] - scores[j] for j in range(len(players)) if j != i)
    results.loc["ストローク", p] = -diff_sum * 100

# -------------------------
# 合計
# -------------------------
results.loc["合計"] = results.sum()

st.divider()
st.subheader("💰 計算結果")

# -------------------------
# セルの色付け関数
# -------------------------
def color_cells(val):
    color = ""
    if val > 0:
        color = "#d4edda"   # 緑（プラス）
    elif val < 0:
        color = "#f8d7da"   # 赤（マイナス）
    else:
        color = "#f2f2f2"   # グレー（ゼロ）
    return f"background-color: {color}; color: black; font-weight: bold;"

# -------------------------
# 結果表示（色付き）
# -------------------------
styled_results = results.style.format("{:+,}").applymap(color_cells)
st.dataframe(styled_results, use_container_width=True)

# -------------------------
# CSVダウンロード
# -------------------------
csv = results.to_csv(index=True).encode("utf-8-sig")
st.download_button(
    label="📥 結果をCSVでダウンロード",
    data=csv,
    file_name="eagle_bet_result.csv",
    mime="text/csv"
)






























