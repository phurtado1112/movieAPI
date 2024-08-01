"""Configuración de la base de datos"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "postgresql://movieapi:Moap2024!@localhost:5432/peliculas"
DATABASE_URL = "mysql+pymysql://movieapi:Moap2024!@localhost:3306/peliculas"

# Crear un motor y una sesión de base de datos
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependencia para obtener una sesión de base de datos


def get_db():
    """Obtener una sesión de base de datos"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()
