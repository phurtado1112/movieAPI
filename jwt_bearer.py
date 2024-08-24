''' clase de BearerToken '''
from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from jwt_manager import validate_jwt


class JWTBearer(HTTPBearer):
    """Class JWTBearer para validar el token JWT"""

    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_jwt(auth.credentials, "secret")
        if data['email'] != 'phurtado1112@gmail.com':
            raise HTTPException(status_code=403, detail="Token inválido")
    # def __init__(self, token: str = Depends(oauth2_scheme)):
    #     self.token = token

    # def __call__(self, db: Session = Depends(get_db)):
    #     try:
    #         payload = jwt.decode(self.token, SECRET_KEY, algorithms=[ALGORITHM])
    #         username: str = payload.get("sub")
    #         if username is None:
    #             raise HTTPException(status_code=403, detail="Token inválido")
    #         return username
    #     except JWTError:
    #         raise HTTPException(status_code=403, detail="Token inválido")
