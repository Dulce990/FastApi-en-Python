from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.prestamos
import config.db
import schemas.prestamos
import models.prestamos
from typing import List

prestamo = APIRouter()

models.prestamos.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@prestamo.get("/prestamos", response_model=List[schemas.prestamos.Prestamo], tags=["Prestamos"])
async def read_prestamos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.prestamos.get_prestamos(db=db, skip=skip, limit=limit)

@prestamo.get("/prestamos/{id_prestamo}", response_model=schemas.prestamos.Prestamo, tags=["Prestamos"])
async def read_prestamo(id_prestamo: int, db: Session = Depends(get_db)):
    db_prestamo = crud.prestamos.get_prestamo(db=db, id_prestamo=id_prestamo)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo not found")
    return db_prestamo

@prestamo.post("/prestamos", response_model=schemas.prestamos.Prestamo, tags=["Prestamos"])
async def create_prestamo(prestamo_data: schemas.prestamos.PrestamoCreate, db: Session = Depends(get_db)):
    return crud.prestamos.create_prestamo(db=db, prestamo=prestamo_data)

@prestamo.put("/prestamos/{id_prestamo}", response_model=schemas.prestamos.Prestamo, tags=["Prestamos"])
async def update_prestamo(id_prestamo: int, prestamo_data: schemas.prestamos.PrestamoUpdate, db: Session = Depends(get_db)):
    db_prestamo = crud.prestamos.update_prestamo(db=db, id_prestamo=id_prestamo, prestamo=prestamo_data)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo not found")
    return db_prestamo

@prestamo.delete("/prestamos/{id_prestamo}", response_model=schemas.prestamos.Prestamo, tags=["Prestamos"])
async def delete_prestamo(id_prestamo: int, db: Session = Depends(get_db)):
    db_prestamo = crud.prestamos.delete_prestamo(db=db, id_prestamo=id_prestamo)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo not found")
    return db_prestamo
