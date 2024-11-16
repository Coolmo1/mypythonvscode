"""MAKE IT JUST LIKE THE FOOD ORDER APP. THIS ONE IS A BOOKSTORE

What is your name?

**3. Book Selection:**

Make sure you arrange your books in different categories using the selectbox or radio to switch categories:

Children Books
4 columns each with 2 rows
Image and price with checkbox included
Each book must have an image

Family Books
Christian Books
Science Books

Books in checkboxes with images, names and prices
**Total Amount:**
Based on your selections, the total amount will be calculated automatically.

Mr. tee: get purchased book and plot chart
save each click sales in the database
plot the sales barchart"""

import streamlit as st
from PIL import Image as im

st.title("Bookstore")

menu = st.sidebar.selectbox("Menu",["Children Book","Family Books","Christian Books","Science Books"])

if menu == "Children Book":
    cbook1,cbook2,cbook3,cbook4 = st.columns(4)
    s1,s2,s3,s4 = st.columns(4)
    s1,s2,s3,s4 = st.columns(4)
    s1,s2,s3,s4 = st.columns(4)
    cbook5,cbook6,cbook7,cbook8 = st.columns(4)
    #Row 1
    phcbook1 = im.open(R"C:\Users\adeol\OneDrive\Desktop\pythonvscode\bearbook.png")
    phcbook2 = im.open(R"C:\Users\adeol\OneDrive\Desktop\pythonvscode\book.png")
    phcbook3 = im.open(R"C:\Users\adeol\OneDrive\Desktop\pythonvscode\maltilda.png")
    phcbook4 = im.open(R"C:\Users\adeol\OneDrive\Desktop\pythonvscode\owl moon.png")
    #Row 2
    phcbook5 = im.open(R"C:\Users\adeol\OneDrive\Desktop\pythonvscode\poky little puppy.png")
    phcbook6 = im.open(R"C:\Users\adeol\OneDrive\Desktop\pythonvscode\the cat in the hat.png")
    phcbook7 = im.open(R"C:\Users\adeol\OneDrive\Desktop\pythonvscode\the lorax book.png")
    phcbook8 = im.open(R"C:\Users\adeol\OneDrive\Desktop\pythonvscode\the snowy day.png")
    
        #Row 1
    with cbook1:
        phcbook1 = st.image(phcbook1)
        st.write("Stor")
    with cbook2:
        phcbook2 = st.image(phcbook2)
    with cbook3:
        phcbook3 = st.image(phcbook3)
    with cbook4:
        phcbook4 = st.image(phcbook4)

    #Row 2
    with cbook5:
        phcbook5 = st.image(phcbook5)
    with cbook6:
        phcbook6 = st.image(phcbook6)
    with cbook7:
        phcbook7 = st.image(phcbook7)
    with cbook8:
        phcbook8 = st.image(phcbook8)

    


