"""Este módulo contiene el modelo para la tabla 'tbb_Material'."""

import enum
from sqlalchemy import Column, Integer, String, Enum
from config.db import Base

class TipoMaterial(str, enum.Enum):
    """Enumeración de los tipos de material."""
    CANON = "Cañon"
    COMPUTADORA = "Computadora"
    EXTENSION = "Extension"

class Estatus(str, enum.Enum):
    """Enumeración de los estatus del material."""
    DISPONIBLE = "Disponible"
    PRESTADO = "Prestado"
    EN_MANTENIMIENTO = "En Mantenimiento"

class Material(Base):
    """Modelo de la tabla 'tbb_Material'."""
    __tablename__ = "tbb_Material"
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo_material = Column(Enum(TipoMaterial))
    marca = Column(String(60))
    modelo = Column(String(100))
    estado = Column(Enum(Estatus))
