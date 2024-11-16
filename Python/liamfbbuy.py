import streamlit as st

st.title("Match Day")

menu = st.sidebar.selectbox("Menu", ["Matches", "Account Login"])

money_spent = 0

if menu == "Matches":
    st.header("Current Match")
    matches = st.radio("Choose the Football match you want to watch",["Manchester city - liverpool", 
                                                                    "Manchester United - Aston Villa",
                                                                    "Chelsea -  Leicester City", 
                                                                    "Nottingham Forest - Newcastle United"])

    if st.button("Purchase"):
        money_spent =+ 100

if menu == "Account Login":
    pasword = "Hello"
    username = st.sidebar.text_input("Username")
    tpasword = st.sidebar.text_input("Password")
    if username and tpasword:
        if pasword == tpasword:
            st.sidebar.success("You have typed the correct Pasword")
            st.title("Other Purchases")
            st.header("Season Pass")
            seasonp = st.radio("Season Pass",["Standard Pass: 200", "VIP Pass: 500"])
            st.header("Team Merchandise")
            merch = st.radio("Merch",["Jersey: 10","Scarf: 30","Hat: 20"])
            st.header("Snacks Purchase")
            snacks = st.radio("Snacks",["Popcorn: 10","Hot dog: 15","Soda: 5"])
            st.header("Premium Sports Chanel Subscription")
            sportch = st.radio("Sports Channel Membership",["Monthly subcription: 20","Annual subcription: 200"])
            if st.button("Purchase") and seasonp and merch and snacks and sportch:
                if seasonp == "Standard Pass: 200":
                    money_spent =+ 200
                if seasonp == "VIP Pass: 500":
                    money_spent =+ 500
                if merch == "Jersey: 10":
                    money_spent =+ 10
                if merch == "Scarf: 30":
                    money_spent =+ 30
                if merch == "Hat: 20":
                    money_spent =+ 20
                if snacks == "Popcorn: 10":
                    money_spent =+ 10
                if snacks == "Hot dog: 15":
                    money_spent =+ 15
                if snacks == "Soda: 5":
                    money_spent =+ 5
                if sportch == "Monthly subcription: 20":
                    money_spent += 20
                if sportch == "Annual subcription: 200":
                    money_spent =+ 200
                st.write(money_spent)

            else:
                st.warning("Please fill in all the boxes")
                


        elif tpasword != pasword:
            st.error("You have typed the wrong password")
        else:
            st.warning("Please write type a password")



