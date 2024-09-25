from langchain_core.prompts import PromptTemplate

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