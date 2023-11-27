from typing import Optional, List

from fastapi import APIRouter, Depends

from managers.auth import oauth2_scheme, es_admin
from managers.ganadero import GanadoManager
from schemas.request.ganado import GanadoIn
from schemas.response.ganado import GanadoOut

router = APIRouter(tags=["Ganado"])

@router.post("/ganado/")
async def registrar_ganado(ganado_data: GanadoIn):
    return await GanadoManager.registrar_ganado(ganado_data.dict())


@router.delete("/ganado/{ganado_id}/", dependencies=[Depends(oauth2_scheme), Depends(es_admin)],
               status_code=204)  # 204 exito no retorna nada
async def delete_ganado(localidad_id: int):
    await GanadoManager.delete(localidad_id)

@router.get("/ganado/", dependencies=[Depends(oauth2_scheme), Depends(es_admin)], response_model=List[GanadoOut])
async def get_ganado(categoria: Optional[str] = None, identificacion: Optional[str] = None):
    if categoria:
        return await GanadoManager.get_by_categoria(categoria)
    if identificacion:
        return await GanadoManager.get_by_identificacion(identificacion)

    return await GanadoManager.get_all_ganado()