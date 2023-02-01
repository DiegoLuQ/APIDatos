from pydantic import BaseModel, Field
from bson.objectid import ObjectId
from datetime import datetime, date

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class Mensaje_Email(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    nombre: str = Field(description="Nombre del emisor", min_length=3 )
    email: str = Field(description="Email del emisor", min_length=5)
    mensaje: str = Field(description="Mensaje del emisor", min_length=1)
    fecha=date.today()

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "nombre":"Diego",
                "email":"sincero_.dig@gmail.com",
                "mensaje":"Hola"
            }
        }