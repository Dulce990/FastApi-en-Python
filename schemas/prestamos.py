"""Este módulo define los esquemas para el modelo Prestamo."""

from datetime import datetime
from pydantic import BaseModel


class PrestamoBase(BaseModel):
    """Esquema base para un préstamo."""
    id_usuario: str
    id_material: str
    fecha_prestamo: datetime
    fecha_devolucion: datetime
    estatus: str


class PrestamoCreate(PrestamoBase):
    """Esquema para la creación de un préstamo."""
    # No se requieren campos adicionales.


class PrestamoUpdate(PrestamoBase):
    """Esquema para la actualización de un préstamo."""
    # No se requieren campos adicionales.


class Prestamo(PrestamoBase):
    """Esquema que representa un préstamo con su ID."""
    id_prestamo: int

    class Config:
        """Configuración para el modelo Pydantic, permitiendo la 
        creación a partir de atributos ORM."""
        from_attributes = True
