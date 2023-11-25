from schemas.base import UserBase


class RegistrarUsuario(UserBase):
    password: str
    first_name: str
    last_name: str
    phone: str
    cedula: str

class UserChangeData(UserBase):
    first_name: str
    last_name: str
    phone: str
    cedula: str

class LoginUsuario(UserBase):
    password : str


class Config:
    orm_mode = True