""""Módulo que define el modelo de la entidad Pelicula."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base


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
    titulo = Column(String)
    descripcion = Column(String)
    anio_publicacion = Column(Integer)
    # lenguaje_id = Column(Integer, ForeignKey("lenguajes.lenguaje_id"))

    # lenguaje = relationship("lenguaje", back_populates="peliculas")

    def __init__(self, titulo, descripcion, anio_publicacion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.anio_publicacion = anio_publicacion
        # self.lenguaje_id = lenguaje_id
