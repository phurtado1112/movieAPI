""" Módulo que define el modelo de Actor. """
from sqlalchemy import Column, Integer, String
from config.database import Base


class Actor(Base):
    """
    Clase que representa un actor en la base de datos.

    Atributos:
        actor_id (int): Identificador único del actor.
        nombre (str): Nombre del actor.
        apellido (str): Apellido del actor.
        fecha_nacimiento (str): Fecha de nacimiento del actor.
    """
    __tablename__ = "actores"

    actor_id = Column(Integer, primary_key=True,
                      index=True, autoincrement=True)
    nombre = Column(String)
    apellido = Column(String)

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
