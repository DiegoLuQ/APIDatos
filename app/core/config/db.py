from pymongo import MongoClient
from core.config.config import settings


conn = MongoClient(settings.RUTA_CLUSTER)


datos_diego = conn.api_diego.datos_api
db_login = conn.api_diego.datos_login
db_email = conn.api_diego.datos_email
