import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')

# ----- Intro -----
st.markdown('สวัสดี! *Streamlit*')
st.title('Map of San Fransisco Tree')
st.write("""
  เราจะลองทำ San Francisco Dataset กันดู
""")

# ----- Data -----
trees_df = pd.read_csv('trees.csv')

# ------ Map ------
trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
trees_df = trees_df.sample(n=1000, replace=True)
st.map(trees_df)
st.divider()