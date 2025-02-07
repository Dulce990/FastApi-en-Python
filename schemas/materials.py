from pydantic import BaseModel

class MaterialBase(BaseModel):
    TipoMaterial: str
    Marca: str  
    Modelo: str
    Estado: str  

class MaterialCreate(MaterialBase):
    pass

class MaterialUpdate(MaterialBase):
    pass

class Material(MaterialBase):
    id: int
    class Config:
        from_attributes = True
