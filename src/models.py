from pydantic import BaseModel
from langchain_core.messages import HumanMessage, AIMessage
from enum import Enum
from typing import Optional

class Role(Enum):
    HUMAN = "human"
    AI = "ai"
    
class Message(BaseModel):
    role: Role
    content: str
    audio: Optional[bytes] = None

class Conversation(BaseModel):
    messages: list[HumanMessage | AIMessage]
    
class InputMessage(BaseModel):
    content: str