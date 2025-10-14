import time
from functools import lru_cache
from dotenv import load_dotenv
from src.models import Role, Message
import streamlit as st
from src.frontend.views import Profile
from src.frontend import api_utils

load_dotenv()

from groq import Groq
client = Groq()

def invoke_interviewer():
    system_message = {
                "role": "system",
                "content": """
                You are a helpful mock interviewer helping the student in preparing for his upcoming interviews for Machine Learning roles. 
                Ask relevant quesions one by one - and follow up questions based on student's response.
                Before each question, give a single line feedback on the student's previous response, except the first one.
                Keep the conversation flowing and engaging"""
            }
    human_message = {
                "role": Role.USER.value,
                "content": "Now, start asking questions."
            }
    
    messages = [system_message, human_message] + [{"role": message.role.value, "content": message.content} for message in st.session_state.messages]
    
    with st.spinner("Thinking..."):
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama-3.1-8b-instant"
            # model="llama-3.3-70b-versatile"
            # model="openai/gpt-oss-120b"
        )
        
    content = chat_completion.choices[0].message.content
    speech = None #text_to_speech(content)
    st.session_state.messages.append(Message(role=Role.ASSISTANT, 
                                             content=content,
                                             audio=speech))

@lru_cache(maxsize=None)
def transcribe_audio(file, test=False):
    if test:
        return "dummy text"
    transcription = client.audio.transcriptions.create(
    file=file,
    model="whisper-large-v3-turbo",
    response_format="json",
    prompt="capture even the filler words, like umm, agh, etc",
    )
    return transcription.text

def text_to_speech(text):
    response = client.audio.speech.create(
    model="playai-tts",
    voice="Celeste-PlayAI",
    input=text,
    response_format="wav"
    )
    
    return response.read()

def create_generator(text):
    words = text.split()
    for word in words:
        yield word + ' '
        time.sleep(0.07) 

def display_in_center(text, size=2):
    st.markdown(
        f"<div style='display: flex; justify-content: center; align-items: center; height: 100%;'><h{size}>{text}</h{size}></div>",
        unsafe_allow_html=True
    )

def display_logo_in_center():
    cols = st.columns([25, 50, 25])
    with cols[1]:
        st.image("/Users/harshit/Documents/Projects/role-mentor/src/assets/logo_wide.jpg", width="stretch")

def display_sidebar():
    with st.sidebar:
        st.title("History")
        col = st.columns(1)[0]
        with col:
            st.button("Session 1", width="stretch")
            st.button("Session 2", width="stretch")

def display_messages(user_id: str) -> int:
    # TODO: Convert this to async
    messages = api_utils.get_conversation(user_id)
    
    for message in messages:
        avatar = "src/assets/message_avatar.jpg" if message.type == Role.AI.value else None
        with st.chat_message(message.type, avatar=avatar):
            cols = st.columns([70, 30])
            with cols[0]:
                st.write(message.content)
            # with cols[1]:
            #     st.audio(message.audio)
    
    return len(messages)

def get_transcript(audio_value):
    audio_bytes = audio_value.read()
    audio_value.seek(0)
    transcription = transcribe_audio(audio_value, test=False)
    return transcription
        # st.session_state.messages.append(Message(role=Role.USER,
        #                                          content=transcription, 
        #                                          audio=audio_bytes))

import streamlit as st

def style_text(
    text: str,
    level: int = 1,
    align: str = "center",
    color: str = "#0E6909",
    background_color: str = "#A7A9A7",
):
    """
    Display a styled heading (h1-h6) in Streamlit using HTML and CSS.

    Args:
        text (str): The heading text.
        level (int): Heading level (1–6). Default: 1.
        align (str): Text alignment - 'left', 'center', or 'right'.
        font_size (str | None): Custom font size (e.g., '32px', '2.5rem'). Defaults to browser default for chosen h-level.
        color (str): Text color.
        background_color (str): Background color.
        font_family (str): Font family.
        padding (str): Padding around text.
        border_radius (str): Rounded corners for background.
    """

    # Ensure heading level is between 1 and 6
    level = max(1, min(level, 6))

    html_code = f"""
    <div style="text-align: {align};">
        <h{level} style="
            display: inline-block;
            color: {color};
            background-color: {background_color};
        ">
            {text}
        </h{level}>
    </div>
    """

    st.markdown(html_code, unsafe_allow_html=True)