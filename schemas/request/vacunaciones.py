from pydantic import BaseModel

class VacunacionesIn(BaseModel):
    carbon: bool
    fiebre_aftosa:bool
    bruselosis:bool
    rabia:bool
    vitaminas:bool
    animal: int

    class Config:
        orm_mode = True