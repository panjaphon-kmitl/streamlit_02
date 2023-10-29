import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')

# ----- Intro -----
st.markdown('สวัสดี! *Streamlit*')
st.title('Tab Layout')
st.write("""
  เราจะลองทำ San Francisco Dataset กันดู
""")

# ----- Data -----
trees_df = pd.read_csv('trees.csv')
df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']

# ------ Tabs ------
tab1,tab2,tab3 = st.tabs(["Line", "Bar", "Area"])
with tab1:
    st.write('Column1')
    st.line_chart(df_dbh_grouped)
with tab2:
    st.write('Column2')
    st.bar_chart(df_dbh_grouped)
with tab3:
    st.write('Column3')
    st.area_chart(df_dbh_grouped)
st.divider()
