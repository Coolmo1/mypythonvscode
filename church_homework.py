'''
CLASSWARK
A church asks members of their age:
if the member is less than 13, please go to the kids class
if the member is from 13 to 19, please go to the teens class
if the member is older than 19, you can go to the adult class

Any age between 0 - 2 is not not allowed yet in church
Any age below 0 is an error, not acceptable (not a valid age)
'''

import streamlit as st
from PIL import Image

st.title("Church")
img = Image.open(R"C:/Users/adeol/OneDrive/Desktop/pythonvscode/bourg-en-bresse-3599450_640.jpg")

st.image(img,use_column_width=True)

st.image("https://cdn.pixabay.com/photo/2013/04/09/08/08/building-102110_1280.jpg")

Age = st.number_input("Enter your Age", 0 , 150, value = 0, step=1, format="%d" )

if st.button("Check class"):
    if Age < 3 and Age > -1 :
        st.warning("You are not allowed to church yet. But you can either take him / her with you to the Adult church or to the nursing area")

    elif Age < 13 and Age > -1 :
        st.write("You can go to the kids class. But if any child starts crying we will send it to the nursing area or the parents.")

    elif Age > 12 and Age < 20 and Age > -1 :
        st.write("You can go the Teenage/youth church.")
     
    elif Age > 19 :
       
     st.write("You are going to the adult church")


 

