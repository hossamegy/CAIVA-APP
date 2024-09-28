from fastapi import APIRouter, UploadFile, status, Depends
from fastapi.responses import JSONResponse
from controllers import UploadController, VectorStoreController
from models.enum import ResponesUploadSignal
from settings import get_settings, Settings
import aiofiles
import os


upload_router = APIRouter()

@upload_router.post('/uplaod/')
async def upload_file(file: UploadFile, settings: Settings = Depends(get_settings)):
    upload_controller = UploadController()
    is_valid, response_signal = upload_controller.check_validation_upload_file(
        file=file
    )

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                'signal': response_signal,
            }
        )

    file_path, id = upload_controller.generate_unique_file_name(
        orignal_file_name=file.filename,
    
    )
    try:
        async with aiofiles.open(file_path, 'wb') as f:
            while chunk := await file.read(settings.FILE_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:
            return   JSONResponse(
                content={
                    'signal': ResponesUploadSignal.FILE_UPLOAD_FAILED.value,
                }
            )
 
    VectorStoreController().create_vector_store(os.path.abspath(file_path))

    return JSONResponse(
         content={
            'signal': ResponesUploadSignal.FILE_UPLOAD_SUCCESS.value,
            'file_id': id,
        }
    ) 