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

if menu == 'Registration':

    st.title ("Register Here")
    row1,row2 = st.columns(2)
    with row1:
        #this ask the person for rthe personal information
        firstname = st.text_input("Enter in your firstname")#firstname
        email = st.text_input("Enter in your email")#email
        education = st.selectbox("Education level",["Masters","Bacherlors","OND","HND","None/Out of school"])#edeucation level
        dept = st.selectbox("Department",["Department","Manegment","Acounting Dept","Engineering Dept","HumanResources Dept","Security","Medical Dept","Transportation"]) #dropdown
        emdate = st.date_input('Enter the Employment date')

    with row2:
        lastname = st.text_input("Enter in your lastname")#lastname
        gender=st.radio("Gender",["Male","Female"],horizontal=True) #this a radio that means that zou dont have to type it Select toogle  gender
        salary = st.number_input("Enter in your monthly salary",value=1000, step = 100, format = "%d")
        job = st.selectbox("Job title",["Intern","Junior","Senior"])
        emp_status = st.selectbox("Employee Status",["Part time", "Full Time"])
    redate = st.date_input('Enter the Registration date')
    #this makes sure that theemployee has putin all the info requierd
    if st.button("Add Employee Data"):
        #Firstname,Lastname,Gender,Email,Education,Dept,Salary,Job,Employee,Registrationdate,Employmentdate, Employee ID
        if firstname and lastname and gender and email and education and salary and dept and job and emp_status and redate and emdate:
            employee_dict = {"Employee ID":[employee_id],"Firstname":[firstname],"Email" : [email],"Education":[education],"Department":[dept],
            "Registrationdate": [redate],"Employmentdate" : [emdate], "Lastname" : [lastname],"Gender" : [gender],"Salary" :[salary],"Job Title" : [job],"Employeestatus" : [emp_status]}
            employee_df= pd.DataFrame(employee_dict)
            newem_df= pd.concat([df,employee_df],ignore_index = True)
            newem_df.to_csv("employee_db.csv",index = False)
            st.success("You have been successfully added")

        else:
            st.error("You need to fill in the boxes")

corectpassword = "1q2w3e4r5t6y"
pass1,pass2 = st.sidebar.columns(2)
# this is for the search
if menu == 'Database':
    st.title('Employee Database')
    with pass1:
        password = st.sidebar.text_input("Enter in the correct password")
        login = st.sidebar.button("login")
    if login:
        if password:
            if password == corectpassword:
                st.dataframe(df,use_container_width=True)

            else:
                with pass1:
                    st.sidebar.error("The password that you typed is incorrect")
        else:
            with pass1:
                st.sidebar.error("Please type in a password")
 

if menu == 'Employee File':
    col1,col2,col3 = st.columns([2,2,1])
    with col3:
        employeesearch = st.text_input("Enter Employee",label_visibility='collapsed',placeholder='Enter Employee ID')
        search = st.button("Search Employee")
    if search:
        if employeesearch:
            search_result=df[df["Employee ID"]== employeesearch]
                        #the abov is a new df that has been filtered to show only the row in employee Id that contains the employee search
            gfname = search_result["Firstname"].iloc[0] #firstname and lastname and gender and email and education and salary and dept and salary and job and emp_status and redate and emdate
            gflname = search_result["Lastname"].iloc[0]
            gfemail = search_result["Email"].iloc[0]
            gfgender = search_result["Gender"].iloc[0]
            gfedu = search_result["Education"].iloc[0]
            gfdept = search_result["Department"].iloc[0]
            gfjob = search_result["Job Title"].iloc[0]
            gfempst = search_result["Employeestatus"].iloc[0]
            gfemdate = search_result["Employmentdate"].iloc[0]
            gfredate = search_result["Registrationdate"].iloc[0]
            gfsal = search_result["Salary"].iloc[0]

        else:
            st.write("Enter an Employee ID")

    if search:
        if employeesearch:
            gen1,gen2 = st.columns([0.8,4])

            with gen2:
                c1,c2,c3 = st.columns([2,2,1])
                coli1,coli2,coli3=st.columns([0.8,2,1])
                colw1,colw2,col3=st.columns([0.8,2,0.8])
                co1,co2,co3 = st.columns([1,2,3])
                colu1,colu2,colu3=st.columns([1,2,1])
                cou1,cou2,cou3 = st.columns([1,2,3])
                


                with coli2:
                    st.subheader("EMPLOYEE INFORMATON")
                
                with colw2:
                    st.subheader("Personal Infomation")
                with colu2:
                    st.subheader("Job information")
                with c1:
                    st.header(f':blue[{gfname} {gflname}]')    
                    st.write("")   
                with co1:
                    st.write("Email")
                    st.write("Gender")
                    st.write("Education")
                with cou1:   
                    st.write("Department")
                    st.write("Job Title")
                    st.write("Employment Date")
                    st.write("Registration Date")
                with co3:
                    st.write(gfemail)
                    st.write(gfgender)
                    st.write(gfedu)
                with cou3:     
                    st.write(gfdept)
                    st.write(gfjob)   
                    st.write(gfemdate)
                    st.write(gfredate)
