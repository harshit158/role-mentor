from typing import Annotated

from langchain.chat_models import init_chat_model
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

from langchain_ollama import ChatOllama

class State(TypedDict):
    messages: Annotated[list, add_messages]

llm = ChatOllama(model="llama3.1:8b")

# == Define nodes ==
def chatbot(state: State):
    system_message = {
            "role": "system",
            "content": """
            You are a helpful mock interviewer helping the student in preparing for his upcoming interviews for Machine Learning roles. 
            Ask relevant quesions one by one - and follow up questions based on student's response.
            Before each question, give a single line feedback on the student's previous response, except the first one.
            Keep the conversation flowing and engaging"""
        }

    messages = [system_message] + state["messages"] if len(state["messages"])==1 else state["messages"]
    return {"messages": [llm.invoke(messages)]}

def get_graph_builder():
    
    # == Add nodes ==
    graph_builder = StateGraph(State)
    graph_builder.add_node("chatbot", chatbot)

    # == Add edges ==
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", END)

    return graph_builder