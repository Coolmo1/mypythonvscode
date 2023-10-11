import streamlit as st
from PIL import Image

menu = st.sidebar.selectbox("Menu"["Uploud Files","About us"])

if menu == "Uploud Files":
    st.header("Uploud files here")

    image_file = st.file_uploader("Upload your image",type = ["png","jpg","jpeg"])

    if image_file is not None:
        st.image(Image.open(image_file))