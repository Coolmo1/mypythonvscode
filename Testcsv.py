import streamlit as st
import pandas as pd


st.set_page_config(layout='wide')

st.title("Registrationpage")
corectpass = "iamcool"
menu = st.sidebar.selectbox('Menu',['Registration','Student File']) 

df = pd.read_csv("Teststucsv.csv")

pass1,pass2 = st.sidebar.columns(2)





if menu == "Student File":
 
    with pass1:
        passw = st.sidebar.text_input("Enter in the correctpassword")
        login = st.sidebar.button("login")
    if login:
        if passw:
            if passw == corectpass:
                st.dataframe(df,use_container_width=True)
            else:
                with pass1:
                    st.sidebar.error("You typed in the wrong password")

        else:
            with pass1:
                st.sidebar.error("Please type in a password")
    

col1, col2 = st.columns(2)

if menu == 'Registration':
    

    with col1:
        name = st.text_input("Enter in your name")

    with col2:    
        age = st.number_input("Enter in your age", value=1)

    gender=st.radio("Gender",["Male","Female"],horizontal=True)

    if st.button("Sumbmit"):
        if name and age and gender :
            menudict = {"Name":[name],"Age":[age],"Gender" : [gender]}
            menu_df= pd.DataFrame(menudict)
            newem_df= pd.concat([df,menu_df],ignore_index = True)
            newem_df.to_csv("Teststucsv.csv",index = False)
            st.success("You have been successfully added")

        else:
            st.error("Fill in all the boxes")



       