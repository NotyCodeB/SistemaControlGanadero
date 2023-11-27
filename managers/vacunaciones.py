from asyncpg import UniqueViolationError
from fastapi import HTTPException

from db import database
from models import vacunaciones


class VacunacionManager:
    @staticmethod
    async def registrar_vacunacion(vacunaciones_data):
        try:
            id_ = await database.execute(vacunaciones.insert().values(**vacunaciones_data))
        except UniqueViolationError:
            raise HTTPException(400, "Error insertando datos")
        vacunas_do = await database.fetch_one(vacunaciones.select().where(vacunaciones.c.id == id_))
        return vacunas_do

    @staticmethod
    async def get_all_vacunaciones():
        return await database.fetch_all(vacunaciones.select())

    @staticmethod
    async def delete(vacunas_data):
        await database.execute(vacunaciones.delete().where(vacunaciones.c.id == vacunas_data))