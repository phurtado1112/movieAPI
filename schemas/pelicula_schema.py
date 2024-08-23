""" Schema de Película """
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

# from models.lenguaje_model import Lenguaje


class PeliculaCreate(BaseModel):
    """
    Esquema de datos para crear una película.

    Atributos:
        titulo (str): El título de la película.
        director (str): El director de la película.
        duracion (int): La duración de la película en minutos.
        genero (str): El género de la película.
        sinopsis (str): Una breve sinopsis de la película.

    """
    titulo: str
    descripcion: str
    anio_publicacion: int
    lenguaje_id: int
    duracion_renta: int = None
    precio_renta: int = None
    duracion: Optional[int] = None
    costo_reemplazo: Optional[float] = None
    clasificacion: Optional[str] = None
    ultima_actualizacion: datetime
    caracteristicas_especiales: Optional[str] = None
    texto_completo: Optional[str] = None

    class Config():
        """
        Configuración para habilitar el modo ORM.
        """
        from_attributes = True


class PeliculaSchema(BaseModel):
    """
    Esquema de datos para una película.

    Atributos:
        titulo (str): El título de la película.
        director (str): El director de la película.
        duracion (int): La duración de la película en minutos.
        genero (str): El género de la película.
        sinopsis (str): Una breve sinopsis de la película.
    """
    titulo: str
    descripcion: str
    anio_publicacion: int
    duracion: int
    clasificacion: str
    lenguaje_id: int
    lenguaje_nombre: str = None

    class Config():
        """
        Configuración para habilitar el modo ORM.
        """
        from_attributes = True


class PeliculaId(BaseModel):
    """
    Esquema de datos para una película en la base de datos.

    Atributos:
        pelicula_id (int): El identificador único de la película.
        lenguaje_id (int): El identificador único del lenguaje de la película.
    """
    pelicula_id: int
    lenguaje_id: int

    class Config():
        """
        Configuración para habilitar el modo ORM.
        """
        from_attributes = True


class PeliculaActulizar(BaseModel):
    """
    Esquema de datos para crear una película.

    Atributos:
        titulo (str): El título de la película.
        director (str): El director de la película.
        duracion (int): La duración de la película en minutos.
        genero (str): El género de la película.
        sinopsis (str): Una breve sinopsis de la película.

    """
    titulo: str = None
    descripcion: str = None
    anio_publicacion: int = None
    lenguaje_id: int = None
    duracion_renta: int = None
    precio_renta: int = None
    duracion: Optional[int] = None
    costo_reemplazo: Optional[float] = None
    clasificacion: Optional[str] = None
    ultima_actualizacion: datetime
    caracteristicas_especiales: Optional[str] = None
    texto_completo: Optional[str] = None

    class Config():
        """
        Configuración para habilitar el modo ORM.
        """
        from_attributes = True
