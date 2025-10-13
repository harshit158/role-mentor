import streamlit as st
from src.frontend import utils
from src.frontend import api_utils

cols = st.columns([25, 50, 25])
with cols[1]:
    user_id = st.selectbox("User_ID", ["1", "2", "3", "4", "5"], key="user_id")
    
    with st.container(border=True, height=800):
        total_messages = utils.display_messages(user_id)
    
    audio_value = st.audio_input("Record a voice message.", key=f"audio{total_messages}")
    if audio_value:
        transcription = utils.get_transcript(audio_value)
        api_utils.invoke_interviewer(transcription, user_id)
        st.rerun()

utils.display_sidebar()