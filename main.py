from fastapi import FastAPI
from agent.caivaAgent import Caiva
from controllers.agent_controller import agent_router
app = FastAPI()

abot = Caiva()
app.include_router(agent_router)

@app.get('/')
def get_welcome():
    return {
        "message": "hello world"
    }

# caivaBot = Caiva()