from agent.caivaAgent import Caiva
from fastapi import APIRouter
from langchain_core.messages import HumanMessage

agent_router = APIRouter()

abot = Caiva()

@agent_router.get('/ans')

def get_ans(input):
    messages = [HumanMessage(content=input)]
    result = abot.g.invoke({"messages": messages})
    return {
        "message":result['messages'][-1].content
    }
