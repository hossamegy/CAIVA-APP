from agent.tools.assistant_tools import emotions, eyes
from agent.tools.retrieve_tools import agent_info, user_info, book_info

from agent.prompts import get_generate_answer_prompt, get_grade_prompot, get_analyize_prompt
from settings import get_settings

from langchain_google_genai import  ChatGoogleGenerativeAI
from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.messages import AIMessage
from langgraph.graph import StateGraph, END, START
from typing import TypedDict, Annotated, Literal
from operator import add
from langchain_core.messages import AIMessage, AnyMessage
from typing import Annotated, Literal, TypedDict


class State(TypedDict):
   messages: Annotated[list[AnyMessage], add]

class Caiva:
    def __init__(self):
       
        graph = StateGraph(State)
        graph.add_node("agent", self.agent)
        graph.add_node("understand-gen-new-q", self.gen_clean_question)


        graph.add_node("eye", eyes)
        graph.add_node("emotions", emotions)
        graph.add_node("user_information", user_info)
        graph.add_node("agent_information", agent_info)
        graph.add_node("book_information", book_info)


        graph.add_node("generate", self.generate_answer)


        graph.add_edge(START, "agent")
        graph.add_edge("agent", "understand-gen-new-q")

        graph.add_edge("user_information", "generate")
        graph.add_edge("agent_information", "generate")
        graph.add_edge("book_information", "generate")


        graph.add_conditional_edges(
            "understand-gen-new-q",
            # Assess agent decision
            self.grade_tools,
        )

        graph.add_edge("generate", END)
        self.agentGraph = graph.compile()
  
    def agent(self, state):
        print('agent done')

        messages = state['messages']

        model = ChatGoogleGenerativeAI(
            temperature=get_settings().TEMPERATURE, 
            model=get_settings().MODEL_NAME, 
            google_api_key=get_settings().API_KEY
        )

        # model = model.bind_tools(tools)
        response = model.invoke(messages)
        return {"messages": [response]}
    
    def generate_answer(self, state):
        print('generate_answer done')

        messages = state['messages']
        question = messages[0].content
        context = messages[-1].content

        model = ChatGoogleGenerativeAI(
            temperature=get_settings().TEMPERATURE, 
            model=get_settings().MODEL_NAME, 
            google_api_key=get_settings().API_KEY
        )

        prompt = get_generate_answer_prompt()

        chain = prompt | model
        result = chain.invoke({"question": question, "context": context})
        messages = messages + [AIMessage(content=result.content)]
        return {"messages": messages}

    def gen_clean_question(self, state):
        print('gen_clean_question done')
        messages = state['messages']
        question = messages[0].content

        prompt =get_analyize_prompt()

        model = ChatGoogleGenerativeAI(
            temperature=get_settings().TEMPERATURE, 
            model=get_settings().MODEL_NAME, 
            google_api_key=get_settings().API_KEY
        )

        chain = prompt | model
        result = chain.invoke({"input": question})
        messages = [AIMessage(content="Discuss how data traffic management works")] + [AIMessage(content=result.content)]
        return {"messages": messages}


    def grade_tools(self, state) -> Literal["agent_information", "user_information", "book_information", "eye", "emotions"]:
        """
        Determines which tool to use based on the current state.

        Args:
            state (messages): The current state

        Returns:
            str: A decision for which tool to use based on the current state.
        """
        print("---CHECK RELEVANCE---")

        # Data model
        class grade(BaseModel):
            """Binary score for relevance check."""
            out: str = Field(description="Decision indicator: 'agent' for agent information, 'user' for user information, 'book' for book information, 'eye' for eye-related information, or 'emotions' for emotions-related information.")

        # LLM
        model = ChatGoogleGenerativeAI(
            temperature=get_settings().TEMPERATURE, 
            model=get_settings().MODEL_NAME, 
            google_api_key=get_settings().API_KEY
        )
        llm_with_tool = model.with_structured_output(grade)

        # Updated Prompt
        prompt = get_grade_prompot()

        # Chain
        chain = prompt | llm_with_tool
        messages = state["messages"]
    
        question = messages[0].content

        scored_result = chain.invoke({"question": question})
        print(scored_result.out)
        score = scored_result.out

        # Determine the tool based on the score returned by the model
        if score == "agent":
            print("---DECISION: USE AGENT TOOL---")
            return "agent_information"
        elif score == "user":
            print("---DECISION: USE USER TOOL---")
            return "user_information"
        elif score == "book":
            print("---DECISION: USE BOOK TOOL---")
            return "book_information"
        elif score == "eye":
            print("---DECISION: USE EYE TOOL---")
            return "eye"
        elif score == "emotions":
            print("---DECISION: USE EMOTIONS TOOL---")
            return "emotions"
        else:
            raise ValueError(f"Unexpected score: {score}")
        

    