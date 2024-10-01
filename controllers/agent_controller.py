from agent.caivaAgent import Caiva
from langchain_core.messages import HumanMessage


def return_agent_response(input: str, agent: Caiva) -> dict:

    messages = [HumanMessage(content=input)]

    result = agent.agentGraph.invoke({"messages": messages})

    return  result['messages'][-1].content
    