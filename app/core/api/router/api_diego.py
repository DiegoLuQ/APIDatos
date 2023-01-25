from fastapi import APIRouter
from fastapi.responses import JSONResponse

from core.db.repo_diego import create_datos, retrieve_dato, edit_dato
from core.schemas.schemas_diego import (DatosCompletos, Datos, DatosUpdate)
from fastapi.encoders import jsonable_encoder
router = APIRouter()


@router.get('/datos')
def get_dato(id:str) -> DatosCompletos:
    dato = retrieve_dato(id)
    return dato

@router.post('/')
def post_dato(model: Datos):
    dato = create_datos(model=jsonable_encoder(model))
    return dato

@router.patch('/patch')
def patch_dato(id: str, model: DatosUpdate):
    dato = edit_dato(id=id, model=model)
    return dato
