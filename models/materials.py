from sqlalchemy import Column, Integer, String, Enum
from config.db import Base
import enum

class TipoMaterial(str, enum.Enum):
    Cañón = "Cañon"
    Computadora = "Computadora"
    Extensión = "Extensión"
        
class Estatus(str, enum.Enum):
    Disponible = "Disponible"
    Prestado = "Prestado"
    En_Mantenimiento = "En Mantenimiento"

class Material(Base):
    __tablename__ = "tbb_Material"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    TipoMaterial = Column(Enum(TipoMaterial))
    Marca = Column(String(60))  
    Modelo = Column(String(100))  
    Estado = Column(Enum(Estatus))  
