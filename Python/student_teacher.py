import streamlit as st
import pandas as pd #this lets you read, display dataframes
#Name,Clazz,score
st.title("Student's Databas App")


#This function helps us to get student's data
def new_student(name,clazz,score,df): #func to process each student data
    student_dict = {"Name":name, "Class":clazz, "Score": score} #create a dict for each student data
    student_df = pd.DataFrame([student_dict]) #convert the dict to a df
    df = pd.concat([df,student_df], ignore_index = True) #append new df above to the exisiting df (df)
    #ignore means if dupplicate data then overwrite existing one
    return df




#Load the employee CSV file as a dataframe
df = pd.read_csv("studentsmoyo.csv") #exisiting df
st.dataframe(df) # display df on streamlit


name = st.text_input("Enter your name: ")
clazz = st.text_input("Enter your class: ")
score = st.number_input("Enter your score: ")


if st.button("Add student data"):
    if name and clazz and score: #check if all boxes are filled
        df = new_student(name,clazz,score,df)
        df.to_csv("studentsmoyo.csv", index= False)
        st.success("Student data successfully added")
        st.session_state.name = "" #reset variable and widget to empty
        st.session_state.clazz = "" #reset variable and widget to empty
        st.session_state.score = 0 #reset variable and widget to empty
   
    else: #if all or any box(es) have not been filled
        st.warning("You need to fill all the boxes")




#simple homework: download a csv file from the internet and read, display it with python streamlit
