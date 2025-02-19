"""Definición del modelo de la tabla 'tbb_usuarios' en la base de datos."""

import enum
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, Enum
from config.db import Base

class TipoUsuario(str, enum.Enum):
    """Enumeración de los tipos de usuario."""
    Alumno = "Alumno"
    Profesor = "Profesor"
    Secretaria = "Secretaria"
    Laboratorista = "Laboratorista"
    Directivo = "Directivo"
    Administrativo = "Administrativo"

class Estatus(str, enum.Enum):
    """Enumeración de los estatus del usuario."""
    Activo = "Activo"
    Inactivo = "Inactivo"
    Bloqueado = "Bloqueado"
    Suspendido = "Suspendido"

class User(Base):
    """Modelo de la tabla 'tbb_usuarios'."""
    __tablename__ = "tbb_usuarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(60))
    primerApellido = Column(String(60))
    segundoApellido = Column(String(60))
    TipoUsuario = Column(Enum(TipoUsuario))
    nombreUsuario = Column(String(60))
    correoElectronico = Column(String(100))
    contrasena = Column(String(60))
    numeroTelefono = Column(String(20))
    estatus = Column(Enum(Estatus))
    fechaRegistro = Column(DateTime)
    fechaActualizacion = Column(DateTime)

    prestamo = relationship("Prestamo", back_populates="usuario")