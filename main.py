""" API de Películas """
from fastapi import FastAPI, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from config.database import get_db
from models.pelicula_model import Pelicula


app = FastAPI()

app.title = "API de Peliculas"
app.version = "0.0.1"

# Montar el directorio static para servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Ruta para servir el favicon.ico


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    """Ruta para servir el favicon.ico"""
    return FileResponse("static/favicon.ico")


@app.get("/", tags=["Home"])
def read_root():
    """Ruta de bienvenida"""
    return "Hello World"


@app.get("/peliculas", tags=["Peliculas"], status_code=200)
def get_peliculas(db: Session = Depends(get_db)):
    """Obtener todas las películas"""
    try:
        result = db.query(Pelicula).all()
        # Convertir los resultados a JSON, manejando errores de decodificación
        json_result = jsonable_encoder(result, custom_encoder={
                                       str: lambda x: x.encode('utf-8', errors='replace').decode('utf-8')})
        return JSONResponse(status_code=200, content=json_result)
    except UnicodeDecodeError as e:
        return JSONResponse(status_code=500, content={"message": "Error de decodificación de caracteres", "error": str(e)})
