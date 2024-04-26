"""create a job opportunity and job search python app.
user can submit job oppurtunities with various categories
user can search for jobs too with various categories and levels as filters
like (job sector, experience, contract status, experience years, educational level etc)
apply by sending a email to job poster"""

import streamlit as st

Menu = st.sidebar.selectbox("Menu",[,"Job application",])