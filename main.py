from fastapi import FastAPI
from agent.caivaAgent import Caiva
app = FastAPI()

abot = Caiva()

@app.get('/')
def get_welcome():
    return {
        "message": "hello world"
    }

# caivaBot = Caiva()