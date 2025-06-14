import streamlit as st
import pandas as pd
st.set_page_config(page_title="Amazon Data Viewer", layout="wide")
file = pd.read_csv('./data/amazon.csv')

st.write("Hello, Streamlit!")
st.write(file)