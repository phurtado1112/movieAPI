""" API de Películas """
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from config.database import get_db
from models.pelicula_model import Pelicula
from schemas.pelicula_schema import PeliculaSchema, PeliculaCreate, PeliculaActulizar

app = FastAPI()

app.title = "API de Peliculas"
app.description = "API de Peliculas para la gestión de películas de una tienda de alquiler"
app.version = "0.1.0"

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
    return "Bienvenido a la API de Películas"


@app.get("/peliculas", response_model=List[PeliculaSchema], tags=["Peliculas"], status_code=200)
def get_peliculas(db: Session = Depends(get_db)):
    """Obtener todas las películas"""
    try:
        peliculas = db.query(Pelicula).all()
        peliculas_data = []

        for pelicula in peliculas:
            lenguaje_nombre = pelicula.lenguaje.nombre if pelicula.lenguaje else None
            pelicula_data = {
                "titulo": pelicula.titulo,
                "descripcion": pelicula.descripcion,
                "anio_publicacion": pelicula.anio_publicacion,
                "duracion": pelicula.duracion,
                "clasificacion": pelicula.clasificacion,
                "lenguaje_id": pelicula.lenguaje_id,
                "lenguaje_nombre": lenguaje_nombre
            }
            peliculas_data.append(pelicula_data)

        return peliculas_data

    except UnicodeDecodeError as e:
        return JSONResponse(status_code=500, content={"message": "Error de decodificación de caracteres", "error": str(e)})


@app.get("/peliculas/{pelicula_id}", response_model=PeliculaSchema, tags=["Peliculas"], status_code=200)
def get_pelicula(pelicula_id: int, db: Session = Depends(get_db)):
    """Obtener una película por su ID"""
    try:
        pelicula = db.query(Pelicula).filter(
            Pelicula.pelicula_id == pelicula_id).first()
        if not pelicula:
            raise HTTPException(
                status_code=404, detail="Película no encontrada")

        lenguaje_nombre = pelicula.lenguaje.nombre if pelicula.lenguaje else None

        pelicula_data = {
            "titulo": pelicula.titulo,
            "descripcion": pelicula.descripcion,
            "anio_publicacion": pelicula.anio_publicacion,
            "duracion": pelicula.duracion,
            "clasificacion": pelicula.clasificacion,
            "lenguaje_id": pelicula.lenguaje_id,
            "lenguaje_nombre": lenguaje_nombre
        }

        return PeliculaSchema(**pelicula_data)
    except UnicodeDecodeError as e:
        return JSONResponse(status_code=500, content={"message": "Error de decodificación de caracteres", "error": str(e)})


@app.post("/peliculas", response_model=PeliculaCreate, tags=["Peliculas"], status_code=201)
def create_pelicula(pelicula: PeliculaCreate, db: Session = Depends(get_db)):
    """Crear una nueva película"""
    try:
        agregar_pelicula = Pelicula(
            **pelicula.model_dump()
        )
        db.add(agregar_pelicula)
        db.commit()
        db.refresh(agregar_pelicula)
        return agregar_pelicula
    except UnicodeDecodeError as e:
        return JSONResponse(status_code=500, content={"message": "Error de decodificación de caracteres", "error": str(e)})


@app.put("/peliculas/{pelicula_id}", response_model=PeliculaActulizar, tags=["Peliculas"], status_code=200)
def update_pelicula(pelicula_id: int, pelicula: PeliculaActulizar, db: Session = Depends(get_db)):
    """Actualizar una película"""
    try:
        pelicula_actualizada = db.query(Pelicula).filter(
            Pelicula.pelicula_id == pelicula_id).first()
        pelicula_actualizada.titulo = pelicula.titulo
        pelicula_actualizada.descripcion = pelicula.descripcion
        pelicula_actualizada.anio_publicacion = pelicula.anio_publicacion
        pelicula_actualizada.lenguaje_id = pelicula.lenguaje_id
        pelicula_actualizada.duracion_renta = pelicula.duracion_renta
        pelicula_actualizada.precio_renta = pelicula.precio_renta
        pelicula_actualizada.duracion = pelicula.duracion
        pelicula_actualizada.costo_reemplazo = pelicula.costo_reemplazo
        pelicula_actualizada.clasificacion = pelicula.clasificacion
        pelicula_actualizada.ultima_actualizacion = pelicula.ultima_actualizacion
        pelicula_actualizada.caracteristicas_especiales = pelicula.caracteristicas_especiales
        pelicula_actualizada.texto_completo = pelicula.texto_completo
        db.commit()
        db.refresh(pelicula_actualizada)
        return pelicula_actualizada
    except UnicodeDecodeError as e:
        return JSONResponse(status_code=500, content={"message": "Error de decodificación de caracteres", "error": str(e)})


