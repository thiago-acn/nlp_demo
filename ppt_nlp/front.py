import streamlit as st
from gtts import gTTS
from PIL import Image
from ppt_nlp.backend import load_ppt, summarization


banner = "./images/banner.png"
image = Image.open(banner)
st.image(banner, use_column_width=True)
# Set app title
st.title("PowerPoint Summarization")
st.subheader("From slide to text")
# Using "with" notation

# Create file uploader
uploaded_file = st.file_uploader("Choose a PowerPoint file", type="pptx")




if uploaded_file is not None:
    text = load_ppt(uploaded_file)
    summary = summarization(text)
    # Convert text to audio


    # Display the dataframe
    st.write(summary)


    tts = gTTS(summary, lang="en")
    tts.save("audio_analysis.mp3")
    audio_file = open("audio_analysis.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/ogg")

    
