import streamlit as st
from  PIL import Image

st.set_page_config(page_title="home_page")

hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("welcome !!!")

ima = Image.open(r'media_16261cecfff79f6cdf1d37c733e8bd91d5c2bea74.png')
st.image(image=ima)