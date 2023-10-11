import streamlit as st




st.title("Welcome to my savings app")

st.subheader("I will need sum personal informaotion")

"""
Those wil be your...

* Name

* Age

* The amount of money you spent


"""

Name = st.text_input("Enter in your name")

Age = st.number_input("Enter in your Age" , value = 1, step=1, format="%d")

if Age > 12 :

    Sunday = st.number_input("Enter in how you would normaly spend on sunday")


    Saturday = st.number_input("Enter in how you would normaly spend on saturday")

    Sundays = st.number_input("Enter in how much you spent this sunday ")


    Saturdays = st.number_input("Enter in how much you spent this saturday")

    savingssun = Sunday - Sundays

    savingssat = Saturday - Saturdays

    totsav = savingssat +savingssun

    if totsav > 0 :
        st.success(f"Your Savings this weekend is {totsav} keep up the good work")

    elif totsav < 0:
        st.error(f"Your Savings this weekend is {totsav}. Try and save more next time")
else:
    st.write("You are not old enough to use this app")

