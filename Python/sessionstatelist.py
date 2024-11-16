# A boy went to the supermarket to get a list of items, 
# use ONLY one text box to ask the user for the 5 items he wants to get each time 
# Put each item entered/submitted in the customer’s list
# Display all items in the customer’s list

import streamlit as st

st.title("The Infinty store")

if "userlist" not in st.session_state:
    st.session_state.userlist = []
    



items = st.text_input("Enter in a item that you would lke to puchase")

if st.button("Submit"):
    st.session_state.userlist.append(items)
    st.write("All your items", st.session_state.userlist)


