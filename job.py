"""create a job opportunity and job search python app.
user can submit job oppurtunities with various categories
user can search for jobs too with various categories and levels as filters
like (job sector, experience, contract status, experience years, educational level etc)
apply by sending a email to job poster"""

import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
contries = pd.read_csv("countries.csv")
dpment = pd.read_csv("departments.csv")

Menu = st.sidebar.selectbox("Menu",["Job application","Job opportunity"])

st.title("Find your dream Job")

if Menu == "Job application":
    col1,col2 = st.columns(2)
    with col1:
        location = st.selectbox("**Location**",contries["Country"].tolist())
        Role =st.selectbox("**Role**",dpment["Roles"].tolist())
        email = st.text_input("**Email**")

    with col2:
        salary = st.number_input("Salary")
        type = st.selectbox("**Type**",["Remote","In Office"])
        pdate = st.date_input("Posting Date")


    jobdecon = st.text_area("Job Description", height=400)

    #if st.button("Submit"):


    
