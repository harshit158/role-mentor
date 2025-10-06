from fastapi import FastAPI, APIRouter
from src.backend.agents.supervisor import get_graph
from src.backend import utils
from src import models

# Get agents graphs
supervisor_agent = get_graph(utils.get_memory())

config={
    "callbacks": [utils.get_langfuse_handler()],
    "configurable": {"thread_id": "1"}
}

router = APIRouter()

@router.post("/chat")
async def chat(message: str):
    return await supervisor_agent.ainvoke({"messages": [{"role": "user", "content": message}]}, config=config)

@router.get("/history/{user_id}")
async def history(user_id: str) -> models.Conversation:
    config={"configurable": {"thread_id": user_id}}
    state = await supervisor_agent.aget_state(config=config)
    
    conversation = {}
    conversation['messages'] = state.values.get("messages", [])
    return conversation