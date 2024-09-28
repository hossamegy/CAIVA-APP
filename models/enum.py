from enum import Enum

class ResponesUploadSignal(Enum):

    FILE_VALIDATED_SUCCESS = "file_validate_successfully"
    FILE_TYPE_NOT_SUPPORTED = "file_type_note_supported"
    FILE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_UPLOAD_SUCCESS = " file_upload_success"
    FILE_UPLOAD_FAILED = "file_upload_failed"
    PDF_DIRS_PATH_NOT_FOUNDED = "pdf_dirs_path_not_founded"
    EMBEDDINGS_DIR_PATH_NOT_FOUNDED = "embeddings_dirs_path_not_founded"