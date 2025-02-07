"""Este módulo contiene las rutas de la API relacionadas con los usuarios."""

from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.users
import config.db
import schemas.users
import models.users

# Definir el enrutador para las rutas de usuarios
user_router = APIRouter()

# Crear las tablas de la base de datos si no existen
models.users.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    """Obtiene la sesión de la base de datos."""
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user_router.get("/users", response_model=List[schemas.users.User], tags=["Usuarios"])
async def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Obtiene una lista de usuarios."""
    return crud.users.get_users(db=db, skip=skip, limit=limit)

@user_router.get("/users/{user_id}", response_model=schemas.users.User, tags=["Usuarios"])
async def read_user(user_id: int, db: Session = Depends(get_db)):
    """Obtiene un usuario por su ID."""
    db_user = crud.users.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user_router.post("/users", response_model=schemas.users.User, tags=["Usuarios"])
async def create_user(user_data: schemas.users.UserCreate, db: Session = Depends(get_db)):
    """Crea un nuevo usuario."""
    return crud.users.create_user(db=db, user=user_data)

@user_router.put("/users/{user_id}", response_model=schemas.users.User, tags=["Usuarios"])
async def update_user(user_id: int, user_data: schemas.users.UserUpdate, db: Session = Depends(get_db)):
    """Actualiza un usuario existente."""
    db_user = crud.users.update_user(db=db, user_id=user_id, user=user_data)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user_router.delete("/users/{user_id}", response_model=schemas.users.User, tags=["Usuarios"])
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Elimina un usuario por su ID."""
    db_user = crud.users.delete_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
