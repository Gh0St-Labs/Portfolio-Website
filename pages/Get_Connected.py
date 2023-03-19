import streamlit as st
import random as rd
from send_email import send_email

messages = ['Coffee on me?',"Lunch on me?", "We've never met, but...",'Reaching out regarding Project ABC.',
            'Long time fan, first time emailer!','Hello from a fellow blogger','Wanna grab Pizza?']
random_messages = rd.choice(messages)

st.write(" <center><header><h1> Contact Me </h1></header></center> ", unsafe_allow_html=True)

with st.form(key='contact_form'):
    user_email = st.text_input(label="Your E-Mail Address",placeholder="abcde@example.com")
    raw_user_message = st.text_area(label="Your Message")
    # DO NOT GIVE PLACEHOLDERS IN THE MESSAGING SECTION OF THE EMAIL FORM.
    # The subject which is being used below is an inbuilt instance which changes the subject of the E-Mail.
    # Everything below that is just the Message
    user_message = f"""\
Subject: New E-Mail from {user_email}

From: {user_email}

Message: {raw_user_message}

"""

    submit_button = st.form_submit_button(label="Submit")
    if submit_button:
        send_email(user_message)
        st.info("Your E-Mail was Successfully Sent!")
        
