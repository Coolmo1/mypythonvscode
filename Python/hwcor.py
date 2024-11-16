import streamlit as st

name = st.text_input("Name")
h= st.number_input("History grade", max_value=4)
m= st.number_input("math grade", max_value=4)
E = st.number_input("english grade", max_value=4)
b = st.number_input("biology grade", max_value=4)
f = st.number_input("french grade", max_value=4)

total = h+m+E+b+f
avr = total/5

if avr < 2.5:
    st.write("you are not allowed to register for any courses")
elif avr >= 2.5 and avr <3:
    st.write("You are regitister for 2 courses")
elif avr >= 3 and avr <3.5:
    st.write("You are can register for 3 courses")
elif avr == 4:
    st.write("You can register for 4 courses")