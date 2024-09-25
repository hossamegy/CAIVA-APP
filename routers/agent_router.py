from agent.caivaAgent import Caiva
from fastapi import APIRouter
from langchain_core.messages import HumanMessage
from fastapi.responses import JSONResponse
from controllers.agent_controller import return_agent_response

agent_router = APIRouter()

abot = Caiva()

@agent_router.get('/agent_response')
def get_agent_response(input: str):
    
    return JSONResponse(
        content=return_agent_response(input=input, agent=abot)
    )