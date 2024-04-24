"""write a python program for house buyers
Ask them for their name
ask them for their yearly salary
If the earn between 100000-500,000 they can buy a bungalow
If the earn between >500,000-1,000,000 they can buy a duplex
If the earn between >1,000,000-5,000,000 they can buy a manshion
create a database to to store and view their answers and display in another customer section"""

import streamlit as st
import pandas as pd

df = pd.read_csv("realestate.csv")

ysalary = st.number_input("Enter in your yearly salary")
name  =  st.text_input("Enter in your name ")

if st.button("search houses"):
    if ysalary > 99_999 and ysalary < 500_001:
        house = "Bungalo"
        st.write("You can a bungalo")

    elif ysalary > 500000 and ysalary < 1_000_001:
        house = "duplex"
        st.write("You can buy a duplex")

    elif ysalary > 1_000_000 and ysalary < 5_000_001:
        house = "Mashion"
        st.write("You can buy a mashion")
    else:
        st.error("You dont have enough money")

    if name and ysalary:
        house_dict = {"Name" : [name], "Yearly Salary" : [ysalary], "House Type" : [house]}
        house_df = pd.DataFrame(house_dict)
        newhouse_df = pd.concat([df,house_df], ignore_index=True)
        newhouse_df.to_csv("realestate.csv", index=False)

st.dataframe(df)