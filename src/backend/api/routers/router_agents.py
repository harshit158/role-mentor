from fastapi import APIRouter
from src.backend.agents.supervisor import get_graph_builder
from src.backend import utils
from src import models
from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver

# Get agents graphs
memory = utils.get_memory()
graph_builder = get_graph_builder()

config={"callbacks": [utils.get_langfuse_handler()]}

router = APIRouter()

@router.post("/chat/{user_id}")
async def chat(message: str, user_id: str):
    config["configurable"] = {"thread_id": user_id}
    async with AsyncSqliteSaver.from_conn_string("src/backend/db/checkpoints.sqlite") as memory:
        graph = graph_builder.compile(checkpointer=memory)
        return await graph.ainvoke({"messages": [{"role": "user", "content": message}]}, config=config)

@router.get("/history/{user_id}")
async def history(user_id: str) -> models.Conversation:
    config={"configurable": {"thread_id": user_id}}
    async with AsyncSqliteSaver.from_conn_string("src/backend/db/checkpoints.sqlite") as memory:
        graph = graph_builder.compile(checkpointer=memory)
        state = await graph.aget_state(config=config)
    
    conversation = {}
    conversation['messages'] = state.values.get("messages", [])
    return conversation