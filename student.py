"""
homework: Create a students score sheet to ask of their name and 5 subjects scores.
Then create a csv file with a df to display each student scores and cummulative and average on
seperate separate columns for each student
"""

import streamlit as st
import pandas as pd #This is used to read, write tables , df

st.title("Stundent data")

"""
Here you can see the grades of past students.

To Register i would need 
Your...

Personal Data: Name, Age, class

Scores: science, english ,math, history, biology grades
"""

df = pd.read_csv("student.csv")
st.dataframe(df)

name = st.text_input("Enter in your name")
age = st.number_input("Enter in your Age",0,150,value=0,step=1,format= "%d")
clazz = st.text_input("Enter which class you are in")

science = st.number_input("Enter in your science grade ",0,100)
english = st.number_input("Enter in your english grade ",0,100)
math = st.number_input("Enter in your maths grade ",0,100)
history = st.number_input("Enter in your history grade ",0,100)
biology = st.number_input("Enter in your biology grade ",0,100)
total = math +english +history+biology +science
average = total / 5

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

if average <= 50 :
    grades = "F"








if st.button("Add student data"):
    if name and clazz and age and science and english and math and history and biology: 
        employee_dict = {"Name":[name], "Age":[age], "Class" :[clazz], "Science" :[science], "English" : [english],
         "Math":[math], "History":[history], "Biology":[biology],"Total" : [total],"Average" : [average],"Grades" : [grades] }
        employee_df = pd.DataFrame(employee_dict)
        new_df = pd.concat([df,employee_df],ignore_index=True)
        new_df.to_csv('student.csv',index=False)
        st.success("Student data successfully added")
        
    else: 
        st.warning("You need to fill all the boxes")


