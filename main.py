from fastapi import FastAPI
from typing import Union
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from pydantic import BaseModel

app = FastAPI()

app.title = "Movie API"
app.version = "0.0.1"

SQLALCHEMY_DATABASE_URL = "postgresql://movieapi:Moap2024!@localhost:/movies"

Base = declarative_base()

class Movie(Base):
    __tablename__ = "peliculas"

    pelicula_id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descripcion = Column(String)
    anio_publicacion = Column(Integer)

@app.get("/", tags=["Home"])
def read_root():
    return {"Hello": "World"}

@app.get("/movies/{movie_id}", tags=["Movies"])
def read_movie(movie_id: int):
    return {"movie_id": movie_id}