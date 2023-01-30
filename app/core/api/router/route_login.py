from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from core.api.utils import OAuth2PasswordBearerWithCookie
from datetime import timedelta
from jose import jwt, JWTError
from core.db.repo_login import get_user, list_user, create_user
from core.hashing import Hasher
from core.config.config import settings
from core.security import create_access_token
from core.schemas.schemas_login import ShowUserForLogin, UserCreate
from fastapi.encoders import jsonable_encoder

from pydantic import BaseModel

router = APIRouter()


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


def authenticate_user(username: str, password: str):
    user = get_user(username)
    pass_hash = user['password']
    if not user:
        return False
    if not Hasher.verify_password(password, pass_hash):
        return False
    return user


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login/token")


def get_current_user_from_token(token: str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,              
        detail="Could not validate credentials")
    try:
        # payload guardare el token obtenido en el login, juto la llave secrete y el algorith
        payload = jwt.decode(token, settings.SECRET_KEY,
                             algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception
    except JWTError:
        raise credential_exception

    user = get_user(username=username)
    if user is None:
        raise credential_exception
    return user


def get_current_active_user(current_user: ShowUserForLogin = Depends(get_current_user_from_token)):
    if current_user["is_active"]:
        return current_user
    raise HTTPException(status_code=400, detail="Inactive user")

def get_current(current_user: ShowUserForLogin = Depends(get_current_user_from_token)):
    return current_user

@router.post("/token", response_model=Token)
def login_for_access_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"], "admin": user["is_admin"]}, expires_delta=access_token_expires
    )
    print(access_token)
    response.set_cookie(
        key="access_token", value=f"Bearer {access_token}", httponly=True
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post('/registrar')
def registrar_usuario(model: UserCreate, current_user: UserCreate = Depends(get_current)):
    if not current_user["is_admin"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User not is Admin")
    model.password = Hasher.get_password_hash(model.password)
    user = create_user(model=jsonable_encoder(model))
    return user


@router.get('/buscar')
def buscar_usuario(current_user: UserCreate = Depends(get_current)):
    if not current_user["is_admin"]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User not is Admin")
    modelito = list_user()
    return modelito
