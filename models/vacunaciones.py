import sqlalchemy

from db import metadata

vacunas = sqlalchemy.Table(
    "vacunaciones",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("carbon", sqlalchemy.Boolean, nullable=True),
    sqlalchemy.Column("fiebre_aftosa", sqlalchemy.Boolean, nullable=True),
    sqlalchemy.Column("bruselosis", sqlalchemy.Boolean, nullable=True),
    sqlalchemy.Column("rabia", sqlalchemy.Boolean, nullable=True),
    sqlalchemy.Column("vitaminas", sqlalchemy.Boolean, nullable=True),
    sqlalchemy.Column("animal", sqlalchemy.ForeignKey("ganado.id"), nullable=False)
)
