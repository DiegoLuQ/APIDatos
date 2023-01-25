from fastapi import APIRouter
from .router.v1 import api_router

base_router = APIRouter()

base_router.include_router(api_router, prefix="/api")