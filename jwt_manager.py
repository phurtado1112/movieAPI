'''======================= Cración del Token ============================='''

from fastapi.responses import JSONResponse
from jwt import decode, encode


def create_jwt(payload: dict, secret: any) -> str:
    '''====== Función de Creación del Token ====='''
    token: str = encode(payload, secret, algorithm='HS256')
    return token


def validate_jwt(token: str, secret: any) -> dict:
    '''====== Función de Validación del Token ====='''
    try:
        payload: dict = decode(token, secret, algorithms=['HS256'])
        return payload
    except UnicodeDecodeError as e:
        return JSONResponse(status_code=500, content={
            "message": "Error de decodificación de caracteres", "error": str(e)})
