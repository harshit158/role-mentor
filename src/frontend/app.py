import streamlit as st
from src.frontend import utils
from src.frontend.models import Message

st.set_page_config(layout="wide")

if "messages" not in st.session_state:
    st.session_state.messages = []

utils.display_logo_in_center()
st.divider()

utils.display_sidebar()

cols = st.columns([25, 50, 25])
with cols[1]:
    # display main chat box
    with st.container(border=True, height=800):
        utils.display_messages()
    
    audio_value = st.audio_input("Record a voice message.", key=f"audio{len(st.session_state.messages)}")
    if audio_value:
        utils.process_audio_input(audio_value)
        st.rerun()