from langchain_core.prompts import PromptTemplate

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