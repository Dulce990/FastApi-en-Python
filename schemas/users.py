from datetime import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
    """Esquema base para el usuario."""
    nombre: str
    primerApellido: str
    segundoApellido: str
    TipoUsuario: str
    nombreUsuario: str
    correoElectronico: str
    contrasena: str
    numeroTelefono: str
    estatus: str
    fechaRegistro: datetime
    fechaActualizacion: datetime

class UserCreate(UserBase):
    """Esquema para la creación de un usuario."""
    pass

class UserUpdate(UserBase):
    """Esquema para la actualización de un usuario."""
    pass

class User(UserBase):
    """Esquema que representa un usuario con su ID."""
    id: int

    class Config:
        from_attributes = True
