from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PrestamoBase(BaseModel):
    id_usuario: str
    id_material: str
    fecha_prestamo: datetime
    fecha_devolucion: datetime
    estatus: str

class PrestamoCreate(PrestamoBase):
    pass

class PrestamoUpdate(PrestamoBase):
    pass

class Prestamo(PrestamoBase):
    id_prestamo: int

    class Config:
        from_attributes = True
