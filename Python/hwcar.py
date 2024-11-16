import streamlit as st

st.title("Car shop")

ys = st.number_input("Yearly Salary",min_value=10000)

if ys < 30000:
    st.write("You can buy a used car")
elif ys >= 30000 and ys < 600000:
    st.write("You can an economy car")
elif ys >= 60000 and ys < 1000000:
    st.write("You can an mid-range car")
elif ys >= 100000 and ys < 2000000:
    st.write("You can an luxury car")
elif ys < 200000 :
    st.write("You can an supercar")