# Create an employee database, that shows the name of employee, date of employment (use st.date),
#salary, gender, position/role, education level, contract status (full/part)



import streamlit as st
import pandas as pd

#this is to set the page to full screen
st.set_page_config(layout='wide')
menu = st.sidebar.selectbox('Menu',['Registration','Employee File','Database']) #menu bar

#this is to read the csv file
df = pd.read_csv("employee_db.csv")

#this is to give every the user a user id by the number of rows in the df
employee_id = 'USER' + str(len(df) +1)

#this function adds the information to the csv file
def new_employee(employee_id,firstname,lastname,email,education,dept,date,gender,salary,job,emp_status,df):
    #this is used to create a dict, which creates the column name as the key and assigns it to the corresponding variable name
    employee_dict = {"Employee ID":employee_id,"Firstname":firstname,"Email" : email,"Education":education,"Dept":dept,"Registrationdate": date,"Lastname" : lastname,"Gender" : gender,"Salary" :salary,"Job" : job,"Employee" : emp_status}
    employee_df = pd.DataFrame([employee_dict]) #this converts the dict into a dataframe
    df = pd.concat([df,employee_df],ignore_index = True)# this appends the new df to the old df
    return df


if menu == 'Registration':


    st.title ("Register Here")
    row1,row2 = st.columns(2)
    with row1:
        #this ask the person for rthe personal information
        firstname = st.text_input("Enter in your firstname")#firstname
        email = st.text_input("Enter in your email")#email
        education = st.selectbox("Education level",["Masters","Bacherlors","OND","HND"])#edeucation level
        dept = st.selectbox("Department",["Department","Manegment","Acounting Dept","Engineering Dept","HumanResources Dept","Security","Medical Dept","Transportation"]) #dropdown
        date = st.date_input('Enter the Employment date')


    with row2:
        lastname = st.text_input("Enter in your lastname")#lastname
        gender=st.radio("Gender",["Male","Female"],horizontal=True) #this a radio that means that zou dont have to type it Select toogle  gender
        salary = st.number_input("Enter in your monthly salary",value=1000, step = 100, format = "%d")
        job = st.selectbox("Job title",["Intern","Junior","Senior"])
        emp_status = st.selectbox("Employee Status",["Part time", "Full Time"])
    date = st.date_input('Enter the Registration date')
    #this makes sure that theemployee has putin all the info requierd
    if st.button("Add Employee Data"):
        if firstname and email and education and dept and date and lastname and gender and salary and job and emp_status:
            df = new_employee(employee_id,firstname,email,education,dept,date,lastname,gender,salary,job,emp_status,df)
            df.to_csv("employee_db.csv",index = False)
            st.success("You have been successfully added")


        else:
            st.error("You need to fill in the boxes")


# this is for the search
if menu == 'Database':
    st.title('Employee Database')


    st.dataframe(df,use_container_width=True)
 

if menu == 'Employee File':
    col1,col2,col3 = st.columns([2,2,1])
    with col3:
        employeesearch = st.text_input("Enter Employee",label_visibility='collapsed',placeholder='Enter Employee ID')
        search = st.button("Search Employee")
    if search:
        if employeesearch:
            search_result=df[df["Employee ID"]== employeesearch]
                        #the abov is a new df that has been filtered to show onlz te row in employee Id that contains the employee search
            st.data_editor(search_result)
            gfname = search_result["Firstname"].iloc[0]
            

        else:
            st.write("Enter an Employee ID")

    if search:
        if employeesearch:
            coli1,coli2,coli3=st.columns([1,2,1])
            co1,co2,co3 = st.columns([1,2,3])

            with coli2:
                st.header("Info about this person")
            with co1:
            
                st.write("Name")
            with co3:
                st.write(gfname)







