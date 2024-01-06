import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("Welcome to my CSV Editor")

upload_csv = st.file_uploader("Upload CSV file",type = ["csv"])
st.write(upload_csv.name)

if upload_csv:
    csv_file = pd.read_csv(upload_csv)
    edit_csv = st.data_editor(csv_file,use_container_width=True)

    if st.button("Save Edited Csv"):
        edit_csv.to_csv(upload_csv.name, index=False)
        st.success("You have been added")
