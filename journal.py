import streamlit as st
import pandas as pd

menu = st.sidebar.selectbox("Select Option",["Create Note","View Note","Update Note"])

rj = pd.read_csv("journal.csv")

if menu == "Create Note":
    head1,hed2,hed3 = st.columns(3)
    with hed2:
        st.header(":blue[create Notes]")
    t1,t2,= st.columns(2)
    with t1:
        title = st.text_input("Enter the title for a new Notes")
    with t2:
        date = st.date_input("Select date")

    c = st.text_area("Make you notes",height=250)

    if st.button("Save button"):
        if title and c:
            notedict={"Title":[title],"Date":[date],"Content":[c]}
            notesdf = pd.DataFrame(notedict)
            newnotesdf = pd.concat([rj,notesdf],ignore_index=True)
            newnotesdf.to_csv("journal.csv",index = False)
            st.success("saved")

if menu == "View Note":
    hed1,hed2,hed3 = st.columns(3)
    with hed2:
        st.header(":blue[View Notes]")

    rt = rj["Title"].to_list()

    s_t = st.selectbox("Selct Note",rt)

    ft = rj[rj["Title"] == s_t]

    fc = ft["Content"].iloc[0]
    fd = ft["Date"].iloc[0]

    d1,d2 = st.columns(2)

    with d1:
        st.subheader(":blue[Selected note content]")
    with d2:
        st.subheader(fd)

    st.divider()

    st.write(fc)

