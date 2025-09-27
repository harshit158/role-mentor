import time
from functools import lru_cache
from dotenv import load_dotenv
from io import BytesIO

load_dotenv()

from groq import Groq
client = Groq()

@lru_cache(maxsize=None)
def transcribe_audio(file):
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
    response.write_to_file("speech.wav")

def create_generator(text):
    words = text.split()
    for word in words:
        yield word + ' '
        time.sleep(0.07) 