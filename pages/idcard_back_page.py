
from  PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from barcode import EAN13
from barcode.writer import ImageWriter
import random
import os
import streamlit as st


hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
# 523x280
st.header("ID Card Back Page")
DOB = st.date_input("Enter your DOB :")
blood_group = st.text_input("Enter your blood group :")
student = st.selectbox("Enter dayscalar or hostelar :",["dayscalar","hostelar"])
door_no = st.text_input("Enter the door number :")
street = st.text_input("Enter your street :")
near_location = st.text_input("Enter your nearby location :")
city = st.text_input("Enter your city :")
district = st.text_input("Enter your district :")
state = st.text_input("Enter your state :")
pincode = st.text_input("Enter your pincode :")
parent_number = st.text_input("Enter your parent's number :")
your_number =  st.text_input("Enter your number :")
condition_for_show_button = True
condition_for_download_button = True

generate_idcard = st.button("Generate idcard")

if generate_idcard:
    
    number_barcode = random.randint(100000000000,999999999999)
    barcode = EAN13(str(number_barcode),writer=ImageWriter())
    barcode.save("barcode_image")

    image = Image.open(r"id2.png").convert("RGBA")
    bar = Image.open("barcode_image.png").convert("RGBA")

    size_front = (650, 900)
    size_bar = (450, 130)
    main_image = image.resize(size_front)
    main_bar = bar.resize(size_bar)

    Image.Image.paste(main_image,main_bar,(60,680))

    sub_font = ImageFont.truetype(r"Poppins-Black.otf",35)
    myname_font = ImageFont.truetype(r"Poppins-Medium.otf",35)
    d1 = ImageDraw.Draw(main_image)
    d1.text((10,50),"DOB                                 :",font = sub_font,fill= (77,25,201),align="center")
    d1.text((330,50),str(DOB),font = myname_font,fill= (0,0,0),align="center")

    d1.text((10,110),"BLOOD  GROUP   :",font = sub_font,fill= (77,25,201),align="center")
    d1.text((330,110),blood_group,font = myname_font,fill= (0,0,0),align="center")

    d1.text((10,170),"STUDENT                   : ",font = sub_font,fill= (77,25,201),align="center")
    d1.text((330,170),student,font = myname_font,fill= (0,0,0),align="center")

    d1.text((10,230),"ADDRESS                   :",font = sub_font,fill= (77,25,201),align="center")
    d1.text((10,290)," ".join([door_no,street]),font = myname_font,fill= (0,0,0),align="center")
    d1.text((10,350)," ".join([near_location,city]),font = myname_font,fill= (0,0,0),align="center")
    d1.text((10,410)," ".join([district,state]),font = myname_font,fill= (0,0,0),align="center")
    d1.text((10,470),pincode,font = myname_font,fill= (0,0,0),align="center")

    d1.text((10,530),"PARENT'S NUMBER      : ",font = sub_font,fill= (77,25,201),align="center")
    d1.text((410,530),parent_number,font = myname_font,fill= (0,0,0),align="center")

    d1.text((10,590),"STUDENT'S NUMBER   :",font = sub_font,fill= (77,25,201),align="center")
    d1.text((410,590),your_number,font = myname_font,fill= (0,0,0),align="center")

    main_image.save("save_back_page_idcard.png")
    condition_for_show_button = False
    

st.subheader("Show ID card!!!")
view_id = st.button("Show id card",disabled=condition_for_show_button)
if view_id:
    image_show = Image.open('save_back_page_idcard.png')
    st.image(image_show)
    condition_for_download_button = False
    
st.subheader("Download your ID card!!!")
download_button = st.button("Click here",disabled=condition_for_download_button)
if download_button:
    with open('Save_created_idcard.png', 'rb') as file:
        st.download_button("Download ID card",file,file_name = 'save_back_page_idcard.png')
    st.success("best model is downloaded successfully !!!")
    st.snow()
    os.remove("save_back_page_idcard.png")