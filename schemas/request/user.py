from models import RoleType
from schemas.base import UserBase


class RegistrarUsuario(UserBase):
    password: str
    first_name: str
    last_name: str
    phone: str
    cedula: str

class LoginUsuario(UserBase):
    password : str