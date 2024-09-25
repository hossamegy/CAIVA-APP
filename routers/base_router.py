from settings import get_settings
from fastapi import APIRouter
from fastapi.responses import JSONResponse

base_router = APIRouter()

@base_router.get('/project_info')
def get_project_info():
    
    return JSONResponse(
        content={
            "project_name": get_settings().NAME,
            "project_version": get_settings().VERSION,
            "api_key": get_settings().API_KEY,
            "Model_name": get_settings().MODEL_NAME,
            "Embbedings_name": get_settings().EMBEDDING_MODEL
        }
    )