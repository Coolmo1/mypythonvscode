import streamlit as st

menu = st.sidebar.selectbox("Menu",["Invoice Generator","Change details "])

if menu == "Invoice Generator":
    img1,img2,img3 = st.columns()

    with img1:
        st.image("c:\Users\adeol\Downloads\logo.png")
