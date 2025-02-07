from fastapi import APIRouter, HTTPException, Depends
import crud.materials
import models.materials
from sqlalchemy.orm import Session
import config.db
import schemas.materials
from typing import List

material = APIRouter()

models.materials.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@material.get("/materials", response_model=List[schemas.materials.Material], tags=["Materiales"])
async def read_materials(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.materials.get_materials(db=db, skip=skip, limit=limit)

@material.get("/materials/{id}", response_model=schemas.materials.Material, tags=["Materiales"])
async def read_material(id: int, db: Session = Depends(get_db)):
    db_material = crud.materials.get_material(db=db, id=id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material

@material.post("/materials", response_model=schemas.materials.Material, tags=["Materiales"])
async def create_material(material_data: schemas.materials.MaterialCreate, db: Session = Depends(get_db)):
    return crud.materials.create_material(db=db, material=material_data)

@material.put("/materials/{id}", response_model=schemas.materials.Material, tags=["Materiales"])
async def update_material(id: int, material_data: schemas.materials.MaterialUpdate, db: Session = Depends(get_db)):
    db_material = crud.materials.update_material(db=db, id=id, material=material_data)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material

@material.delete("/materials/{id}", response_model=schemas.materials.Material, tags=["Materiales"])
async def delete_material(id: int, db: Session = Depends(get_db)):
    db_material = crud.materials.delete_material(db=db, id=id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material
