from settings import get_settings
import os
import random
import string

class BaseController:

    def __init__(self):
        self.settings = get_settings()
        self.base_path =os.path.dirname(os.path.dirname(__file__))
        self.vectorstore_path = os.path.join(
            self.base_path,
            r"store\PDFfiles"
        )

        
        self.PDF_Embeddings_path = os.path.join(
            self.base_path,
            r"store\PDF_Embeddings"
        )
        
        self.check_dir_exists(self.vectorstore_path)
        self.check_dir_exists(self.PDF_Embeddings_path)
        
    def generate_random_string(self, length: int = 8):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    
    def check_dir_exists(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
