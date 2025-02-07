"""Definición del modelo de la tabla 'tbb_usuarios' en la base de datos."""

import enum
from sqlalchemy import Column, Integer, String, DateTime, Enum
from config.db import Base

class TipoUsuario(str, enum.Enum):
    """Enumeración de los tipos de usuario."""
    ALUMNO = "Alumno"
    PROFESOR = "Profesor"
    SECRETARIA = "Secretaria"
    LABORATORISTA = "Laboratorista"
    DIRECTIVO = "Directivo"
    ADMINISTRATIVO = "Administrativo"

class Estatus(str, enum.Enum):
    """Enumeración de los estatus del usuario."""
    ACTIVO = "Activo"
    INACTIVO = "Inactivo"
    BLOQUEADO = "Bloqueado"
    SUSPENDIDO = "Suspendido"

class User(Base):
    """Modelo de la tabla 'tbb_usuarios'."""
    __tablename__ = "tbb_usuarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(60), nullable=False)
    primer_apellido = Column(String(60), nullable=False)
    segundo_apellido = Column(String(60), nullable=True)
    tipo_usuario = Column(Enum(TipoUsuario), nullable=False)
    nombre_usuario = Column(String(60), unique=True, nullable=False)
    correo_electronico = Column(String(100), unique=True, nullable=False)
    contrasena = Column(String(60), nullable=False)
    numero_telefono = Column(String(20), nullable=True)
    estatus = Column(Enum(Estatus), nullable=False)
    fecha_registro = Column(DateTime, nullable=False)
    fecha_actualizacion = Column(DateTime, nullable=False)
