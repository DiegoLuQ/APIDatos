from fastapi import APIRouter
from .api_diego import router 
from .route_login import router as router_login

api_router = APIRouter()

api_router.include_router(router, prefix="/v1", tags=["Datos API"])
api_router.include_router(router_login, prefix="/login", tags=["Login"])