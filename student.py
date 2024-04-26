

import streamlit as st
import pandas as pd #This is used to read, write tables , df
import plotly.express as px

st.set_page_config(layout='wide')
df = pd.read_csv("student.csv")                                                                                                        

Menu = st.sidebar.selectbox("Menu",["Grade submission","Score charts","Student grade Database"])
if Menu == "Grade submission":
        
    st.title("Stundent data")

    name = st.text_input("Enter in students name")
    col1,col2 = st.columns(2)
   
    with col1:
        science = st.number_input("Enter in students science grade ",0,100)
        biology = st.number_input("Enter in students biology grade ",0,100)
        math = st.number_input("Enter in students maths grade ",0,100)
    with col2:
        history = st.number_input("Enter in students history grade ",0,100)
        english = st.number_input("Enter in students english grade ",0,100)
        st.write("")
        st.write("")
        submit =   st.button("Submit Student Data")

    total = math +english +history+biology +science
    average = total / 5

    if submit:
        if average <= 100 and average >= 90:
            if average == 95:
                grades = "A"
            elif average > 95:
                grades = "A+"
            elif average < 95:
                grades="A-"

        if average <= 89 and average >= 80:
            if average == 85:
                grades = "B"
            elif average > 85:
                grades = "B+"
            elif average < 85:
                grades="B-"

        if average <= 79 and average >= 70:
            if average == 75:
                grades = "C"
            elif average > 75:
                grades = "C+"
            elif average < 75:
                grades="C-"

        if average <= 69 and average >= 60:
            if average == 65:
                grades = "D"
            elif average > 65:
                grades = "D+"
            elif average < 65:
                grades="D-"

        if average <= 59 and average >= 50:
            if average == 55:
                grades = "E"
            elif average > 55:
                grades = "E-"
            elif average < 55:
                grades ="E+"

        if average <= 50 :
            grades = "F"
        st.write(average)
        if name and science and english and math and history and biology: 
            students_dict = {"Name":[name],"Science" :[science], "English" : [english],
            "Math":[math], "History":[history], "Biology":[biology],"Total" : [total],"Average" : [average],"Grades" : [grades]}
            students_df = pd.DataFrame(students_dict)
            new_df = pd.concat([df,students_df],ignore_index=True)
            new_df.to_csv('student.csv',index=False)
            st.success("Student data successfully added")
            
        else: 
            st.warning("You need to fill all the boxes")

    

if Menu == "Student grade Database":
    
    st.table(df)

if Menu == "Score charts":
    subjects =["Science","English","Math","History","Biology"]
    subjectstb = df[subjects].mean().reset_index()
    rnametb = subjectstb.rename(columns={"index":"Subjects", 0 : "score"})
    st.table(subjectstb)
    barchart = px.bar(rnametb,x= "index", y = 0)

    st.plotly_chart(barchart)
#csv sales bracharts
#max 10

    



