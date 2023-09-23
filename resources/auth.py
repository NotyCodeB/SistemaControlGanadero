from fastapi import APIRouter

from managers.user import UserManager
from schemas.request.user import RegistrarUsuario, LoginUsuario

router = APIRouter(tags=["Autenticacion"])


@router.post("/registro/", status_code=201)
# crea el token para el usuario registrado en UserManager.register
async def registrar_usuario(user_data: RegistrarUsuario):
    token = await UserManager.register(user_data.dict())
    return {"token": token}


@router.post("/login/")
async def login(user_data: LoginUsuario):
    token = await UserManager.login(user_data.dict())
    return {"token": token}

