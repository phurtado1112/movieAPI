""" Schema de Película """
from pydantic import BaseModel


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
    director: str
    duracion: int
    genero: str
    sinopsis: str

    class ConfigDict:
        """
        Configuración para habilitar el modo ORM.
        """
        orm_mode = True
