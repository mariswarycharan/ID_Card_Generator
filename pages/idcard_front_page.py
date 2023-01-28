
from  PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
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

# receiving input from user

st.header("ID Card Front Page")
myphoto = st.file_uploader("Upload your photo")
college_logo = st.file_uploader("Upload your college logo")
college_name1 = st.text_input("Enter your college name (enter main tittle only ) :")
college_name2 = st.text_input("Enter your college name (enter remaining name only ) :")
your_name = st.text_input("Enter your name :")
roll_no = st.text_input("Enter your roll no :")
year = st.text_input("Enter which year you are studying :")
degree = st.text_input("Enter your degree :")
course = st.text_input("Enter your branch :")

condition_for_show_button = True
condition_for_download_button = True


generate_idcard = st.button("Generate idcard")

if generate_idcard:
    # open the image

    front = Image.open(r"4958577397a4539.png").convert("RGBA")
    P1 = Image.open(myphoto).convert("RGBA")
    l1 = Image.open(college_logo).convert("RGBA")

    # giving size for image

    size_front = (650, 900)
    size_photo = (270,300)
    size_logo = (110,110)

    # resize the image

    photo = P1.resize(size_photo)
    logo = l1.resize(size_logo)
    front = front.resize(size_front)

    Image.Image.paste(front,photo,(180,270))

    title_font = ImageFont.truetype(r"Poppins-Black.otf",55)

    d1 = ImageDraw.Draw(front)

    d1.text((170,10),college_name1,font = title_font,fill= (255,255,0))


    title_sub = ImageFont.truetype(r"Poppins-Regular.otf",30)

    d1.text((200,70),college_name2,font = title_sub ,fill= (0,0,0))

    sub_font = ImageFont.truetype(r"Poppins-Black.otf",35)
    myname_font = ImageFont.truetype(r"Poppins-Medium.otf",35)

    d1.text((10,600),"NAME        :",font = sub_font,fill= (77,25,201),align="center")
    d1.text((200,600),your_name,font = myname_font,fill= (0,0,0),align="center")

    d1.text((10,660),"ROLL NO :",font = sub_font,fill= (77,25,201),align="center")
    d1.text((200,660),roll_no,font = myname_font,fill= (0,0,0),align="center")

    d1.text((10,720),"YEAR          :",font = sub_font,fill= (77,25,201),align="center")
    d1.text((200,720),year,font = myname_font,fill= (0,0,0),align="center")

    d1.text((10,780),"DEGREE/BRANCH :",font = sub_font,fill= (77,25,201),align="center")


    course_font = ImageFont.truetype(r"Poppins-Medium.otf",28)
    d1.text((10,840),degree,font = course_font,fill= (0,0,0),align="center")
    d1.text((93,840),"/",font = course_font,fill= (0,0,0),align="center")
    d1.text((103,840),course,font = course_font ,fill= (0,0,0),align="center")

    Image.Image.paste(front,logo,(20,20))
    front.save("Save_created_idcard.png")
    condition_for_show_button = False
    
    
st.subheader("Show ID card!!!")
view_id = st.button("Show id card",disabled=condition_for_show_button)
if view_id:
    image_show = Image.open('Save_created_idcard.png')
    st.image(image_show)
    condition_for_download_button = False
    
st.subheader("Download your ID card!!!")
download_button = st.button("Click here",disabled=condition_for_download_button)
if download_button:
    with open('Save_created_idcard.png', 'rb') as file:
        st.download_button("Download ID card",file,file_name = 'Save_created_idcard.png')
    st.success("best model is downloaded successfully !!!")
    st.snow()
    os.remove("Save_created_idcard.png")
    