import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.write('Interavtive Widgets')


# 2カラムにする。カラムにしたい値を（）に入れる。今回は２なので２。
left_column, right_column = st.beta_columns(2)
# 左側にボタンを追加、右側にテキストを表示する。
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')
# 右カラムに文字を表示ボタンを押すと、ここは右カラムと出現する。

# イクスパンダー
expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')
# 問い合わせ　＋
# と表示され、＋を押すと、問い合わせ内容を書く　- と表示される。

# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味：', text
# 'コンディション：', condition