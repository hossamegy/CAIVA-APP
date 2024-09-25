from langchain_google_genai import  ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage
from agent.prompts import get_emotion_analysis_prompt
from settings import get_settings

def eyes(state):
    """
    Describes what the model can 'see' or observe based on the input query.

    Args:
        query (str): A query to generate a visual response.

    Returns:
        str: A description of what the model 'sees'.
    """
    messages = state['messages']
    messages = messages + [AIMessage(content='i see two cats')]
    # Return formatted results
    return {"messages": messages}


def emotions(state):
    print('generate_answer done')
    
    messages = state['messages']
    question = messages[0].content
    context = messages[-1].content

    model = ChatGoogleGenerativeAI(
        temperature=get_settings().TEMPERATURE, 
        model=get_settings().MODEL_NAME, 
        google_api_key=get_settings().API_KEY
    )

    prompt = get_emotion_analysis_prompt()

    chain = prompt | model
    result = chain.invoke({"question": question, "context": context})
    messages = messages + [AIMessage(content=result.content)]
    return {"messages": messages}

