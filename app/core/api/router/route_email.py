from fastapi import APIRouter, HTTPException, status
from core.schemas.schema_email import Mensaje_Email
from core.db.repo_email import create_email
from fastapi.encoders import jsonable_encoder

router = APIRouter()

@router.post('/')
def obtener_email(model:Mensaje_Email):
    dato = create_email(jsonable_encoder(model))
    if(dato):
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Mensaje Recibido")
    return HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Mensaje no enviado")