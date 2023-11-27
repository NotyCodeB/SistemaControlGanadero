from typing import List

from fastapi import APIRouter, Depends

from managers.auth import oauth2_scheme, es_admin
from managers.vacunaciones import VacunacionManager
from schemas.request.vacunaciones import VacunacionesIn
from schemas.response.vacunaciones import VacunacionesOut

router = APIRouter(tags=["Vacunaciones"])

@router.post("/vacunaciones/", status_code=201)
async def registrar_vacunacion(vacunacion_data: VacunacionesIn):
    return await VacunacionManager(vacunacion_data.dict())


@router.delete("/vacunaciones/{vacunacion_id}/", dependencies=[Depends(oauth2_scheme), Depends(es_admin)],
               status_code=204)  # 204 exito no retorna nada
async def delete_vacunaciones(vacunacion_id: int):
    await VacunacionManager.delete(vacunacion_id)

@router.get("/vacunaciones/", dependencies=[Depends(oauth2_scheme), Depends(es_admin)], response_model=List[VacunacionesOut])
async def get_vacunaciones():
    return await VacunacionManager.get_all_vacunaciones()

