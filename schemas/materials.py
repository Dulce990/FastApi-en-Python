"""Este módulo define los esquemas para el modelo Material."""

from pydantic import BaseModel


class MaterialBase(BaseModel):
    """Esquema base para el material."""
    TipoMaterial: str
    Marca: str
    Modelo: str
    Estado: str


class MaterialCreate(MaterialBase):
    """Esquema para la creación de un material."""
    # No es necesario 'pass' ya que el docstring cumple la función de un statement.


class MaterialUpdate(MaterialBase):
    """Esquema para la actualización de un material."""
    # No es necesario 'pass' ya que el docstring cumple la función de un statement.


class Material(MaterialBase):
    """Esquema que representa un material con su ID."""
    id: int

    class Config:
        """Configuración para el modelo Pydantic, 
        permitiendo crear instancias a partir de atributos ORM."""
        from_attributes = True
