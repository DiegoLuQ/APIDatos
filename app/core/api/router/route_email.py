from fastapi import APIRouter, HTTPException, status, Depends
from core.schemas.schema_email import Mensaje_Email, Get_Mensaje
from core.schemas.schemas_login import UserCreate
from core.db.repo_email import create_email, retrive_email
from core.api.router.route_login import get_current_user_from_token
from fastapi.encoders import jsonable_encoder
from typing import List

router = APIRouter()

@router.post('/')
def send_msg(model:Mensaje_Email):
    dato = create_email(jsonable_encoder(model))
    if(dato):
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Mensaje Recibido")
    return HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Mensaje no enviado")

@router.get('/')
def get_msg(current_user: UserCreate = Depends(get_current_user_from_token)) -> List[Get_Mensaje]:
    dato = retrive_email()
    return dato