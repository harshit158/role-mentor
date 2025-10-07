import streamlit as st
from src.frontend import utils
from src.frontend import api_utils

user_id = "1"
cols = st.columns([25, 50, 25])
with cols[1]:
    # display main chat box
    with st.container(border=True, height=800):
        utils.display_messages(user_id)
    
    audio_value = st.audio_input("Record a voice message.", key=f"audio{len(st.session_state.messages)}")
    if audio_value:
        transcription = utils.get_transcript(audio_value)
        api_utils.invoke_interviewer(transcription)
        st.rerun()

utils.display_sidebar()