from pymongo import MongoClient
from core.config.config import settings


conn = MongoClient(settings.RUTA_MONGO)


datos_diego = conn.api_diego.datos_api
db_login = conn.api_diego.datos_login
