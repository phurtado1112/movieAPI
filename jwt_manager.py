'''======================= Cración del Token ============================='''

from jwt import encode


def create_jwt(payload: dict, secret: any) -> str:
    '''====== Función de Creación del Token ====='''
    token: str = encode(payload, secret, algorithm='HS256')
    return token
