from typing import Optional, List

from fastapi import APIRouter, Depends

from managers.auth import oauth2_scheme, es_admin
from managers.user import UserManager
from models import RoleType
from schemas.response.user import UserResponse

router = APIRouter(tags=["Users"])


@router.get("/users/", dependencies=[Depends(oauth2_scheme), Depends(es_admin)], response_model=List[UserResponse])
async def get_users(email: Optional[str] = None):
    if email:
        return await UserManager.get_user_by_email(email)

    return await UserManager.get_all_users()

# put porque es un update
@router.put("/users/{user_id}/make-admin", dependencies=[Depends(oauth2_scheme), Depends(es_admin)], status_code=204)
async def make_admin(user_id: int):
    await UserManager.change_role(RoleType.admin, user_id)


# put porque es un update
@router.put("/users/{user_id}/make-ganadero", dependencies=[Depends(oauth2_scheme), Depends(es_admin)], status_code=204)
async def make_ganadero(user_id: int):
    await UserManager.change_role(RoleType.ganadero, user_id)