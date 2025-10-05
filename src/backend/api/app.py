from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

from .routers import agents

app = FastAPI()

app.include_router(agents.router)

def main():
    import uvicorn
    uvicorn.run("src.backend.api.app:app", reload=True)