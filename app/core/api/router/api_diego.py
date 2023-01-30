from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from core.db.repo_diego import create_datos, retrieve_dato, edit_dato
from core.schemas.schemas_diego import (DatosCompletos, Datos, DatosUpdate)
from core.schemas.schemas_login import UserCreate
from fastapi.encoders import jsonable_encoder
from core.api.router.route_login import get_current_user_from_token

router = APIRouter()


@router.get('/datos')
def get_dato() -> DatosCompletos:
    dato = retrieve_dato(name="Diego Luque Linares")
    return dato

@router.post('/')
def post_dato(model: Datos, current_user: UserCreate = Depends(get_current_user_from_token)):
    dato = create_datos(model=jsonable_encoder(model))
    return dato

@router.patch('/patch')
def patch_dato(id: str, model: DatosUpdate, current_user: UserCreate = Depends(get_current_user_from_token)):
    dato = edit_dato(id=id, model=model)
    return dato
