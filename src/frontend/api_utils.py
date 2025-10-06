import requests
from src import models

URL = "http://localhost:8000/{endpoint}"

def invoke_interviewer(message: str):
    url = URL.format(endpoint="chat")
    response = requests.post(url, json={"messages": [{"role": "user", "content": message}]})
    return response.json()

def get_conversation(user_id: str) -> models.Conversation:
    url = URL.format(endpoint=f"history/{user_id}")
    response = requests.get(url)
    return response.json()