from pathlib import Path
from dotenv import load_dotenv
from os import environ


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    RUTA_MONGO = environ.get('RUTA_MONGO')
    DOCS = environ.get('DOCS')
    REDOCS = environ.get('REDOCS')
    SECRET_KEY = environ.get('SECRET_KEY')
    ALGORITHM = environ.get('ALGORITHM')
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    REFRESH_TOKEN_EXPIRE_MINUTES = 30

    # FASTAPI
    TITLE = "Portafolio Backend Developer"
    VERSION = "1.0.0.0"
    CONTACT = {
                    "name": "Diego Luque",
                    "url": "https://www.diego-luque.com",
                    "email": "ds.diegoluque@gmail.com",
    }
    DESCRIPTION = """
    API para portafolio 😀
    donde podremos obtener los datos del programador y sus proyectos.
## LA RUTA
    - Get - https://api.diego-luque.com/api/v1/datos

## Data

You will be able to:

* **Read Data**.
* **Create Data** (if u are admin).
* **Patch Data** (if u are admin).

    """


settings = Settings()
