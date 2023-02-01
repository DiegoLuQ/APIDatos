from fastapi import APIRouter
from .api_diego import router 
from .route_login import router as router_login
from .route_email import router as route_email

api_router = APIRouter()

api_router.include_router(router, prefix="/v1", tags=["Datos API"])
api_router.include_router(router_login, prefix="/login", tags=["Login"])
api_router.include_router(route_email, prefix="/email", tags=["Email"])