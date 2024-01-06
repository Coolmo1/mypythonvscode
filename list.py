# classwork:
# create a list.py file
# -tell us what a list is in python
# -create an example of a list and display all the list items in python
# -give 3 examples of how to use a list in streamlit (radio, selectbox, sidebar)

import streamlit as st

st.write("List can be used to store a lot of Data into one Variable")

names = ["Jason", "Luke", "Charlotte"]

st.write(names)

st.radio("Gender",["Male","Female"])
st.selectbox("Clothes",["Jeans","T-shirts","Dress"])
st.sidebar.selectbox("Groceries",["Fruits","Dairy","Pastries"])