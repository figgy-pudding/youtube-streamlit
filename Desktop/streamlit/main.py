import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
# 画像を表示させる。

# タイトル
st.title('Streamlit 入門')
# 表の使い方
st.write('DataFrame')
# DataFrame:write以外にもある。

df = pd.DataFrame({
    '1列目':[1, 2, 3, 4],
    '2列目':[10, 20, 30, 40]
})

# 表(テーブル)を表示させる
st.write(df)
# 表示させたいデータフレームをこの中（df）に入れる
# 指定できる引数がdataframeと異なる。

# st.write(df)から dataframe（動的な表）に変更する。
st.dataframe(df, width=100, height=100)
# なんと st.write(df)と同じ表が作成される。
# 全体の表の大きさ（縦と横）をピクセル単位で指定することができる。writeにはない引数指定をすることができる。

# ハイライトを付ける。
st.dataframe(df.style.highlight_max(axis=0))# , width=100, height=100)
# 列もしくは行の最大のものをハイライトしてあげる。列で最大値にハイライトを付けてみる。

# スタティック（静的な）な表を作りたい時に使用する。ソートができないため、ただ表を表示させたい時に使用する。
st.table(df.style.highlight_max(axis=0))

# マジックコマンド - マークダウン記法を適用することができる - ```←バッククォーテーション
# 上から順に見出し１、見出し２、見出し３
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""
# ```で囲ったところはPythonのコードを書きますよ、という表記方法、しかもHP上でコピーすることができる優れもの！

# st.latex(r'''
#     a + ar + a t^2 + a r^3 + \cdots + a r^{n-1} =
#     \sum_{k=0}^{n-1} ar^k =
#     a \left(\frac{1-r^{n}}{1-r}\right)
#     ''')

# チャートを描く - 折れ線グラフ📈　カラム：表の上にある項目名、vscode, URL先では表示不可。ここでjupiterを落とそうとして初期化する羽目に。。多分。
df = pd.DataFrame(
    np.random.rand(20, 3), # 縦に２０個、横に３つの行列
    columns=['a', 'b', 'c']
)
# vs codeでの表示方法 - 折れ線グラフ📈
st.line_chart(df)

# エリアチャート - エリアを囲ってくれている。折れ線塗り潰しグラフ。
st.area_chart(df)

# 棒グラフ - 引数＝パラメーター
st.bar_chart(df)

# マップをプロットする。（matplotlibのこと）
# 東京付近 - 緯度・経度[35.69, 139.70]
df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70], # １００箇所の情報を表にまとめたもの
    columns=['lat', 'lon'] # 緯度・経度
)
# 地図上にプロットしていく。散布図みたいな感じです。
st.map(df)

# 画像を表示させる。
st.write('Display Image')
# main.py(作業ファイル)と同じ階層にあるものを使用するため、ファイル名をそのまま記述。
img = Image.open('senku.png')
# 表示する。''を絶対忘れずに！エラーになる。
st.image(img, caption='senku ishigami', use_column_width=True)
# (表示させたい画像, 画像のキャプション, use_column_width=True)
# use_column_width=True = 実際のレイアウトのカラム（横幅に合わせて表示してくれる）

# インタラクティブなウィジェット　 - 双方向の会話、一方通行ではない。動的な変化を起こしてくれるもの。
# ウィジェット - つまるところのUI。ユーザーインターフェイス。各機能のパーツ。チェックボックスやスライダー、テキスト入力など、値を動的に変化させていく。

# チェックボックスでメディア表示の有無を作る。
if st.checkbox('Show Image'): # TrueかFalseを返してくれる。チェックが入っていたらTrue、入っていなければFalse。
    img = Image.open('senku.png')
    st.image(img, caption='senku ishigami', use_column_width=True)
# チェックを入れると千空が出現、外すと消える

# セレクトボックス
# optionという変数にst以下の変わる動的な値を入れることができる。
option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    # label
    list(range(1, 11))
    # options - リストで表示させる必要あり。
)
# なんと以下の記載方法でも出来てしまう
'あなたの好きな数字は、', option, 'です。'
# optionの変数が変わると、optionも変わる。

# テキスト入力
st.write('Interavtive Widgets')
text = st.text_input('あなたの趣味を教えてください')
'あなたの趣味：', text
# 入力すると上のあなたの趣味の欄に反映される。

# スライダー
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# label, 数値(最小値、最大値、デフォルトの値（初期値）)
'コンディション：', condition
