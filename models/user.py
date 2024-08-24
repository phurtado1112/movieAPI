'''======================= Clase de Modelo de Usuarios ============================='''

from sqlalchemy import Column, Integer, String
from config.database import Base


class User(Base):
    """
    Clase que representa un usuario en la base de datos.

    Atributos:
        user_id (int): Identificador único del usuario.
        nombre (str): Nombre del usuario.
        apellido (str): Apellido del usuario.
        email (str): Correo electrónico del usuario.
        password (str): Contraseña del usuario.
    """
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True,
                     index=True, autoincrement=True)
    nombre = Column(String)
    apellido = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
