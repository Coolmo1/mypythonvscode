import streamlit as st
import pandas as pd

studentgrades = ["Maya",10,50,20]

st.write(studentgrades)

studentgrades = {"Name": ["Maya","Kyra"], "Sience" : [10,20], "Math" : [50,30], "English" : [20,80]}

st.write(studentgrades)

table = pd.DataFrame(studentgrades)

st.dataframe(table)