"""
Módulo CRUD para la gestión de usuarios.

Este módulo proporciona funciones para obtener, crear, actualizar y eliminar registros de usuarios
utilizando SQLAlchemy.
"""

from models.users import User
from schemas.users import UserCreate, UserUpdate
from sqlalchemy.orm import Session

def get_users(db: Session, skip: int = 0, limit: int = 10):
    """Obtiene una lista de usuarios con paginación."""
    return db.query(User).offset(skip).limit(limit).all()

def get_user_by_usuario(db: Session, usuario: str):
    """Obtiene un usuario por su nombre de usuario."""
    return db.query(User).filter(User.nombreUsuario == usuario).first()

def get_user(db: Session, user_id: int):
    """Obtiene un usuario por su ID."""
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate):
    """Crea un nuevo usuario en la base de datos."""
    db_user = User(
        nombre=user.nombre,
        primerApellido=user.primerApellido,
        segundoApellido=user.segundoApellido,
        TipoUsuario=user.TipoUsuario,
        nombreUsuario=user.nombreUsuario,
        correoElectronico=user.correoElectronico,
        contrasena=user.contrasena,
        numeroTelefono=user.numeroTelefono,
        estatus=user.estatus,
        fechaRegistro=user.fechaRegistro,
        fechaActualizacion=user.fechaActualizacion
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: UserUpdate):
    """Actualiza los datos de un usuario existente."""
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        for var, value in vars(user).items():
            if value is not None:
                setattr(db_user, var, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    """Elimina un usuario de la base de datos por su ID."""
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
