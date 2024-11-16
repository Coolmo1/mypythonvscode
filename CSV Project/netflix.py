"""Create a Netflix Movie app clone.. that allows user to login and select a movie category and further select movies on the page.

Make use of attractive movie images, radio button and or checkboxes."""

import streamlit as st
import pandas as pd

menu = st.sidebar.selectbox("Menu",["Sign up","Log in"])
df = pd.read_csv("netflix.csv")

if menu == "Sign up":
    na,ep = st.columns(2)
    with na:
        name = st.text_input("Enter your name")
        age = st.number_input("Enter in your age")
    with ep:
        email = st.text_input("Enter in in your email")
        pasw = st.text_input("Enter in your password")
    
    aofp = st.selectbox("Ammount of people",[1,2,3,4,5,6])
    cost = 0

    if aofp == 1:
        cost == 10
        st.write(cost)
    elif aofp == 2:
        cost == 15
        st.write(cost)
    elif aofp == 3:
        cost == 20
        st.write(cost)
    elif aofp == 4:
        cost == 25
        st.write(cost)
    elif aofp == 5:
        cost == 30
        st.write(cost)
    elif aofp == 6:
        cost == 35
        st.write(cost)
    
    if st.button("Pay"):
        if name and age and email and pasw:
            netflix_dict = {"Name" : [name], "Age" : [age], "Email": [email],"Password":[pasw]}
            netflix_df = pd.DataFrame(netflix_dict)
            newnetflixdf = pd.concat([df,netflix_df],ignore_index=True)
            newnetflixdf.to_csv("netflix.csv", index=False)
            st.success("You have successfuly bought minoflix")
        else:
            st.warning("Fill in all the boxes")

if menu == "Log in":
    lname = st.sidebar.text_input("Enter in your email_Name")
    if st.button("login"):
        if lname in "netflix.csv":
            st.write("hi")