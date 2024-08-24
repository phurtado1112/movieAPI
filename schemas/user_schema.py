""" Schema de Usuario """
from pydantic import BaseModel


class UserCreate(BaseModel):
    """
    Esquema de datos para crear un usuario.

    Atributos:
        nombre (str): Nombre del usuario.
        apellido (str): Apellido del usuario.
        email (str): Correo electrónico del usuario.
        password (str): Contraseña del usuario.
    """
    nombre: str
    apellido: str
    email: str
    password: str

    class Config():
        """
        Configuración para habilitar el modo ORM.
        """
        from_attributes = True


class UserLogin(BaseModel):
    """
    Esquema de datos para iniciar sesión.

    Atributos:
        email (str): Correo electrónico del usuario.
        password (str): Contraseña del usuario.
    """
    email: str
    password: str

    class Config():
        """
        Configuración para habilitar el modo ORM.
        """
        from_attributes = True
