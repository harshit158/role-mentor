import requests

URL = "http://localhost:8000/{endpoint}"

def invoke_interviewer(message: str):
    url = URL.format(endpoint="chat")
    response = requests.post(url, json={"messages": [{"role": "user", "content": message}]})
    return response.json()