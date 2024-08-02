""" Módulo que define el modelo de lenguaje """

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base


class Lenguaje(Base):
    """
    Clase que representa un lenguaje en la base de datos.

    Atributos:
        lenguaje_id (int): Identificador único del lenguaje.
        nombre (str): Nombre del lenguaje.
    """
    __tablename__ = "lenguajes"

    lenguaje_id = Column(Integer, primary_key=True,
                         index=True, autoincrement=True)
    nombre = Column(String)

    pelicula = relationship("Pelicula", back_populates="lenguaje")

    def __init__(self, nombre):
        self.nombre = nombre
