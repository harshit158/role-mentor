import streamlit as st
import utils

st.set_page_config(layout="wide")

st.title("Role Mentor")

with st.sidebar:
    st.image("/Users/harshit/Documents/Projects/role-mentor/src/assets/logo.jpg", width=1500)
    with st.popover("Settings", use_container_width=True):
        st.text_input("Open AI Key", key="openai_key")
        st.button("Apply", use_container_width=True)
        
    st.divider()
    
    st.title("Sessions")
    col = st.columns(1)[0]
    with col:
        st.button("Session 1", use_container_width=True)
        st.button("Session 2", use_container_width=True)

# Record audio
audio_value = st.audio_input("Record a voice message.", key="audio1")

if audio_value:
    transcription = utils.transcribe_audio(audio_value)
    transcription_generator = utils.create_generator(transcription)
    st.audio(audio_value)
    st.write_stream(transcription_generator)
    
    speech = utils.text_to_speech(transcription)
    st.audio("speech.wav")