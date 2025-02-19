"""Este módulo contiene el modelo para la tabla 'tbb_prestamos'."""

import enum
from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKeyConstraint
from config.db import Base
from sqlalchemy.orm import relationship

class EstatusPrestamo(str, enum.Enum):
    """Enumeración de los posibles estados de un préstamo."""
    Activo = "Activo"
    Devuelto = "Devuelto"
    Vencido = "Vencido"

class Prestamo(Base):
    """Modelo de la tabla 'tbb_prestamos'."""
    __tablename__ = "tbb_prestamos"
    id_prestamo = Column(Integer, primary_key=True, autoincrement=True)
    id_usuario = Column(Integer)
    id_material = Column(Integer)
    fecha_prestamo = Column(DateTime , nullable=False)
    fecha_devolucion = Column(DateTime, nullable=True)
    estatus = Column(Enum(EstatusPrestamo), nullable=False)

    __table_args__ = (
            ForeignKeyConstraint(['id_material'], ['tbb_Material.id']),
            ForeignKeyConstraint(['id_usuario'], ['tbb_usuarios.id']),
        )

    material = relationship("Material", back_populates="prestamo")
    usuario = relationship("User", back_populates="prestamo")
