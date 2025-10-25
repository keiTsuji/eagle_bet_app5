import streamlit as st
import pandas as pd

# -------------------------------------------
# タイトル
# -------------------------------------------
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

# -------------------------------------------
# データ準備
# -------------------------------------------
players = ["菅井", "辻", "木村", "霜田"]
categories = ["優勝", "ベスト", "ドラニヤ", "バーディ", "ストローク"]
results = pd.DataFrame(0, index=categories, columns=players)

# 優勝
st.subheader("🏆 優勝（1000）")
winner_victory = st.radio("優勝者を選択", players)
for p in players:
    results.loc["優勝", p] = 1000*3 if p == winner_victory else -1000

# ベスト・ドラニヤ・バーディ
awards = [("ベスト", 200), ("ドラニヤ", 300), ("バーディ", 500)]
for cat, value in awards:
    st.subheader(f"{cat}（単価 {value}）")
    inputs = [int(st.number_input(f"{p} の {cat} 数", min_value=0, value=0)) for p in players]
    for i, p in enumerate(players):
        others_sum = sum(inputs) - inputs[i]
        results.loc[cat, p] = (inputs[i]*3 - others_sum) * value

# ストローク
st.subheader("⛳ ストローク（単価100）")
scores = [int(st.number_input(f"{p} のスコア", min_value=0, value=75)) for p in players]
for i, p in enumerate(players):
    diff_sum = sum(scores[i] - scores[j] for j in range(len(players)) if j != i)
    results.loc["ストローク", p] = -diff_sum * 100

# 合計
results.loc["合計"] = results.sum()

st.markdown("---")
st.subheader("💰 計算結果")

# -------------------------------------------
# 安全にHTMLテーブル作成
# -------------------------------------------
html_table = "<table style='width:100%; border-collapse:collapse; text-align:center;'>"

# ヘッダー
html_table += "<thead><tr><th style='background-color:#f5deb3; padding:6px 8px'></th>"
for p in players:
    html_table += f"<th style='background-color:#f5deb3; padding:6px 8px'>{p}</th>"
html_table += "</tr></thead>"

# ボディ
html_table += "<tbody>"
for idx in results.index:
    # 太線を入れるか判定














