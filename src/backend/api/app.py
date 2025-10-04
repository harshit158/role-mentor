from fastapi import FastAPI

from .routers import agents

app = FastAPI()

app.include_router(agents.router)

def main():
    import uvicorn
    uvicorn.run("src.backend.api.app:app", reload=True)