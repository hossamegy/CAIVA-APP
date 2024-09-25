from fastapi import FastAPI
from routers import base_router, agent_router

app = FastAPI()

app.include_router(base_router)
app.include_router(agent_router)


@app.get('/')
def get_welcome():
    return {
        "message": "hello world"
    }
