from fastapi import FastAPI
from core.api.base import base_router
from fastapi.middleware.cors import CORSMiddleware




def include_router(app):
    app.include_router(base_router)

def start_app():
    app = FastAPI(docs_url="/diegoapi")
    origins = [
    "http://127.0.0.1:5173", 
    "https://api.diego-luque.com/",
    "https://www.diego-luque.com/",
    "https://diego-luque.com/"
    ]
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