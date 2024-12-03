import streamlit as st
import pandas as pd

file = pd.read_csv("home.csv")

st.dataframe(file)