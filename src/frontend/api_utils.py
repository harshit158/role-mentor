import requests
from src import models

URL = "http://localhost:8000/{endpoint}"

def invoke_interviewer(message: str, user_id: str):
    url = URL.format(endpoint=f"chat/{user_id}")
    # TODO: Make it a payload and not params
    response = requests.post(url, params={"message": message})
    return response.json()

def get_conversation(user_id: str) -> list[models.AIMessage | models.HumanMessage]:
    url = URL.format(endpoint=f"history/{user_id}")
    response = requests.get(url)
    
    messages = response.json()["messages"]
    messages = [models.AIMessage(**x) if x["type"] == "ai" else models.HumanMessage(**x) for x in messages]
    return messages