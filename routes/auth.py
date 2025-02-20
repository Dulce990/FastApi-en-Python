from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jose import jwt  # se utiliza para generar el token
from schemas.auth import LoginRequest
from pydantic import BaseModel
import crud.users
import models.users
import config.db

# Configuración del token
SECRET_KEY = "UTXJ12345678910"  
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter()

class Token(BaseModel):
    access_token: str
    token_type: str

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login", response_model=Token, tags=["Autenticación"])
def login(auth: LoginRequest, db: Session = Depends(get_db)):
    # Buscar el usuario donde el identificador coincida con nombre de usuario, correo o teléfono
    user = db.query(models.users.User).filter(
        (models.users.User.nombreUsuario == auth.identifier) |
        (models.users.User.correoElectronico == auth.identifier) |
        (models.users.User.numeroTelefono == auth.identifier)
    ).first()

    if not user:
        raise HTTPException(status_code=400, detail="Credenciales inválidas")
    
    # Para fines de este ejemplo se compara la contraseña en texto plano.
    # En producción, utiliza contraseñas hasheadas y la verificación correspondiente.
    if user.contrasena != auth.password:
        raise HTTPException(status_code=400, detail="Credenciales inválidas")
    
    # Crear el token
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token_payload = {
        "sub": str(user.id),
        "exp": expire
    }
    token = jwt.encode(token_payload, SECRET_KEY, algorithm=ALGORITHM)
    
    return {"access_token": token, "token_type": "bearer"}
