"""Create a python program using streamlit that accepts user age to accredit use for voting. 

Minimum age is 18 years. 
User gets a “Sorry, You are not eligible to vote” response when age falls below minimum.

Otherwise, user gets “Congratulations, You are eligible to vote”

Your interface should have button for user to submit their age and get a response.

Add image"""

import streamlit as st

st.title("Vote now")

age = st.number_input("Age")
vote = st.radio("**Vote**",["Cookies","Brownies"],horizontal=True)



if st.button("Submit vote"):
    if age <18:
        st.error("Sorry, You are not eligible to vote")

    if age >= 18:
        st.success("Congratulations, You are eligible to vote")

st.image("https://www.gannett-cdn.com/presto/2019/03/20/PBIN/e9dfb24f-3532-4245-bb5e-a3b9665583fe-GettyImages-884243522.jpg?crop=4999,2835,x0,y559&width=3200&height=1680&fit=bounds")

