import streamlit as st

if "number" not in st.session_state:
    st.session_state.number = 5


st.write(st.session_state.number)

def add():
    st.session_state.number +=1

if st.button("Add 1",on_click=add):
    pass

def subtract():
    st.session_state.number -=1


if st.button("Subtract 1",on_click=subtract):
    pass



