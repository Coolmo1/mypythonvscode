import streamlit as st

st.title("Find out your BMI(Body Mass Index)")

with st.form(key="BMI"):
    hwcol1,hwcol2 = st.columns()
    st.subheader("ENter in your height")
    with hwcol1:
        mheigth = st.number_input("Enter in your height in metres")
        kgweight = st.number_input("Enter in your weight in kilogramms")

    with hwcol2:
        fheight = st.number_input("Enter in your height in inches")
        lbsweight



