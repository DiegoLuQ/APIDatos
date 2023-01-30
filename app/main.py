from fastapi import FastAPI
from core.api.base import base_router
from fastapi.middleware.cors import CORSMiddleware
from core.config.config import settings


def include_router(app):
    app.include_router(base_router)


def start_app():
    app = FastAPI(docs_url="/"+settings.DOCS,
                  version=settings.VERSION, 
                  redoc_url="/"+settings.REDOCS,
                  title=settings.TITLE, 
                  description=settings.DESCRIPTION,
                  contact=settings.CONTACT)
                  
    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    include_router(app)
    return app


app = start_app()
