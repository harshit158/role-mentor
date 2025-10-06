from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

from .routers import router_agents

app = FastAPI()

app.include_router(router_agents.router)

def main():
    import uvicorn
    uvicorn.run("src.backend.api.app:app", reload=True)