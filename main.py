import streamlit as st

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
        the Founder and CEO of Shuttle, which is in progress right now, but more on that later. This Web Interface has
        been made with Streamlit in Python. Please take no notice of my tight-lipped introduction. I'am 16 years old 
        as of this year! To know more about me and the Languages and Projects I've mastered and done, please befall 
        onto my LinkedIn. Hope you enjoy this Forum and I'll catch up with you! Peace!

        """
    st.info(content)
