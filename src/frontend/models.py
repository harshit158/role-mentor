from pydantic import BaseModel
from enum import Enum
from typing import Optional

class Role(Enum):
    USER = "user"
    ASSISTANT = "assistant"
    
class Message(BaseModel):
    role: Role
    content: str
    audio: Optional[bytes] = None