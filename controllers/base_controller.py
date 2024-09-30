from settings import get_settings
import os
import random
import string

class BaseController:

    def __init__(self):
        self.settings = get_settings()
        self.base_path =os.path.dirname(os.path.dirname(__file__))

        self.pdfs_path = os.path.join(
            self.base_path,
            r"store\PDFfiles"
        )

        self.agent_vector_store_path = os.path.join(
            self.base_path,
            r"store\agent_info_faiss_index"
        )

        self.user_vector_store_path = os.path.join(
            self.base_path,
            r"store\user_info_faiss_index"
        )

        self.pdf_vector_store_path = os.path.join(
            self.base_path,
            r"store\pdf_faiss_index"
        )

        self.check_dir_exists(self.pdfs_path)

        
    def generate_random_string(self, length: int = 8):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    
    def check_dir_exists(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
