from langchain.pydantic_v1 import BaseModel, Field
from typing import TypedDict, List
from langchain_core.messages import AIMessage, AnyMessage
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from settings import get_settings

# Initialize embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model=get_settings().EMBEDDING_MODEL, 
    google_api_key=get_settings().API_KEY
)

# InputQuery model
class InputQuery(BaseModel):
    query: str = Field(description="The query string used for searching the vector store")

# State model
class State(TypedDict):
    messages: List[AnyMessage]  # Define explicitly as a list of AnyMessage

# Function to format documents into a readable string
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


# Helper function to load FAISS vector DB and perform a search
def query_faiss(vector_db_path: str, query: str, k: int = 5) -> list:
    """
    Helper function to query a FAISS vector store.

    Args:
        vector_db_path (str): Path to the FAISS vector database.
        query (str): The search query.
        k (int): Number of results to retrieve. Default is 5.

    Returns:
        list: List of retrieved documents.
    """
    try:
        # Load the FAISS vector store
        vectorDB = FAISS.load_local(vector_db_path, embeddings, allow_dangerous_deserialization=True)
    except FileNotFoundError:
        raise RuntimeError(f"FAISS index not found at {vector_db_path}")
    except Exception as e:
        raise RuntimeError(f"Failed to load FAISS index: {e}")
    
    try:
        # Perform the search query
        documents_retrieved = vectorDB.similarity_search(query, k=k)
    except Exception as e:
        raise RuntimeError(f"Error querying the FAISS index: {e}")

    return documents_retrieved


# Function to handle agent information queries
def agent_info(state: State) -> dict:
    messages = state['messages']
    query = messages[0].content

    # Query the agent info vector store
    documents_retrieved = query_faiss(r"store\agent_info_faiss_index", query)

    # Append results to messages and return
    messages.append(AIMessage(content=format_documents(documents_retrieved)))
    return {"messages": messages}


# Function to handle user information queries
def user_info(state: State) -> dict:
    messages = state['messages']
    query = messages[0].content

    # Query the user info vector store
    documents_retrieved = query_faiss(r"store\user_info_faiss_index", query)

    # Append results to messages and return
    messages.append(AIMessage(content=format_documents(documents_retrieved)))
    return {"messages": messages}


# Function to handle book information queries
def book_info(state: State) -> dict:
    messages = state['messages']
    query = messages[0].content

    # Query the book info vector store
    documents_retrieved = query_faiss(r"store\PDF_faiss_index", query, k=10)

    # Append results to messages and return
    messages.append(AIMessage(content=format_documents(documents_retrieved)))
    return {"messages": messages}
