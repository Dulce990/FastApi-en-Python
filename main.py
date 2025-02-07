from fastapi import FastAPI
from routes.users import user
from routes.materials import material
from routes.prestamos import prestamo

app = FastAPI(
    title="PRESTAMOS S.A. de C.V.",
    description="API de prueba para almacenar registros de prestamo de material educativo"
)

app.include_router(user)
app.include_router(material)
app.include_router(prestamo)