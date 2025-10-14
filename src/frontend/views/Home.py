import streamlit as st
from src.frontend import utils
from src.frontend import api_utils

user_id = st.selectbox("User_ID", ["1", "2", "3", "4", "5"], key="user_id")

cols = st.columns([25, 50, 25], border=True)

# Plan column
with cols[0]:
    st.subheader("Plan")
    role = st.selectbox("Select Role", ["MLE (Tiktok)", "MLE (Meta)", "SE (Google)"], key="plan")
    if role == "MLE (Tiktok)":
        st.button("Round 1 (Technical)", width="stretch")
        st.button("Round 2 (Technical)", width="stretch")
        st.button("Round 3 (Behavioral)", width="stretch")
    
# Chat column
with cols[1]:
    st.subheader("Chat")
    
    with st.container(border=True, height=800):
        total_messages = utils.display_messages(user_id)
    
    audio_value = st.audio_input("Record a voice message.", key=f"audio{total_messages}")
    if audio_value:
        transcription = utils.get_transcript(audio_value)
        api_utils.invoke_interviewer(transcription, user_id)
        st.rerun()

# Result column
with cols[2]:
    st.subheader("Result")
    for metrics in ["Answer structure", "Keyword coverage", "Relevance", "Conciseness"]:
        st.write(metrics)
        st.feedback("stars", key=metrics)

utils.display_sidebar()