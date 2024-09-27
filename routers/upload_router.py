from fastapi import APIRouter, UploadFile, status, Depends
from fastapi.responses import JSONResponse
from controllers import UploadController
from models.enum import ResponesUploadSignal
from settings import get_settings, Settings
import aiofiles



upload_router = APIRouter()

@upload_router.post('/uplaod/{id}')
async def upload_file(id: str, file: UploadFile, settings: Settings = Depends(get_settings)):
    upload_controller = UploadController()
    is_valid, response_signal = upload_controller.check_validation_upload_file(
        file=file
    )

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                'signal': response_signal
            }
        )

    file_path, id = upload_controller.generate_unique_file_name(
        orignal_file_name=file.filename,
        id=id
    )
    try:
        async with aiofiles.open(file_path, 'wb') as f:
            while chunk := await file.read(settings.FILE_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:
            return   JSONResponse(
                content={
                    'signal': ResponesUploadSignal.FILE_UPLOAD_FAILED
                }
            )
    
    return JSONResponse(
         content={
            'signal': ResponesUploadSignal.FILE_UPLOAD_SUCCESS,
            'file_id': id
        }
    ) 