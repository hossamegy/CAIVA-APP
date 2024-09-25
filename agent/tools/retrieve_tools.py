from langchain.pydantic_v1 import BaseModel, Field
from typing import TypedDict, Annotated
from operator import add
from langchain_core.messages import AIMessage, AnyMessage
from typing import Annotated, TypedDict
from agent import CreateVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from settings import get_settings

embeddings = GoogleGenerativeAIEmbeddings(
    model=get_settings().EMBEDDING_MODEL, 
    google_api_key=get_settings().API_KEY
)

paths = ["/content/agent_info.pdf"]
vectorstore_agent = CreateVectorStore(paths, embeddings)
vectorDB_agent = vectorstore_agent()

paths = ["/content/user_info.pdf"]
vectorstore_user = CreateVectorStore(paths, embeddings)
vectorDB_user = vectorstore_user()
paths = ["/content/7-ch2_part2.pdf"]
vectorstore_domain = CreateVectorStore(paths, embeddings)
vectorDB_domain = vectorstore_domain()

class InputQuery(BaseModel):
        query: str = Field(description="The query string used for searching the vector store")

class State(TypedDict):
   messages: Annotated[list[AnyMessage], add]


def format_documents(documents: list) -> str:
        """
        Converts document objects into a readable string format.

        Args:
            documents (List[dict]): List of document objects with metadata and content.

        Returns:
            str: Formatted string with document details.
        """
        formatted_output = ""
        for doc in documents:
            source = doc.metadata.get('source', 'Unknown Source')
            page_number = doc.metadata.get('page', 0) + 1
            content = doc.page_content

            formatted_output += (
                f"Source: {source}\n"
                f"Page Number: {page_number}\n"
                f"Content: {content}\n\n"
            )
        return formatted_output

def agent_info(state: State) -> dict:
   
    

    messages = state['messages']
    query = messages[0].content
    # Perform the search and handle errors
    try:
        documents_retrieved = vectorDB_agent.similarity_search(query)
    except Exception as e:
        raise RuntimeError(f"An error occurred while querying the vector database: {e}")
    messages = messages + [AIMessage(content=format_documents(documents_retrieved))]
    # Return formatted results
    return {"messages": messages}


def user_info(state) -> dict:
   
    def format_documents(documents: list) -> str:
        """
        Converts document objects into a readable string format.

        Args:
            documents (List[dict]): List of document objects with metadata and content.

        Returns:
            str: Formatted string with document details.
        """
        formatted_output = ""
        for doc in documents:
            source = doc.metadata.get('source', 'Unknown Source')
            page_number = doc.metadata.get('page', 0) + 1
            content = doc.page_content

            formatted_output += (
                f"Source: {source}\n"
                f"Page Number: {page_number}\n"
                f"Content: {content}\n\n"
            )
        return formatted_output

    messages = state['messages']
    query = messages[0].content
    # Perform the search and handle errors
    try:
        documents_retrieved = vectorDB_user.similarity_search(query)
    except Exception as e:
        raise RuntimeError(f"An error occurred while querying the vector database: {e}")
    messages = messages + [AIMessage(content=format_documents(documents_retrieved))]
    # Return formatted results
    return {"messages": messages}


def book_info(state) -> dict:
   
    def format_documents(documents: list) -> str:
        """
        Converts document objects into a readable string format.

        Args:
            documents (List[dict]): List of document objects with metadata and content.

        Returns:
            str: Formatted string with document details.
        """
        formatted_output = ""
        for doc in documents:
            source = doc.metadata.get('source', 'Unknown Source')
            page_number = doc.metadata.get('page', 0) + 1
            content = doc.page_content

            formatted_output += (
                f"Source: {source}\n"
                f"Page Number: {page_number}\n"
                f"Content: {content}\n\n"
            )
        return formatted_output

    messages = state['messages']
    query = messages[0].content
    # Perform the search and handle errors
    try:
        documents_retrieved = vectorDB_domain.similarity_search(query)
    except Exception as e:
        raise RuntimeError(f"An error occurred while querying the vector database: {e}")
    messages = messages + [AIMessage(content=format_documents(documents_retrieved))]
    # Return formatted results
    return {"messages": messages}