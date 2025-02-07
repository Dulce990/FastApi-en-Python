"""Este módulo contiene el modelo para la tabla 'tbb_prestamos'."""

import enum
from sqlalchemy import Column, Integer, String, DateTime, Enum
from config.db import Base

class EstatusPrestamo(str, enum.Enum):
    """Enumeración de los posibles estados de un préstamo."""
    Activo = "Activo"
    Devuelto = "Devuelto"
    Vencido = "Vencido"

class Prestamo(Base):
    """Modelo de la tabla 'tbb_prestamos'."""
    __tablename__ = "tbb_prestamos"
    id_prestamo = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(String(50))
    id_material = Column(String(50))
    fecha_prestamo = Column(DateTime)
    fecha_devolucion = Column(DateTime, nullable=True)
    estatus = Column(Enum(EstatusPrestamo))
