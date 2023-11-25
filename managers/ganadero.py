from asyncpg import UniqueViolationError
from fastapi import HTTPException

from db import database
from models import ganado


class GanadoManager:

    @staticmethod
    async def registrar_ganado(ganado_data):
        try:
            id_ = await database.execute(ganado.insert().values(**ganado_data))
        except UniqueViolationError:
            raise HTTPException(400, "Error insertando datos")
        ganado_do = await database.fetch_one(ganado_data.select().where(ganado_data.c.id == id_))
        return ganado_do

    @staticmethod
    async def get_all_ganado():
        return await database.fetch_all(ganado.select())

    @staticmethod
    async def get_by_identificacion(identificacion):
        return await database.fetch_all(ganado.select().where(ganado.c.Metodo_identificacion == identificacion))

    @staticmethod
    async def get_by_categoria(categoria):
        return await database.fetch_all(ganado.select().where(ganado.c.categoria == categoria))
    @staticmethod
    async def delete(ganado_data):
        await database.execute(ganado.delete().where(ganado.c.id == ganado_data))