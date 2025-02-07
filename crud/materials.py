import models.materials
import schemas.materials
from sqlalchemy.orm import Session

def get_materials(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.materials.Material).offset(skip).limit(limit).all()

def get_material(db: Session, id: int):
    return db.query(models.materials.Material).filter(models.materials.Material.id == id).first()

def create_material(db: Session, material: schemas.materials.MaterialCreate):
    db_material = models.materials.Material(
        TipoMaterial=material.TipoMaterial,
        Marca=material.Marca,  
        Modelo=material.Modelo,
        Estado=material.Estado
    )
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

def update_material(db: Session, id: int, material: schemas.materials.MaterialUpdate):
    db_material = db.query(models.materials.Material).filter(models.materials.Material.id == id).first()
    if db_material:
        for var, value in vars(material).items():
            if value is not None:
                setattr(db_material, var, value)
        db.commit()
        db.refresh(db_material)
    return db_material

def delete_material(db: Session, id: int):
    db_material = db.query(models.materials.Material).filter(models.materials.Material.id == id).first()
    if db_material:
        db.delete(db_material)
        db.commit()
    return db_material
