import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')

st.markdown('สวัสดี! *Streamlit*')
st.title('Layout and Decoration')
st.write("""
  เราจะลองทำ San Francisco Dataset กันดู
""")

df = pd.read_csv('trees.csv')
df2 = pd.DataFrame(
    df.groupby(['dbh']).count()['tree_id']
)
df2.columns = ['tree_count']

st.divider()

col1,col2,col3 = st.tabs(["Line", "Bar", "Area"])
with col1:
    st.write('Column1')
    st.line_chart(df2)
with col2:
    st.write('Column2')
    st.bar_chart(df2)
with col3:
    st.write('Column3')
    st.area_chart(df2)

st.caption('กราฟแสดงจำนวนต้นไม้ จัดกลุ่มตามเส้นผ่าศูนย์กลาง')
st.title('แปรผล')
st.write('ส่วนใหญ่ของต้นไม้ใน SF มีเส้นผ่าศูนย์กลาง 3\' (2,721 ต้น)')