"""
-Create a dinner app that welcomes users and shows them the food selections
-Add a restaurant picture
-If they choose/select their meals, show them the total amount
-Ask a question if you want to share the bill with others
-if yes, then ask how many people want to share the bill
-Then show the amount each person must contribute to pay the bill
"""

import streamlit as st
from PIL import Image
st.set_page_config(layout="wide")

cost=0
img4 = Image.open(R"C:\Users\adeol\Downloads\pasta face.jpg")
st.title("Pastalino")
st.image(img4)
st.header("This is our menu") 

st.subheader("Pasta")
pasta1,pasta2,pasta3,pasta4 = st.columns(4)

with pasta1:
    img = Image.open(R"C:\Users\adeol\Downloads\spaghettti (2).jpg")
    st.image(img)
    if st.checkbox("Spaghetti :15 "):
        cost+= 15
        if st.checkbox("Bolognaise sauce : 5"):
            cost += 5
            st.success("Added to menu")

        elif st.checkbox("tomato sauce : 2"):
            cost += 2
            st.success("Added to menu")

        elif st.checkbox("carbonara sauce : 5"):
            cost+=5
            st.success("Added to menu")

        elif st.checkbox("no sauce"):
            st.success("Added to menu")

with pasta2:
      img1 = Image.open(R"C:\Users\adeol\Downloads\fettuchine.jpg")
      st.image(img1)
      if st.checkbox("Fettuccine : 20 "):
        cost+= 20
        if st.checkbox("Bolognaise sauce : 5",key=1):
            cost += 5
            st.success("Added to menu")

        elif st.checkbox("tomato sauce : 2",key= 2):
            cost += 2
            st.success("Added to menu")

        elif st.checkbox("carbonara sauce : 5",key=3):
            cost+=5
            st.success("Added to menu")

        elif st.checkbox("no sauce" ,key=4):
            st.success("Added to menu")

with pasta3:
    img2 = Image.open(R"C:\Users\adeol\Downloads\farfalle.jpg")
    st.image(img2)
    if st.checkbox("Farfalle : 10 "):
        cost+= 10
        if st.checkbox("Bolognaise sauce : 5",key=5):
            cost += 5
            st.success("Added to menu",key=3)

        elif st.checkbox("tomato sauce : 2",key=6):
            cost += 2
            st.success("Added to menu")

        elif st.checkbox("carbonara sauce : 5",key=7):
            cost+=5
            st.success("Added to menu")

        elif st.checkbox("no sauce",key=8):
            st.success("Added to menu")

with pasta4:
    img3 = Image.open(R"C:\Users\adeol\Downloads\conchgliette.png")
    st.image(img3)
    if st.checkbox("Conchigliette : 7.50 "):
        cost+= 7.50
        if st.checkbox("Bolognaise sauce : 5",key=9):
            cost += 5
            st.success("Added to menu")

        elif st.checkbox("tomato sauce : 2",key=10):
            cost += 2
            st.success("Added to menu")

        elif st.checkbox("carbonara sauce : 5",key=11):
            cost+=5
            st.success("Added to menu")

        elif st.checkbox("no sauce",key=12):
            st.success("Added to menu")



if st.button("The check"):
    st.write(f"The total cost of this meal is {cost}")

            
        

    



