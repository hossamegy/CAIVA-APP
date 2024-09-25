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

def get_generate_answer_prompt():
    return PromptTemplate(
        template="""You are given a context and a question. Follow the ReAct framework to generate an accurate answer.

        Carefully analyze the provided context to understand the key details and how they relate to the question. Identify the main points and relevant information.
        Based on your reasoning, make a precise and accurate answer to the question using the information from the context.

        Question: {question}

        Context:
        {context}

        Answer:
        """,
        input_variables=["question", "context"]
    )

def get_grade_prompot():
    return PromptTemplate(
            template=""" 
            You are a grader tasked with selecting the most appropriate tool based on the user's question. 
            You have six tools at your disposal: 
            1. 'agent' — Use this tool when the user's question relates to agent-specific information.
            2. 'user' — Use this tool for questions about user-specific information or queries related to user details.
            3. 'book' — Use this tool when the question pertains to book-related inquiries.
            4. 'eye' — Use this tool for questions related to vision or eye-related inquiries.
            5. 'emotions' — Use this tool for questions concerning feelings or emotional states.

            Here is the user question: {question}

            Your task is to analyze the question and decide which tool is best suited for the user's needs:
            - If the question pertains to agent-related information, return 'agent'.
            - If the question relates to user information, return 'user'.
            - If the question involves books or literature, return 'book'.
            - If the question involves eye-related inquiries, return 'eye'.
            - If the question involves emotions, return 'emotions'.
            Make sure to provide a clear and accurate decision.
            """,
            input_variables=["question"],
        )

def get_analyize_prompt():
    return  PromptTemplate(
            template="""
            Your task is to decompose the provided complex input into its smallest, most manageable components.
            Each component should be a distinct, clear piece of information.
            Do not provide any explanations or additional commentary.

            Original input: {input}
            Result:
            """,
            input_variables=["input"]
        )