"""Este módulo contiene el modelo para la tabla 'tbb_Material'."""

import enum
from sqlalchemy import Column, Integer, String, Enum
from config.db import Base

class TipoMaterial(str, enum.Enum):
    """Enumeración de los tipos de material."""
    Cañon = "Cañon"
    Computadora = "Computadora"
    Extension = "Extension"

class Estatus(str, enum.Enum):
    """Enumeración de los estatus del material."""
    Disponible = "Disponible"
    Prestado = "Prestado"
    En_Mantenimiento = "En Mantenimiento"

class Material(Base):
    """Modelo de la tabla 'tbb_Material'."""
    __tablename__ = "tbb_Material"
    id = Column(Integer, primary_key=True, autoincrement=True)
    TipoMaterial = Column(Enum(TipoMaterial))
    Marca = Column(String(60))
    Modelo = Column(String(100))
    Estado = Column(Enum(Estatus))
