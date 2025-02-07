"""Este módulo contiene las rutas de la API relacionadas con los materiales."""
from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.materials
import models.materials
import config.db
import schemas.materials

# Módulo para manejar las rutas de los materiales
# Este archivo define las operaciones CRUD para los materiales, incluyendo
# la creación, lectura, actualización y eliminación de registros de materiales.
material = APIRouter()

# Crear las tablas de la base de datos (si no existen)
models.materials.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    """Obtiene la sesión de la base de datos."""
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@material.get("/materials", response_model=List[schemas.materials.Material], tags=["Materiales"])
async def read_materials(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Obtiene una lista de materiales con paginación."""
    return crud.materials.get_materials(db=db, skip=skip, limit=limit)

@material.get("/materials/{material_id}", response_model=schemas.materials.Material,
            tags=["Materiales"])
async def read_material(material_id: int, db: Session = Depends(get_db)):
    """Obtiene un material por su ID."""
    db_material = crud.materials.get_material(db=db, id=material_id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material

@material.post("/materials", response_model=schemas.materials.Material,
            tags=["Materiales"])
async def create_material(material_data: schemas.materials.MaterialCreate,
                        db: Session = Depends(get_db)):
    """Crea un nuevo material."""
    return crud.materials.create_material(db=db, material=material_data)

@material.put("/materials/{material_id}", response_model=schemas.materials.Material,
            tags=["Materiales"])
async def update_material(material_id: int, material_data: schemas.materials.MaterialUpdate,
                        db: Session = Depends(get_db)):
    """Actualiza un material existente."""
    db_material = crud.materials.update_material(db=db, id=material_id,
                                                material=material_data)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material

@material.delete("/materials/{material_id}", response_model=schemas.materials.Material,
                tags=["Materiales"])
async def delete_material(material_id: int, db: Session = Depends(get_db)):
    """Elimina un material por su ID."""
    db_material = crud.materials.delete_material(db=db, id=material_id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material
