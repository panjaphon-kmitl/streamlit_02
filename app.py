import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')

# ----- Intro -----
st.markdown('สวัสดี! *Streamlit*')
st.title('Layout and Decoration')
st.write("""
  เราจะลองทำ San Francisco Dataset กันดู
""")

# ----- Data -----
trees_df = pd.read_csv('trees.csv')

owners = st.sidebar.multiselect("Tree Owner Filter", trees_df['caretaker'].unique())
query = '(index == index or index != index)'

if owners != []:
    query += ' and caretaker in @owners'

trees_df = trees_df.query(query)
df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']

st.divider()

# ------ Columns ------
col1,col2,col3 = st.columns(3)
with col1:
    st.write('Column1')
    st.line_chart(df_dbh_grouped)
with col2:
    st.write('Column2')
    st.bar_chart(df_dbh_grouped)
with col3:
    st.write('Column3')
    st.area_chart(df_dbh_grouped)
st.divider()

# ------ Tabs ------
# tab1,tab2,tab3 = st.tabs(["Line", "Bar", "Area"])
# with tab1:
#     st.write('Column1')
#     st.line_chart(df_dbh_grouped)
# with tab2:
#     st.write('Column2')
#     st.bar_chart(df_dbh_grouped)
# with tab3:
#     st.write('Column3')
#     st.area_chart(df_dbh_grouped)
# st.divider()

# ------ Map ------
# trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
# trees_df = trees_df.sample(n=1000, replace=True)
# st.map(trees_df)
# st.divider()

# ------ Conclusion ------
st.caption('กราฟแสดงจำนวนต้นไม้ จัดกลุ่มตามเส้นผ่าศูนย์กลาง')
st.title('แปรผล')
st.write('ส่วนใหญ่ของต้นไม้ใน SF มีเส้นผ่าศูนย์กลาง 3\' (2,721 ต้น)')