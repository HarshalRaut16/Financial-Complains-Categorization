import streamlit as st
import base64
from pre_process_data import main_fun


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )


add_bg_from_local('./static/9739.jpg')

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
             
txt_box = "Enter your complain it will be sent to related department"  
with st.form(key='output'):
    st.markdown("<h1 style='text-align: center; font-weight: 900; font-size: 55px;margin: 0 0 20px;'>Financial Complains <br> Classification</h1>", unsafe_allow_html=True)
    st.markdown("<p style='margin: 0; font-size: 20px;'>Submit Your Financial Complaints</p>", unsafe_allow_html=True)
    complaint = st.text_area(txt_box,height=250, placeholder="Type your complaint here...")
    submit_button = st.form_submit_button(label='Get Topic')

    if submit_button:
        data = str(complaint)
        output = main_fun(data)
        st.write("""Thank You for Reaching Us..!!
                 \nYour Complain is sent to """ + output +
                 " Department")
