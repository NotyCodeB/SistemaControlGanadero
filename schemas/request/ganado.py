from pydantic import BaseModel
from datetime import datetime
from models import Categoria, Genero


class GanadoIn(BaseModel):

    Metodo_identificacion: str
    categoria: Categoria
    genero: Genero
    litros_leche_diarios: float
    peso: str
    registrada_en : datetime
    id_usuario: int
    precio: int



    class Config:
        orm_mode = True

