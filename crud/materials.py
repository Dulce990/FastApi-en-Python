"""
Módulo de operaciones CRUD para materiales.

Este módulo proporciona funciones para obtener, crear, actualizar y eliminar registros de materiales
en la base de datos utilizando SQLAlchemy.
"""

from sqlalchemy.orm import Session
from models.materials import Material
from schemas.materials import MaterialCreate, MaterialUpdate

def get_materials(db: Session, skip: int = 0, limit: int = 10):
    """Obtiene una lista de materiales con paginación."""
    return db.query(Material).offset(skip).limit(limit).all()

def get_material(db: Session, material_id: int):
    """Obtiene un material por su ID."""
    return db.query(Material).filter(Material.id == material_id).first()

def create_material(db: Session, material: MaterialCreate):
    """Crea un nuevo material en la base de datos."""
    db_material = Material(
        TipoMaterial=material.TipoMaterial,
        Marca=material.Marca,
        Modelo=material.Modelo,
        Estado=material.Estado
    )
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

def update_material(db: Session, material_id: int, material: MaterialUpdate):
    """Actualiza los datos de un material existente."""
    db_material = db.query(Material).filter(Material.id == material_id).first()
    if db_material:
        for var, value in vars(material).items():
            if value is not None:
                setattr(db_material, var, value)
        db.commit()
        db.refresh(db_material)
    return db_material

def delete_material(db: Session, material_id: int):
    """Elimina un material de la base de datos por su ID."""
    db_material = db.query(Material).filter(Material.id == material_id).first()
    if db_material:
        db.delete(db_material)
        db.commit()
    return db_material
