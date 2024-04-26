import streamlit as st
import pandas as pd
import plotly.express as pt

Menu = st.sidebar.selectbox("Menu",["Sales submission","Sales database"])
df=pd.read_csv("sales.csv")

if Menu == "Sales submission":
    ts = st.number_input("Sales of t-shirt")
    p = st.number_input("Sales of Pants")
    s = st.number_input("Sales of Shoes")
    b = st.number_input("Sales of bags")

    if st.button("Submit sales"):
        if ts and p and s and b:
            salesdict={"t-shirt":[ts],"pants":[p],"shoes":[s],"bags":[b]}
            salesdf= pd.DataFrame(salesdict)
            newsalesdf = pd.concat([df,salesdf],ignore_index=True)
            newsalesdf.to_csv("sales.csv")
            st.success("Sales sucsefully added")

        else:
            st.warning("Fill in all the boxes")

if Menu == "Sales database":

    sales =["t-shirt","pants","shoes","bags"]
    salestb = df[sales].mean().reset_index()
    rnametb = salestb.rename(columns={"index":"Item sold", 0 : "sales"})
    st.table(salestb)
    barchart = pt.bar(rnametb, x="index", y = 0)


