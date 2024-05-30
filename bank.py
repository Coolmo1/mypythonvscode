import streamlit as st

passw = st.sidebar.text_input("Password")

corpassw = "mybankpass"

if st.sidebar.button("Check Pasword"):
    if passw:
        if corpassw == passw:
            bank = st.number_input("Amount of money in your account")
            spent = st.number_input("AMount of money spent")
            if st.button("Submit"):
                mleft = bank - spent
                st.write(mleft)
                
                if mleft < 0:
                    st.warning("You have to budget more")

                elif mleft > 100:
                    st.success("Your budget is great")

                else:
                    st.warning("Your budget could be better")
        else:
            st.sidebar.error("Incorrect password")

    else:
        st.sidebar.warning("Please type in a password")