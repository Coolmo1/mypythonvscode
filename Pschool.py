import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
Menu =st.sidebar.selectbox("Menu", ["Application", "Data"])
countries = pd.read_csv("countries.csv")
df= pd.read_csv("Pschool.csv")

if Menu == "Application":
    
    st.write("**Name**")
    name1,name2,name3 = st.columns(3)
    num,email = st.columns(2)
    s1,s2 = st.columns(2)
    st.write("**Parents/Legal Guardian**")
    pname1,pname2,pname3 = st.columns(3)
    pnum,pemail = st.columns(2)
    st.write("**Adress**")
    cp,sr = st.columns(2)
    
    with name1:
        fname = st.text_input("Firstname" ,label_visibility= "collapsed", placeholder="Firstname" )

    with name2:
        mname = st.text_input("Middlename" ,label_visibility= "collapsed", placeholder="Middlename" )


    with name3: 
        lname = st.text_input("Lastname" ,label_visibility= "collapsed", placeholder="Lastname" )  


    with pname1:
        fnamep = st.text_input("Firstnamep" ,label_visibility= "collapsed", placeholder="Firstname" )

    with pname2:
       mnamep = st.text_input("Middlenamep" ,label_visibility= "collapsed", placeholder="Middlename" )

    with pname3: 
        lnamep = st.text_input("Lastnamep" ,label_visibility= "collapsed", placeholder="Lastname" ) 

    with num:
        num = st.number_input("Age", value=0, max_value=13)

    with email:
        st.write(" ")
        st.write("")
        email= st.text_input("email", label_visibility= "collapsed", placeholder="Childs Email")

    with pnum:
        pnum=st.text_input( label= "Phone number",placeholder = "### ### ## ##")

    with pemail:
        st.write(" ")
        st.write(" ")
        pemail =st.text_input("pemail", label_visibility= "collapsed", placeholder="Parent/Legal Guardian Email")

    with s1:
        school=st.radio("School", ["Public","Private"] ,horizontal= True)

    with s2:
        nschool = st.text_input("Name of old School")
    
    with cp:
        country = st.selectbox("Select a country",countries["Country"].tolist())
        pcode = st.text_input(label="Postalcode", placeholder="####")

    with sr:
        st.write("")
        st.write("")
        state = st.text_input("State",label_visibility= "collapsed", placeholder="State")
        st.write("")
        st.write("")
        region = st.text_input("Region",label_visibility= "collapsed", placeholder="Region")

    street = st.text_input("street", label_visibility="collapsed",placeholder="Street Name")
    if st.button("Apply"):
        if fname and mname and lname and lnamep and fname and mnamep and email and pemail and pnum and school and country and pcode and state and region:
            studict = {"Child Firstname" : [fname],"Child Middlename" : [mname], "Child Lastname":[lname], "Parents/Legal Guadian Firstname": [fnamep],
                       "Parents/Legal Guadian Middlename" : [mnamep], "Parents/Legal Guadian Lastname" : [lnamep],"Childs email":[email],
                       "Parents/Legal Guadian email" :[pemail], "Parents/Legal Guardian number" : [pnum], "Name of old School" : [school],
                     "Country" :[country], "Postalcode" : [pcode], "State" : [state], "Region" : [region]}
            st.write(studict)
            stud_df = pd.DataFrame(studict)
            st.table(stud_df)
            newstud_df = pd.concat([df,stud_df],ignore_index =True)
            st.success("You have been successfully")

if Menu == "Data":
    st.dataframe(df)