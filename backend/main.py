from fastapi import FastAPI
from pydantic import BaseModel, ValidationError
from starlette.middleware.cors import CORSMiddleware
from adivinarService import Sadivinar

adivinarClass = Sadivinar()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes especificar dominios específicos si es necesario
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Adivinanza(BaseModel):
    numero: int


@app.get("/")
def read_root():
    return { 'message': "que heces bobo" }

@app.post("/check")
def check():
    adivinarClass.setNumber()
    return { 'ok': True }
    

@app.post("/adivinar")
def adivinar(data: Adivinanza):
    res = adivinarClass.compareNumbers(data.numero)
    return {
        "numberfinded": res.get('finded'),
        "attempts": adivinarClass.intentos,
        "feedback": res.get('feedback'),
    }

@app.post("/retry")
def retry():
    adivinarClass.setNumber()
    return { 'ok': True }