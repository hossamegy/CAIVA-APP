from fastapi import UploadFile
from .base_controller import BaseController
import os 

class VectorStoreController(BaseController):
    
    def __init__(self):
        super().__init__()

    def get_vectorstore_path(self, id: str) -> str:

        vectorstore_path = os.path.join(
            self.vectorstore_path,
            id
        )

        if not os.path.exists(vectorstore_path):
             os.makedirs(vectorstore_path)

        return vectorstore_path
        