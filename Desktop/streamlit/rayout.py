import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# レイアウトを整える（サイドバーの追加・2カラムレイアウト・イクスパンダー）
# サイドバー
st.sidebar.write('Interavtive Widgets')

text = st.sidebar.text_input('あなたの趣味を教えてください。')
# st.sidebarを足すだけ
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

'あなたの趣味：', text
'コンディション：', condition
# 上記２つはサイドバーに持っていかないのではけておく。

# ▼ここはサイドバーに
# ‣こんなマークで出現
# あなたの趣味を教えてください。
# ■入力
# あなたの今の調子は？
# 0
# 100　■移動させる
# ▼ここはメインに
# Interavtive Widgets
# あなたの趣味：■入力
# コンディション： 53　■移動させた数字に反映
