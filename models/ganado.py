import sqlalchemy

from db import metadata
from models.enums import RoleType, Categoria, Genero

ganado = sqlalchemy.Table(
    "ganado",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("Metodo_identificacion", sqlalchemy.String(120), unique=True),
    sqlalchemy.Column("categoria", sqlalchemy.Enum(Categoria), nullable=False),
    sqlalchemy.Column("genero", sqlalchemy.Enum(Genero), nullable=False),
    sqlalchemy.Column("litros_leche_diarios", sqlalchemy.Float, nullable=False),
    sqlalchemy.Column("peso", sqlalchemy.String(20), nullable=True),
    sqlalchemy.Column("registrada_en", sqlalchemy.DateTime, server_default=sqlalchemy.func.now()),
    sqlalchemy.Column("id_usuario", sqlalchemy.ForeignKey("users.id"), nullable=False),
    sqlalchemy.Column("precio",sqlalchemy.Integer)
)