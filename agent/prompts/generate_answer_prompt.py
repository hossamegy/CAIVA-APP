from langchain_core.prompts import PromptTemplate

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