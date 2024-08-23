""""Módulo que define el modelo de la entidad Pelicula."""
from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey

from config.database import Base
from models.lenguaje_model import Lenguaje


class Pelicula(Base):  # pylint: disable=too-few-public-methods
    """
    Clase que representa una película en la base de datos.

    Atributos:
        pelicula_id (int): Identificador único de la película.
        titulo (str): Título de la película.
        descripcion (str): Descripción de la película.
        anio_publicacion (int): Año de publicación de la película.
    """
    __tablename__ = "peliculas"

    pelicula_id = Column(Integer, primary_key=True,
                         index=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    anio_publicacion = Column(Integer, nullable=False)
    lenguaje_id = Column(Integer, ForeignKey(
        "lenguajes.lenguaje_id", ondelete="CASCADE"), nullable=False)
    lenguaje = relationship("Lenguaje", back_populates="peliculas")

    duracion_renta = Column(Integer, nullable=True)
    precio_renta = Column(Integer, nullable=True)
    duracion = Column(Integer, nullable=True)
    costo_reemplazo = Column(Float, nullable=True)
    clasificacion = Column(String, nullable=True)
    ultima_actualizacion = Column(
        DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())
    caracteristicas_espciales = Column(String, nullable=True)
    texto_completo = Column(String, nullable=True)

    def __init__(self, titulo, descripcion, anio_publicacion, lenguaje_id, duracion_renta, precio_renta, duracion, costo_reemplazo, clasificacion, ultima_actualizacion, caracteristicas_especiales, texto_completo):  # pylint: disable=too-many-arguments
        self.titulo = titulo
        self.descripcion = descripcion
        self.anio_publicacion = anio_publicacion
        self.lenguaje_id = lenguaje_id
        self.duracion_renta = duracion_renta
        self.precio_renta = precio_renta
        self.duracion = duracion
        self.costo_reemplazo = costo_reemplazo
        self.clasificacion = clasificacion
        self.ultima_actualizacion = ultima_actualizacion
        self.caracteristicas_especiales = caracteristicas_especiales
        self.texto_completo = texto_completo
