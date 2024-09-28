import re
import os
from models.enum import ResponesUploadSignal
from fastapi import UploadFile
from .base_controller import BaseController


class UploadController(BaseController):
    def __init__(self):
        super().__init__()

    def check_validation_upload_file(self, file: UploadFile):
        if file.content_type not in self.settings.FILE_ALLOWED_TYPES:
            return ResponesUploadSignal.FILE_TYPE_NOT_SUPPORTED.value
        
        if file.size > self.settings.FILE_MAX_SIZE * 1048576:
            return ResponesUploadSignal.FILE_SIZE_EXCEEDED.value
        
        return True, ResponesUploadSignal.FILE_UPLOAD_SUCCESS.value
    
    def generate_unique_file_name(self, orignal_file_name):
       def generate_new_path():
            random_key = self.generate_random_string()
            path = BaseController().vectorstore_path
            clean_file_name = self.get_clean_file_name(
                orig_file_name=orignal_file_name
            )
            
            return os.path.join(
                path,
                random_key + '_' + clean_file_name
            ), random_key
        
       final_new_path, random_key= generate_new_path()

       while os.path.exists(final_new_path):
            generate_new_path()

       return final_new_path, random_key
            
    def get_clean_file_name(self, orig_file_name: str):
        cleaned_file_name = re.sub(r'[^\w.]', '', orig_file_name.strip())
        return cleaned_file_name.replace(' ', '_')