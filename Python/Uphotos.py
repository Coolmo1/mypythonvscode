import streamlit as st
import pandas as pd


menu = st.sidebar.selectbox("Menu",["Upload CSV","Upload Images", "Upload Audios","Upload Files","Upload Videos"])

if menu == "Upload CSV":
    uploadcsv = st.file_uploader("Upload you CSV", type = "csv")
    if uploadcsv:
        readcsv = pd.read_csv(uploadcsv)
        st.table(readcsv)


if menu == "Upload Images":
    st.header("Upload Images here")
    imageb = st.radio("Choose an option",["Choose","Take a pic","Upload Image"])

    if imageb == "Upload Image":
        uploadimage = st.file_uploader("Upload your image",type = ["png","jpg","jpeg"])
        if uploadimage:
            st.image(uploadimage)
    elif imageb == "Take a Pic":
        uploadimage = st.camera_input("Smile for the camera")
        if uploadimage:
            st.image(uploadimage)
    
