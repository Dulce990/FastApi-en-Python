"""
Módulo de operaciones CRUD para préstamos.

Este módulo proporciona funciones para obtener, crear, actualizar y eliminar registros de préstamos
en la base de datos utilizando SQLAlchemy.
"""

from sqlalchemy.orm import Session
from models.prestamos import Prestamo
from schemas.prestamos import PrestamoCreate, PrestamoUpdate

def get_prestamos(db: Session, skip: int = 0, limit: int = 10):
    """Obtiene una lista de préstamos con paginación."""
    return db.query(Prestamo).offset(skip).limit(limit).all()

def get_prestamo(db: Session, id_prestamo: int):
    """Obtiene un préstamo por su ID."""
    return db.query(Prestamo).filter(Prestamo.id_prestamo == id_prestamo).first()

def create_prestamo(db: Session, prestamo: PrestamoCreate):
    """Crea un nuevo préstamo en la base de datos."""
    db_prestamo = Prestamo(
        id_usuario=prestamo.id_usuario,
        id_material=prestamo.id_material,
        fecha_prestamo=prestamo.fecha_prestamo,
        fecha_devolucion=prestamo.fecha_devolucion,
        estatus=prestamo.estatus
    )
    db.add(db_prestamo)
    db.commit()
    db.refresh(db_prestamo)
    return db_prestamo

def update_prestamo(db: Session, id_prestamo: int, prestamo: PrestamoUpdate):
    """Actualiza los datos de un préstamo existente."""
    db_prestamo = db.query(Prestamo).filter(Prestamo.id_prestamo == id_prestamo).first()
    if db_prestamo:
        for var, value in vars(prestamo).items():
            if value is not None:
                setattr(db_prestamo, var, value)
        db.commit()
        db.refresh(db_prestamo)
    return db_prestamo

def delete_prestamo(db: Session, id_prestamo: int):
    """Elimina un préstamo de la base de datos por su ID."""
    db_prestamo = db.query(Prestamo).filter(Prestamo.id_prestamo == id_prestamo).first()
    if db_prestamo:
        db.delete(db_prestamo)
        db.commit()
    return db_prestamo
