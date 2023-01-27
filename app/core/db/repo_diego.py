from core.schemas.schemas_diego import DatosCompletos, Datos, DatosUpdate
from core.config.db import datos_diego
from bson.objectid import ObjectId

def create_datos(model:dict) -> dict:
    datos = datos_diego.insert_one(model)
    retrive = datos_diego.find_one({"_id":datos.inserted_id})
    return retrive


def retrieve_dato(name:str) -> dict:
    dato = datos_diego.find_one({'datos.name': name})
    return dato

def edit_dato(id:str, model:DatosUpdate):
   
    retrieve = datos_diego.find_one({'_id':id})
    if retrieve:
        dato_obj = dict(DatosUpdate(**retrieve))
        dato_obj.update(model.dict(exclude_unset = True))
        update_dato_obj = datos_diego.update_one({'_id':id}, {"$set": dato_obj})

        if update_dato_obj:
            data = datos_diego.find_one({'_id':id})
            return data
        else:
            return False
        
        return False
    
