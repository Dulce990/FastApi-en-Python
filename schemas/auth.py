from pydantic import BaseModel

class LoginRequest(BaseModel):
    identifier: str  # puede ser nombre de usuario, correo o teléfono
    password: str

