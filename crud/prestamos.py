import models.prestamos
import schemas.prestamos
from sqlalchemy.orm import Session

def get_prestamos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.prestamos.Prestamo).offset(skip).limit(limit).all()

def get_prestamo(db: Session, id_prestamo: int):
    return db.query(models.prestamos.Prestamo).filter(models.prestamos.Prestamo.id_prestamo == id_prestamo).first()

def create_prestamo(db: Session, prestamo: schemas.prestamos.PrestamoCreate):
    db_prestamo = models.prestamos.Prestamo(
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

def update_prestamo(db: Session, id_prestamo: int, prestamo: schemas.prestamos.PrestamoUpdate):
    db_prestamo = db.query(models.prestamos.Prestamo).filter(models.prestamos.Prestamo.id_prestamo == id_prestamo).first()
    if db_prestamo:
        for var, value in vars(prestamo).items():
            setattr(db_prestamo, var, value) if value is not None else None
        db.commit()
        db.refresh(db_prestamo)
    return db_prestamo

def delete_prestamo(db: Session, id_prestamo: int):
    db_prestamo = db.query(models.prestamos.Prestamo).filter(models.prestamos.Prestamo.id_prestamo == id_prestamo).first()
    if db_prestamo:
        db.delete(db_prestamo)
        db.commit()
    return db_prestamo
