import streamlit as st
import pandas as pd

st.set_page_config(layout= "centered")

col1, col2 = st.columns(2)

with col1:
    st.image("images/my_photo_2.png", width=350)

with col2:
    st.title("Nicken Shidqia Nurahman")
    content = """
    Hi, I am Nicken ! I am a civil engineer graduate with some experience in administration and project management, who is interested in Data Science. 
    Detail oriented, and time management person, and familiar with Microsoft Office, Python, SQL and Jupyter. 
    Motivated to continue to learn and grow as a professional.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me :)
"""
st.write(f"[Contact Me](https://www.linkedin.com/in/nickenshidqia/)")

st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3 :
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4 :
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")