from models import RoleType
from schemas.base import UserBase


class UserResponse(UserBase):
    id: int
    first_name: str
    last_name: str
    phone: str
    role: RoleType
    cedula : str