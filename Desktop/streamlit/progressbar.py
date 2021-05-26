# プログレスバー

# from logging import raiseExceptions - 出力
import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
# 空の要素を追加して、それをlatest_iterationにする。
bar = st.progress(0) # ここの（）は、整数か浮動小数点数にする。

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    # このiはfor i in rangeのi。iが追加されているので数字が変化していく。
    bar.progress(i + 1)
    # progressbaeをどんどん変化させていっている。
    time.sleep(0.1)
    # 1秒後に数字が表示されていく。これがないと一瞬で終わってしまう。
    # 占いのカナウみたいな感じ。

'Done!!'
# pythonは上から処理していくので、time.sleepが終了しないと下は表示されない。逆に言うと、終了すれば表示される。

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')