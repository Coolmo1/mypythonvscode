import streamlit as st

st.title("Find out your BMI(Body Mass Index)")

Menu = st.sidebar.selectbox("Menu",["Metric Units","US Units"])

if Menu == "Metric Units":
        st.header("Calculate in metric Units")
        mheigth = st.number_input("Enter in your height in metres")
        kgweight = st.number_input("Enter in your weight in kilogramms")
        if st.button("Caclutate"):
            BMI_kgm = kgweight/mheigth**2
            st.write(BMI_kgm)
            if BMI_kgm <18.5:
                st.error("You are underweight")
            if BMI_kgm >= 18.5 and BMI_kgm < 25:
                st.success("You are a healthy weight")
            if BMI_kgm >= 25 and BMI_kgm <30:
                st.warning("You are overweight")
            if BMI_kgm >= 30:
                st.error("You are obeses")

if Menu == "US Units":
    st.header("Calculate in US Units")
    fheight = st.number_input("Enter in your height in inches")
    lbsweight = st. number_input("Enter in your weight in pounds")
    if st.button("Caclutate"):
        BMI_lbs = lbsweight*703
        BMI_lbsf = BMI_lbs/fheight**2
        st.write(BMI_lbsf)
        if BMI_lbsf <18.5:
            st.error("You are underweight")
        if BMI_lbsf >= 18.5 and BMI_lbsf < 25:
            st.success("You are a healthy weight")
        if BMI_lbsf >= 25 and BMI_lbsf <30:
            st.warning("You are over weight")
        if BMI_lbsf >= 30:
            st.error("You are obeses")    




