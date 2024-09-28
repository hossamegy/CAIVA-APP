from fastapi import UploadFile
from .base_controller import BaseController
import os 

class ProjectController(BaseController):
    
    def __init__(self):
        super().__init__()

    def get_PDF_Embeddings_path(self, id: str) -> str:

        PDF_Embeddings_path = os.path.join(
            self.base_path,
            id
        )

        if not os.path.exists(vectorstore_path):
             os.makedirs(vectorstore_path)

        return vectorstore_path
        