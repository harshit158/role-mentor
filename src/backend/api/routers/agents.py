from fastapi import FastAPI, APIRouter

from src.backend.agents.supervisor import graph

router = APIRouter()

@router.get("/chat")
async def get_agents():
    return graph.invoke({"messages": [{"role": "user", "content": "what is the weather in sf"}]})