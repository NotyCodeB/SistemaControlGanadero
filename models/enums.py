import enum


class RoleType(enum.Enum):
    ganadero = "Ganadero"
    admin = "admin"


class Genero(enum.Enum):
    macho = "Macho"
    hembra = "Hembra"


class Categoria(enum.Enum):
    leche = "Leche"
    engorde = "Engorde"
