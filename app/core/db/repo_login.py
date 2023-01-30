from core.schemas.schemas_login import ShowUser, UserCreate, ShowUserForLogin
from core.config.db import datos_diego, db_login

def create_user(model:dict) -> dict:
    user = db_login.insert_one(model)
    retrive = db_login.find_one({"_id": user.inserted_id})
    return retrive

def list_user():
    user = [x for x in db_login.find({})]
    return user


def get_user(username: str):
    user = db_login.find_one({"username":username})
    return user

