"""CLASS ASSESSMENT
1.What is streamlit used for?
2.show 8 ways to display text on streamlit
3.show how to ask for a text on streamlit
4.show how to ask for a number on streamlit
5.create a button on the left column but show the output on the right column
6.create a radio button with a horizontal orientation
7.import an image with a 150*150 size
8. read and dispay a CSV file in python
9.create a toggle option to display any database/dataframe
10.create a dictionary of 5 different cars with 5 attributes (without using a CSV file)
and convert it to a dataframe/table"""

#1. Streamlit is used to display python code online on a website

import streamlit as st
from PIL import Image
import pandas as pd

#2
st.write("Hello")
st.subheader("Helloo")
st.header("Hello")
st.title("Hello")
st.error("Hello")
st.warning("Hello")
st.success("Hello")

#3
st.text_input("Type in your name")

#4
st.number_input("Enter in your age")

#5
col1,col2 = st.columns(2)

number = 5

with col1:
    if st.button("Add"):
        number =+ 1

with col2:
    st.write(number)        

#6
st.radio("GEnder",["Male","Female"],horizontal=True)

#7
st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.JIVcG9s8quPw0mLZdkiCeQHaBP%26pid%3DApi&f=1&ipt=5fa017344c9e7550430395882495a18195f0ffb8b28fd69ff5d334576160bfc9&ipo=images", width=150)

#8
df = pd.read_csv("CLASSASSESSMENT.csv")
st.dataframe(df)

#9
if st.button("Click me"):
    st.write("Boo!!!!")

#10
cardict = {"Name" : "Natroginma", "Year invented" : "2023", "Product sold" : 1009000, "Colour" : "Red", "Weight" : "8800kg"}
st.dataframe(cardict)



