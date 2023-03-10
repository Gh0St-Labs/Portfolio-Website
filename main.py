import streamlit as st
import pandas as pd
import pathlib

# The syntax is mentioned below. Pandas can use list indexing / slicing, I don't know you name it.
# The [10:4] one.

st.set_page_config(layout='wide')



col1, col2 = st.columns(2) # this column method returns 2 columns as given

with col1:
    st.image("images\\IMG-1194.jpg", width=600) # this is the syntax to add the image instance.
with col2:
    st.title("Syon Duke Abraham")
    content = """
        Hi, I'am Syon Duke Abraham. Not a quite of an Intro but It'll do. I'am a Full Stack Web Developer, Data
        Scientist and a Full Stack Python Developer, and I've done more than 20 projects including a GPT Integrated 
        Chat Bot using OpenAI's API, Weather API, Multiple Conversion Projects and many more on the way! I'am also 
        the Founder and CEO of Shuttle, which is awaiting completion right now, but more on that later. This Web Interface has
        been made with Streamlit in Python, as you can acquaint with the overall Contrary. Please take no notice of my tight-lipped introduction. I'am 16 years old 
        as of this year! To know more about me and the Languages and Projects I've mastered and done, please befall 
        onto my LinkedIn. Hope you enjoy this Forum and I'll catch up with you! Peace!
        """
    st.info(content)

st.write("<h1><center> 🚀 Below you can find some of the apps that I have built in Python 🚀 </center></h1>", unsafe_allow_html=True)
st.write("<h2><center>  💬  Feel free to Contact Me  💬  </center></h2>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

# Always finish writing the content first then add the unsafe allow html to True and the Tags. It's a small bug.
# Leave space between the text and the HTML tags as without them, the HTML is useless.

col3, col4 = st.columns(2)

data_frame  = pd.read_csv("data.csv", sep=';')
with col3:
    for index, row in data_frame[0:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])

with col4:
    for index, row in data_frame[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])

