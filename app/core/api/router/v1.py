from fastapi import APIRouter
from .api_diego import router 

api_router = APIRouter()

api_router.include_router(router, prefix="/v1", tags=["Datos API"])