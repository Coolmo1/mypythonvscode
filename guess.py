import streamlit as st
import random

st.title("Guess my Number")



PN = st.number_input("Guess my number", 1,5)

if "RNG" not in st.session_state:
    st.session_state.RNG = random.randint(1,5) 

def restart():
    st.session_state.RNG = random.randint(1,5)

if st.button("Guess"):
    if PN < st.session_state.RNG:
        st.error("You guess to low")

    elif PN == st.session_state.RNG:
        st.success("You guesed my number")
        st.button("Restart",on_click=restart)
            
            
    elif PN > st.session_state.RNG:
        st.error("You guessed to high")

