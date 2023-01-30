from pydantic import BaseModel, Field
from typing import List
from bson import ObjectId


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


class VideosYoutube(BaseModel):
    canal: str = None
    titulo: str = None
    imagen: str = None
    description: str = None
    url: str = None
    categories: List[str] = None
    level: str = None
    type_back_front: str = None

class Category(BaseModel):
    # python mogodn
    tools: List[str] = None


class Projects(BaseModel):
    subdomain: str = None
    url: str = None
    titulo: str = None
    img: str = None
    categories: List[str] = None
    description: str = None
    level: str = None
    type_back_front: str = None


class RedesSociales(BaseModel):
    github: str = None
    youtube: str = None
    facebook: str = None
    linkedin: str = None
    tiktok: str = None
    instagram: str = None


class datosTecno(BaseModel):
    name: str = None
    logo: str = None


class Tecnologies(BaseModel):
    backend: List[str] = None
    databases: List[str] = None
    frontend: List[str] = None
    others: List[str] = None
    frameworks: List[str] = None


class DatosPersonales(BaseModel):
    name: str = None
    username: str = None
    age: int = None
    email: str = None
    description: str = None
    cv: str = None


class Location(BaseModel):
    ciudad: str = None
    pais: str = None


class Datos(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    datos: DatosPersonales
    url: str
    logo: str
    location: Location
    role: str
    level: str
    tecnologies: List[Tecnologies]
    rrss: RedesSociales
    canal_yt: List[VideosYoutube]
    projects: List[Projects]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "datos": {
                    "name": "Diego Luque Linares",
                    "username": "DiegoLuQ",
                    "age": 27,
                    "email": "ds.diegoluque@gmail.com",
                    "cv": "https://drive.google.com/file/d/1Zu2nZFRcPH0JIa-UXteDE95MBFsPAybs/view?usp=share_link",
                    "description": "¡Hola!, soy un programador backend autodidacta. Me considero una persona responsable, esforzada, que comprende que el trabajo en equipo potencia el desarrollo y acorta el tiempo para alcanzar las metas. Mi objetivo es trabajar en una startUp en lo que me apasiona, que es programar. Te invito a revisar mis trabajos, videos y algunos blogs. Desde ya muchas gracias por darte un tiempo para conocerme."
                },
                "url": "api.diego-luque.com/api/v1/datos",
                "logo": "/logo.png",
                "location": {
                    "ciudad": "Iquique",
                    "pais": "Chile"
                },
                "role": "Backend Developer",
                "level": "Junior",
                "tecnologies": [{
                    "backend": ["Python", "https://img.shields.io/badge/Python-006AC3?&style=plastic&logo=PYTHON&logoColor=white"],
                    "databases":["MongoDB", "https://img.shields.io/badge/MongoDB-008000?style=plastic&logo=mongodb&logoColor=white"],
                    "frontend":["React", "https://img.shields.io/badge/React-007ACC?style=plastic&logo=React&logoColor=white"],
                    "others":["Docker", "https://img.shields.io/badge/Docker-0047b3?&?style=plastic&logo=docker&logoColor=white"],
                    "frameworks":["FastApi", ""],
                },
                    {
                    "backend": ["FastAPI", "https://img.shields.io/badge/FastApi-00945C?&style=plastic&logo=FastApi&logoColor=white"],
                    "databases":["MySQL", "https://img.shields.io/badge/MySQL-404D59?style=plastic&logo=mysql&logoColor=white"],
                    "frontend":["Javascript", "-"],
                    "others":["Jinja", ""],
                    "frameworks":["FastAPI", ""],
                },
                    {
                    "backend": ["", ""],
                    "databases":["PostgresSQL", "https://img.shields.io/badge/PostgreSQL-316192?style=plastic&logo=postgresql&logoColor=white"],
                    "frontend":["TailWindCss", "https://img.shields.io/badge/tailwind-003880?style=plastic&logo=tailwindcss"],
                    "others":["Nginx", ""],
                    "frameworks":["", ""],
                }],
                "rrss":
                    {
                        "github": "https://github.com/DiegoLuQ",
                        "youtube": "https://www.youtube.com/@somosdev",
                        "linkedin": "https://www.linkedin.com/in/diegoluquelinares/",
                        "facebook": "-",
                        "tiktok": "-",
                        "instagram": ""
                },
                "canal_yt": [
                    {
                        "canal": "SomosDev",
                        "titulo": "CRUD FastAPI",
                        "imagen": "www.image.com/imagen",
                        "description": "loremasd asd-asd",
                        "url": "www.youtube.com/@somosdev",
                        "categories": ["mongodb", "react", "fastapi"],
                        "level":"normal",
                        "type_back_front":"full-stack"
                    },
                    {
                        "canal": "SomosDev",
                        "titulo": "CRUD FastAPI 2",
                        "imagen": "www.image.com/imagen",
                        "description": "loremasd asd-asd",
                        "url": "www.youtube.com/@somosdev",
                        "categories": ["mongodb", "python", "fastapi"],
                        "level":"normal",
                        "type_back_front":"backend"
                    },
                    {
                        "canal": "SomosDev",
                        "titulo": "CRUD FastAPI 3",
                        "imagen": "www.image.com/imagen",
                        "description": "loremasd asd-asd",
                        "url": "www.youtube.com/@somosdev",
                        "categories": ["react", "tailwind"],
                        "level":"normal",
                        "type_back_front":"frontend"
                    }
                ],
                "projects": [{
                    "subdomain": "pro-crud1",
                    "url": "pro-crud1.diego-luque.com",
                    "titulo": "CRUD 1",
                    "img": "/logo",
                    "categories": ["react", "tailwindcss", "fastapi"],
                    "description": "orem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500",
                    "level":"normal",
                    "type_back_front":"frontend"},
                    {
                    "subdomain": "pro-crud2",
                    "url": "pro-crud2.diego-luque.com",
                    "titulo": "CRUD 2",
                    "img": "/logo",
                    "categories": ["mongodb", "react", "fastapi"],
                    "description": "orem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500",
                    "level":"normal",
                    "type_back_front":"full-stack"},
                    {
                    "subdomain": "pro-crud3",
                    "url": "pro-crud3.diego-luque.com",
                    "titulo": "CRUD 3",
                    "img": "/logo",
                    "categories": ["mongodb", "python", "fastapi"],
                    "description": "orem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500",
                    "level":"normal",
                    "type_back_front":"backend"},
                    {
                    "subdomain": "pro-crud4",
                    "url": "pro-crud4.diego-luque.com",
                    "titulo": "CRUD 4",
                    "img": "/logo",
                    "categories": ["mongodb", "python", "fastapi"],
                    "description": "orem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500",
                    "level":"normal",
                    "type_back_front":"backend"}
                ]
            }
        }


class DatosCompletos(Datos):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")


class DatosUpdate(BaseModel):
    datos: DatosPersonales
    url: str = None
    logo: str = None
    location: Location
    role: str = None
    level: str = None
    tecnologies: List[Tecnologies] = None
    rrss: RedesSociales = None
    canal_yt: List[VideosYoutube] = None
    projects: List[Projects] = None