from fastapi import FastAPI
from pydantic import BaseModel, ValidationError
from starlette.middleware.cors import CORSMiddleware

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

class Retry(BaseModel):
    retry: bool

class FetchDB():
    fetch: bool


@app.get("/")
def read_root():
    return { 'message': "que heces bobo" }

@app.post("/adivinar")
def adivinar(data: Adivinanza):
    return data

@app.post("/retry")
def retry(data: retry):
    return