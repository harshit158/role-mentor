import aiosqlite
from functools import lru_cache
from langfuse.langchain import CallbackHandler
from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver

def get_langfuse_handler():
    langfuse_handler = CallbackHandler()
    return langfuse_handler

async def get_memory():
    conn = await aiosqlite.connect("src/backend/db/checkpoints.sqlite", check_same_thread=False)
    memory = AsyncSqliteSaver(conn)
    return memory