@app.delete("/peliculas/{pelicula_id}", tags=["Peliculas"], status_code=204)
def delete_pelicula(pelicula_id: int, db: Session = Depends(get_db)):
    """Eliminar una película"""
    try:
        db.query(Pelicula).filter(Pelicula.pelicula_id ==
                                  pelicula_id).delete(synchronize_session=False)
        db.commit()
        return JSONResponse(status_code=204, content={"message": "Película eliminada"})
    except UnicodeDecodeError as e:
        return JSONResponse(status_code=500, content={"message": "Error de decodificación de caracteres", "error": str(e)})


# @app.get("/peliculas/{pelicula_id}/lenguaje", response_model=PeliculaSchema, tags=["Peliculas"], status_code=200)
# def get_lenguaje(pelicula_id: int, db: Session = Depends(get_db)):
#     """Obtener el lenguaje de una película por su ID"""
#     try:
#         pelicula = db.query(Pelicula).filter(
#             Pelicula.pelicula_id == pelicula_id).first()
#         return pelicula.lenguaje
#     except UnicodeDecodeError as e:
#         return JSONResponse(status_code=500, content={"message": "Error de decodificación de caracteres", "error": str(e)})

@app.get("/peliculas/{pelicula_id}/lenguaje", tags=["Peliculas"], status_code=200)
def get_lenguaje(pelicula_id: int, db: Session = Depends(get_db)):
    """Obtener el lenguaje de una película por su ID"""
    try:
        pelicula = db.query(Pelicula).filter(
            Pelicula.pelicula_id == pelicula_id).first()
        return pelicula.lenguaje
    except UnicodeDecodeError as e:
        return JSONResponse(status_code=500, content={"message": "Error de decodificación de caracteres", "error": str(e)})


@app.patch("/peliculas/{pelicula_id}", response_model=PeliculaActulizar, tags=["Peliculas"], status_code=200)
def update_parcial_pelicula(pelicula_id: int, pelicula: PeliculaActulizar, db: Session = Depends(get_db)):
    """Actualizar una película"""
    try:
        pelicula_actualizada = db.query(Pelicula).filter(
            Pelicula.pelicula_id == pelicula_id).first()
        pelicula_actualizada.titulo = pelicula.titulo
        pelicula_actualizada.descripcion = pelicula.descripcion
        pelicula_actualizada.anio_publicacion = pelicula.anio_publicacion
        pelicula_actualizada.lenguaje_id = pelicula.lenguaje_id
        pelicula_actualizada.duracion_renta = pelicula.duracion_renta
        pelicula_actualizada.precio_renta = pelicula.precio_renta
        pelicula_actualizada.duracion = pelicula.duracion
        pelicula_actualizada.costo_reemplazo = pelicula.costo_reemplazo
        pelicula_actualizada.clasificacion = pelicula.clasificacion
        pelicula_actualizada.ultima_actualizacion = pelicula.ultima_actualizacion
        pelicula_actualizada.caracteristicas_especiales = pelicula.caracteristicas_especiales
        pelicula_actualizada.texto_completo = pelicula.texto_completo
        db.commit()
        db.refresh(pelicula_actualizada)
        return pelicula_actualizada
    except UnicodeDecodeError as e:
        return JSONResponse(status_code=500, content={"message": "Error de decodificación de caracteres", "error": str(e)})
