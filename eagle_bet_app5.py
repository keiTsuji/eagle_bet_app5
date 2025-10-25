import streamlit as st
import pandas as pd

# タイトル
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

# プレイヤー・カテゴリ
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
    inputs = [st.number_input(f"{p} の {cat} 数", min_value=0, value=0) for p in players]
    for i, p in enumerate(players):
        others_sum = sum(inputs) - inputs[i]
        results.loc[cat, p] = (inputs[i]*3 - others_sum) * value

# ストローク
st.subheader("⛳ ストローク（単価100）")
scores = [st.number_input(f"{p} のスコア", min_value=0, value=75) for p in players]
for i, p in enumerate(players):
    diff_sum = sum(scores[i] - scores[j] for j in range(len(players)) if j != i)
    results.loc["ストローク", p] = -diff_sum * 100

# 合計
results.loc["合計"] = results.sum()

st.divider()
st.subheader("💰 計算結果")

# -----------------------------
# pandas styleで装飾
# -----------------------------
def style_cell(val, row_name):
    # マイナス赤文字
    color = 'red' if val < 0 else 'black'
    # 太線（ストローク・合計）
    border = '3px solid black' if row_name in ['ストローク','合計'] else '1px solid black'
    return f'color:{color}; background-color:#faebd7; border-bottom:{border}; text-align:center; font-size:20px; padding:6px 8px'

styled = results.style.applymap(lambda v, row=results.index: '', subset=results.columns)  # placeholder
# applymapだと行名情報がないので、ここでは簡単にHTMLで出力する
# そこで行ごとにスタイル付け
html_rows = ""
for row_name in results.index:
    html_rows += "<tr>"
    html_rows += f"<th style='font-size:16px; background-color:#f5deb3; border-bottom:{'3px solid black' if row_name in ['ストローク','合計'] else '1px solid black'}; text-align:center; padding:6px 8px'>{row_name}</th>"
    for p in players:
        val = results.loc[row_name,p]
        color = 'red' if val < 0 else 'black'
        bord

























