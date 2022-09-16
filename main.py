from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, schemas, models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

@app.get("/")
async def root():

    return 'Año con más carreras 2021, Piloto con mayor cantidad de primeros puestos Lewis Hamilton, Nombre del circuito más corrido Autodromo Nazionale Di Monza, Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British Lewis Hamilton'

    
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/Año con mas Carreras/')
async def root():
    AñoANS = '2021, con 23 Carreras'
    return AñoANS



@app.get('/Piloto con mayor cantidad de primeros puestos/')
async def root():
    PilotoANS = 'Lewis Hamilton tras haber obtenido 95 veces el primer lugar'
    return PilotoANS


@app.get('/Nombre del circuito más corrido/')
async def root():
    CircuitoANS = 'Autodromo Nazionale Di Monza tras haber sido lugar de carreras 71 veces'
    return CircuitoANS


@app.get('/Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British/')
async def root():
    PilotoScoreANS = 'Lewis Hamilton es el piloto con mayor puntaje obteniendo 3778 puntos con su maquinaria McLaren de origen Inglés'
    return PilotoScoreANS