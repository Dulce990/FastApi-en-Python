"""
Módulo de configuración de la base de datos para la API CRUD.

Este módulo configura la conexión a la base de datos MySQL utilizando SQLAlchemy.
Define la URL de la base de datos, el motor de conexión y la sesión de base de datos.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:WandaOlsen_96@localhost:3309/base_prueba"

# Creación del motor de base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Configuración de la sesión de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para la definición de modelos
Base = declarative_base()
