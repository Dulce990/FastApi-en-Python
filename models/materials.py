"""Este módulo contiene el modelo para la tabla 'tbb_Material'."""

import enum
from sqlalchemy import Column, Integer, String, Enum
from config.db import Base
from sqlalchemy.orm import relationship

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
    TipoMaterial = Column(Enum(TipoMaterial),nullable=False)
    Marca = Column(String(60), nullable=False)
    Modelo = Column(String(100), nullable=False)
    Estado = Column(Enum(Estatus), nullable=False)

    prestamo = relationship("Prestamo", back_populates="material")