import streamlit as st
from src.frontend import utils

cols = st.columns([25, 50, 25])
with cols[1]:
    # display main chat box
    with st.container(border=True, height=800):
        utils.display_messages()
    
    audio_value = st.audio_input("Record a voice message.", key=f"audio{len(st.session_state.messages)}")
    if audio_value:
        utils.process_audio_input(audio_value)
        st.rerun()

utils.display_sidebar()