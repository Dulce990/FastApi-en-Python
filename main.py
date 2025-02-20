"""Módulo principal de la API para PRESTAMOS S.A. de C.V.
Este módulo configura la aplicación FastAPI y registra los routers.
"""

from fastapi import FastAPI
from routes.users import user_router
from routes.materials import material
from routes.prestamos import prestamo
from routes.auth import router as auth

app = FastAPI(
    title="PRESTAMOS S.A. de C.V.",
    description="API de prueba para almacenar registros de prestamo de material educativo"
)

app.include_router(user_router)
app.include_router(material)
app.include_router(prestamo)
app.include_router(auth, prefix="/auth")  # lo agrupa bajo /auth