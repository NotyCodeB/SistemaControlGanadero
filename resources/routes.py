from fastapi import APIRouter

from resources import user
from resources import auth, ganado,vacunaciones

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(user.router)
api_router.include_router(ganado.router)
api_router.include_router(vacunaciones.router)