from typing import Optional
from pydantic import BaseModel, Field
from bson.objectid import ObjectId

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


_string = dict(min_length=1, max_length=10)


class UserCreate(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    username: str = Field(description="name for join in the app", example="Joe West",**_string)
    email: str = Field(description="email for confirmation", example="joewest@gmail.com",**_string)
    password: str = Field(description="pass for join in the app", example="***",min_length=3, max_length=10)
    is_active: bool
    is_admin= False
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "username":"finoli",
                "email":"ds.diegoluque@gmail.com",
                "password":"aqui_la_clave", 
                "is_active":True
             }}

class ShowUser(BaseModel):
    username: str
    email: str
    is_active: bool
    is_admin: bool

    class Config():
        orm_mode = True

class ShowUserForLogin(BaseModel):
    username: str
    password: str

    class Config():
        orm_mode = True