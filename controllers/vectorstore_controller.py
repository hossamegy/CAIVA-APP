
from .base_controller import BaseController
from vectorStore import VectorStoreCreator
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from settings import get_settings
import os

class VectorStoreController(BaseController):
    def __init__(self):
        super().__init__()
    
    def create_vector_store(self, path):
        embeddings = GoogleGenerativeAIEmbeddings(
            model=get_settings().EMBEDDING_MODEL, 
            google_api_key=get_settings().API_KEY
        )

        vectorStoreCreator= VectorStoreCreator()
        vectorStore = vectorStoreCreator([path], embeddings, loader_type='pdf')
        vectorStore.save_local(os.path.join(
            self.PDF_Embeddings_path,
            r"pdf_faiss_index"
        ))
        

