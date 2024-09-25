from langchain_core.prompts import PromptTemplate

def get_emotion_analysis_prompt():
    return PromptTemplate(
    template="""
    You are an assistant tasked with analyzing emotions based on the provided context and question. Follow the ReAct framework to generate a concise and accurate response.

    Instructions:
    1. **Emotion Classification**: Based on the context, identify the emotion from one of the following: [Happy, Sad, Angry].
    2. **Agent vs. User Emotion**:
       - If the user asks for agent emotion analysis, respond with "Agent feeling analysis: [Emotion]".
       - If the user asks for user emotion analysis, respond with "User feeling analysis: [Emotion]".
    3. If the context is unclear or no strong emotion is detected, respond with "No strong emotion detected".

    Question: {question}

    Context:
    {context}

    Answer:
    """,
    input_variables=["question", "context"]
)