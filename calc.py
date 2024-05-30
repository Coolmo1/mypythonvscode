"""Create a an Arithmetic Calculator that performs addition, subtraction, division and multiplication operation between two numbers.

Ensure to add an image if you wish and also make use of buttons ‘+’, ‘-‘, ‘/‘, and ‘*’."""

import streamlit as st
from PIL import Image as i

num1 = st.number_input("Enter in a Number")
num2 = st.number_input("Enter in a number")


col1,col2,col3,col4 = st.columns(4)

with col1:
    img1 = i.open(R"C:\Users\adeol\OneDrive\Documents\Moyo\Python\Plus-Symbol-Vector-PNG-Cutout-2991627449.png")
    st.image(img1,use_column_width=True)
    if st.button("**+**"):
        total = num1 + num2
        st.write(total)

with col2:
    img2 = i.open(R"C:\Users\adeol\OneDrive\Documents\Moyo\Python\9cR5Mn79i-2645471374.png")
    st.image(img2,use_column_width=True)
    if st.button("**-**"):
        total = num1 - num2
        st.write(total)

with col3:
    img3 = i.open(R"C:\Users\adeol\OneDrive\Documents\Moyo\Python\times.png")
    st.image(img3,use_column_width=True)
    if st.button("x"):
        total = num1 * num2
        st.write(total)
        
with col4:
    img4 = i.open(R"C:\Users\adeol\OneDrive\Documents\Moyo\Python\division-sign-3-43797849.png")
    st.image(img4,use_column_width=True)
    if st.button("/"):
        total = num1 / num2
        st.write(total)
