#create a register and login side bar to allow many people to register (username, password)
#then ask them to login checking if their credentials are correct.
#display their name and middle name after a successful login

import streamlit as st
import pandas as pd

Menu = st.sidebar.selectbox("Menu",["Registerpage","Loginpage"])

pass1,pass2 = st.columns(2)

df = pd.read_csv("loginregister.csv")



if Menu == "Registerpage":
    with pass1:
        username = st.sidebar.text_input("Enter in a username")
        password = st.sidebar.text_input("Enter in a password", type = "password")

        if st.sidebar.button("Register"):
            if username and password:
                registridict = {"Username" : [username], "Password" : [password]}
                registridf = pd.DataFrame(registridict)
                newregistrydf = pd.concat([df,registridf],ignore_index=True)
                newregistrydf.to_csv("loginregister.csv",index=False)
                st.success("You have been sucsessfully login")

            else:
                st.warning("Please fill in the boxes")



if Menu == "Loginpage":
    usernamelogin = st.sidebar.text_input("Enter in your username")
    passwordlogin = st.sidebar.text_input("Enter in your password", type = "password")
    if st.sidebar.button("Login"):
        if usernamelogin:
            if passwordlogin:
                search_result = df[df["Username"] == usernamelogin]
                usernameshow = search_result["Username"].iloc[0]
                passwordshow = search_result["Password"].iloc[0]

                if usernameshow == usernamelogin:
                    if passwordshow == passwordlogin:
                        st.write("Welome",usernameshow)
                        st.write("Your password is",passwordshow)

                    else:
                        st.error("Your password is incorrect")

                else:
                    st.error("Your username is incorrect")

            else:
                st.warning("Please type in your password")
        else:
            st.warning("Please type in your username")
