import streamlit as st
import pandas as pd
import numpy as np

st.header("Welcome to StreamLit", anchor=False)
st.title("Hello, Streamlit")
st.write("Welcome to your first Streamlit app.")

name = st.text_input("Enter your name:")
checkbox = st.checkbox("Show greetings")
radio = st.radio("Choose a greeting style:", ("Formal", "Casual"))
date = st.date_input("Selet a date")
color = st.color_picker("Pick a color:" "#49754A")
image = st.file_uploader("Upload an Image:", type=["png", "jpg", "jpeg"])
select = st.select_slider("select", ("Formal", "Casual", "Native"))
audio = st.audio("/Users/HI/Downloads/dramatic-background-music-for-short-videos-1-minute-little-alicia-155718.mp3")
video = st.video("https://www.youtube.com/watch?v=tollGa3S0o8")

image = st.image("/Users/HI/Downloads//zebra.jfif", "image")

st.sidebar.title("Sidebar")
name = st.sidebar.text_input("Enter Your name")
st.sidebar.write(f"My name is {name}!")





# st.write(f"Hello, {name}!")

# st.write(pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# }))

# dataframe = np.random.randn(10, 20)
# st.dataframe(dataframe)


# dataframe = pd.DataFrame(
#     np.random.randn(10, 20),
#     columns=('col %d' % i for i in range(20)))

# st.dataframe(dataframe.style.highlight_max(axis=0))

# first, second = st.columns(2)

# with first:
#     name = st.text_area("Name")
#     st.write(name)

# with second:
#     audio = st.audio_input("audio")
#     chat = st.chat_input("Enter your chat")

#     if chat:
#         st.write(chat)

