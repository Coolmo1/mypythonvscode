import streamlit as st
import pandas as pd

# create only one dictionary of 3 football players, 
# stating they number of games played, goals scored, assist made, red cards and yellow cards
# convert this into dataframe and display it

footballplayers = {"Name" : ["Ronaldo","Messi","Saurez"], "Games played" : [1200,889,263], "Goals scored" : [873,821,500], "Assist made" : [268,367,293], "Yellow Cards" :[120,90,100], "Red cards" : [11,3,50]}

df = pd.DataFrame(footballplayers)

st.dataframe(df)