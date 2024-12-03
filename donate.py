import streamlit as st
import pandas as pd

st.set_page_config(layout="wide",page_title="Donate to a cause",page_icon="💰💵❤️")

menu = st.sidebar.selectbox("Select Option",["Create Donation", "View Donation", "Make a Donation"])

donate = pd.read_csv("donate.csv")
donateadd = pd.read_csv("donate add.csv")


if menu == "Create Donation":
    c1,c2,c3 = st.columns([0.2,4,0.2])
    with c2:
        st.header("Create Donation")
        co1,co2 = st.columns(2)
        with co1:
            dotitle = st.text_input("Campaign title")
        col1,col2 = st.columns(2)
        
        with co2:
            email = st.text_input("Email")
        st.divider()
        desc = st.text_area("Campagn details", height=200)
        coln1,coln2 = st.columns(2)
        with coln1:
            goala = st.selectbox(
                "Goal amount",
                ("$50","$100","$200","$300","Custom amount"))
            if goala == "$50":
                goala = 50
            if goala == "$100":
                goala = 100
            if goala == "$200":
                goala = 200
            if goala == "$300":
                goala = 300
            if goala == "Custom amount":
                goala = st.number_input("Enter a custom amount")
        if st.button("Create Donation"):
            if dotitle and email and desc:
                dndict = {"Title":[dotitle],"E-mail":[email],"Campagn Details":[desc],"Goal Amount":[goala]}
                dn_df = pd.DataFrame(dndict)
                dnjoin = pd.concat([donate,dn_df], ignore_index=True)
                dnjoin.to_csv("donate.csv",index=False)
                st.success("Created")
            else:
                st.error("FIll in all the boxes")

if menu == "View Donation":
    st.subheader(":orange[View Donation]")
    st.divider()
    donatetitle = donate["Title"]
    col1,col2 = st.columns(2)
    with col1:
        chtitle = st.selectbox("Select Donation to view",donatetitle)


    ftitle = donate[donate["Title"]==chtitle]
    

    getti = ftitle["Title"].iloc[0]
    gete = ftitle["E-mail"].iloc[0]
    getd = ftitle["Campagn Details"].iloc[0]
    getg = ftitle["Goal Amount"].iloc[0]
    


    st.divider()
    col3,col4,col5 = st.columns(3)
    with col3:
        st.subheader(":orange[Campaign details]")    
    with col4:
        st.subheader(f":black[Goal amount:] :green[${getg:,}]")
    with col5:
        try:
            sumleft = donateadd[chtitle].sum()
            sumremainder = getg - sumleft
            if sumremainder < 0:
                st.subheader(f":black[Total Left:] :green[Goal reached]")
            else:
                st.subheader(f":black[Total Left:] :red[${sumremainder:,}]")
        except KeyError:
            st.error("Sorry no donation yet")
        

    st.divider()

    st.write(getd)

    st.write(gete)

if menu == "Make a Donation":
    st.subheader("Make a donation")
    col5,col6 = st.columns(2)
    donatetitle2 = donate["Title"]

    with col5:
        choose_title = st.selectbox("Select a donation you would like to donate to", donatetitle2)
    with col6:
        doamount = st.number_input("Enter in the you would like to donate")
    
    st.divider()

    if st.button("Donate"):
        if choose_title and doamount:
            donatedict = {f"{choose_title}":[doamount]}   
            dotable = pd.DataFrame(donatedict)
           # st.table(dotable)
            donatejoin = pd.concat([donateadd, dotable],ignore_index=False)
            donatejoin.to_csv("donate add.csv",)
            st.success("Thank you for donating")

        else:
            st.error("Please fill in all the boxes")
