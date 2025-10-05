from langfuse.langchain import CallbackHandler
from langgraph.checkpoint.memory import InMemorySaver

def get_langfuse_handler():
    langfuse_handler = CallbackHandler()
    return langfuse_handler

def get_memory():
    memory = InMemorySaver()
    return memory