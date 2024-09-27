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
            r"agent\vectore_store"
        )
            
    def generate_random_string(self, length: int = 8):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))