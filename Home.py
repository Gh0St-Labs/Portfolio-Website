import streamlit as st
import pandas as pd

# If a folder named 'pages', just like this one, is created in a Project, and the python files inside which have
# streamlit loaded inside them will appear on the Browser with the Mother File (which should be outside the
# pages directory). It will appear as an Seperate page with the Mother file. This methodology can be used to add
# contact pages in our website.
# The syntax is mentioned below. Pandas can use list indexing / slicing, I don't know you name it.
# The [10:4] one.

st.set_page_config(layout='centered')


col1, col2 = st.columns(2) # this column method returns 2 columns as given

with col1:
    st.image("images\\IMG-1194.jpg", width=700) # this is the syntax to add the image instance.

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
st.write("<h2><center>  👉  Feel free to Contact Me  👈  </center></h2>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)
st.write("<br>", unsafe_allow_html=True)

# Always finish writing the content first then add the unsafe allow html to True and the Tags. It's a small bug.
# Leave space between the text and the HTML tags as without them, the HTML is useless.

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5]) # this is the ratio dimensions of the columns so you can have
# more space in between the columns

data_frame  = pd.read_csv("data.csv", sep=';')

with col3:
    for index, row in data_frame[0:10].iterrows():
        st.write(f"<center><h1> {row['title']} </h1></center>", unsafe_allow_html=True)
        st.image("images\\" + row['image'])
        st.write(f"<center><h4> {row['description']} </h4></center", unsafe_allow_html=True)
        st.write(f"<center><a href={row['url']}> Source Code </a></center>", unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
    st.write(f"<center><h1> IN PROGRESS! </h1></center>", unsafe_allow_html=True)

with col4:
    for index, row in data_frame[10:].iterrows():
        st.write(f"<center><h1> {row['title']} </h1></center>", unsafe_allow_html=True)
        st.image("images\\" + row['image'])
        st.write(f"<center><h4> {row['description']} </h4></center", unsafe_allow_html=True)
        st.write(f'<center><a href={row["url"]}> Source Code </a></center>', unsafe_allow_html=True)
        # there is also another method to give in links using st.write >>
        # st.write(f"[Source Code]({row['url]})")
        # the first square brackets is the name of the link, and the second curly brackets are for the link.
        # we are getting the link from row['url'] from the data.csv




