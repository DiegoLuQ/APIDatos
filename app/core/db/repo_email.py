from core.schemas.schema_email import Mensaje_Email
from core.config.db import db_email

def create_email(model:dict) -> dict:
    dato = db_email.insert_one(model)
    retrive = db_email.find_one({"_id": dato.inserted_id})
    return retrive
    