import streamlit as st
from fpdf import FPDF
import base64



menu = st.sidebar.selectbox("Menu",["Invoice Generator","Change Details "])

imageurl = "logo.png"
if menu == "Invoice Generator":

    taxbar = st.sidebar.number_input("**Enter Tax %**")
    discount = st.sidebar.number_input("**Enter discount %**")

    st.sidebar.write("**OPTIONAL**")
    img1,img2,img3 = st.columns([2,1,1])

    with img1:
        st.image(imageurl,width=150)
        st.write(":violet[The Laptop Company]")
        st.write(":violet[1141 Sunny Glen Lane]")
        st.write(":violet[Ohio,USA]")

    with img3:
        st.header(":violet[INVOICE]")

    st.write("")
     
    bill1,bill2,bill3 = st.columns([2,1,1])
    with bill1:
        cname = st.text_input(":violet[**Bill to**]",placeholder="Customer Name")
        cemail = st.text_input("email",label_visibility="collapsed",placeholder="Enter email-adress")
    
    with bill2:
        st.write("")
        st.write(":violet[**Invoice#**]")
        st.write("")
        st.write(":violet[**Invoicedate:**]")
        st.write("")
        st.write(":violet[**Due date:**]")

    with bill3:
        invnumber = st.text_input("INv",label_visibility="collapsed",placeholder="Invoice number")
        invdate = st.date_input("invd",label_visibility="collapsed")
        dudate = st.date_input("dued",label_visibility="collapsed")

    des1,des2,des3,des4 = st.columns(4)
    with des1:
        desc = st.text_input(":violet[**Description**]")

    with des2:
        quantitty= st.number_input(":violet[**Quantity**]")
    
    with des3:
        price = st.number_input(":violet[**Price/Unit**]")
        tprice = quantitty * price
        taxcalc = taxbar/100 * tprice
        st.write(f":violet[**Tax: ${taxcalc}**]")

    with des4:
        tpricebar = st.text_input(":violet[**Total price**]",placeholder=f"${tprice}")
        discalc = discount/100 * tprice
        discount = st.write(f":violet[**Discount: ${discalc}**]")

    st.divider()
    fcalc = tprice - discalc + taxcalc

    pay1,pay2 = st.columns(2)
    
    with pay1:
        st.write(":violet[**Payment Info**]")
        st.write(":violet[Acc Name: The Laptop company]")
        st.write(":violet[Acc Number: 0989072307743]")
        st.write(":violet[Bank Name: American Bank]")

    with pay2:
        st.write(":VIOLET[**Payment Due:**]")
        st.header(f":green[**${fcalc:,}**]")

    def generatepdf():
        pdf = FPDF()

        pdf.add_page()

        pdf.set_font("Arial", size = 10)

        col1x = 20
        col1y = 20

        colw = 90
        colh = 10

        pdf.image(imageurl, x=col1x, y=col1y, w=30)

        pdf.set_font("Courier", size=12)

        #Invoice
        pdf.set_font("Courier", size=25,style = "B")
        pdf.set_xy(col1x + 100,col1y +11)
        pdf.cell(colw,colh,txt="INVOICE",ln=True, align="L")

        #The Laptop Company
        pdf.set_font("Courier", size=15, style="B")
        pdf.set_xy(col1x,col1y+40)
        pdf.cell(colw,colh,txt = "The Laptop Company",ln = True, align="L")

        #Street Adress
        pdf.set_font("Courier", size=15)
        pdf.set_xy(col1x,col1y+49)
        pdf.cell(colw,colh,txt = "1141 Sunnz Glen Lane",ln = True, align="L")

        #Ohio,USA
        pdf.set_font("Courier", size=15)
        pdf.set_xy(col1x,col1y+58)
        pdf.cell(colw,colh,txt = "Ohio,USA",ln = True, align="L")

        #Bill to
        pdf.set_font("Courier", size=15, style="B")
        pdf.set_xy(col1x,col1y+85)
        pdf.cell(colw,colh,txt = "Bill To",ln = True, align="L")

        #Customername
        pdf.set_font("Courier", size=15, style="B")
        pdf.set_xy(col1x,col1y+95)
        pdf.cell(colw,colh,txt = f"{cname}",ln = True, align="L")

        #Customeremail
        pdf.set_font("Courier", size=15, style="B")
        pdf.set_xy(col1x,col1y+105)
        pdf.cell(colw,colh,txt = f"{cemail}",ln = True, align="L")

        #Invoicenumber1
        pdf.set_font("Courier", size=15, style="B")
        pdf.set_xy(col1x+100,col1y+95)
        pdf.cell(colw,colh,txt = f"Invoice#:",ln = True, align="L")

        #Invoicenum2
        pdf.set_font("Courier", size=15, style="B")
        pdf.set_xy(col1x+130,col1y+95)
        pdf.cell(colw,colh,txt = f"{invnumber}",ln = True, align="L")

        #Invoicedate1
        pdf.set_font("Courier", size=15, style="B")
        pdf.set_xy(col1x+100,col1y+105)
        pdf.cell(colw,colh,txt = f"Invoice Date:",ln = True, align="L")

        #Invoicedate2
        pdf.set_font("Courier", size=15, style="B")
        pdf.set_xy(col1x+142,col1y+105)
        pdf.cell(colw,colh,txt = f"{invdate}",ln = True, align="L")

        #Decription
        pdf.set_font("Courier", size=15, style="B")
        pdf.set_xy(col1x,col1y+130)
        pdf.cell(colw,colh,txt ="Description",ln = True, align="L")

        #Qunatitiy
        pdf.set_font("Courier", size=15, style="B")
        pdf.set_xy(col1x+80,col1y+130)
        pdf.cell(colw,colh,txt ="Quantity",ln = True, align="L")

        #Price/Unit
        pdf.set_font("Courier", size=15, style="B")
        pdf.set_xy(col1x+110,col1y+130)
        pdf.cell(colw,colh,txt ="Price/Unit",ln = True, align="L")

        #total price
        pdf.set_font("Courier", size=15, style="B")
        pdf.set_xy(col1x+150,col1y+130)
        pdf.cell(colw,colh,txt ="Total price",ln = True, align="L")

        pdf_file = "The Laptop Company Invoice"
        pdf.output(pdf_file)
        return pdf_file

    pdf_func = generatepdf()

    with open(pdf_func,"rb") as binary:
        pdf_data = binary.read()

    if st.button(":violet[View Invoice]"):
        write_pdf = base64.b64encode(pdf_data).decode("utf-8")

        embed_pdf = f'<embed src="data:application/pdf;base64,{write_pdf}" type="application/pdf" width="70%" height="600px" />'

        st.markdown(embed_pdf,unsafe_allow_html = True)


