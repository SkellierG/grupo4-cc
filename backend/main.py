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

class FormData(BaseModel):
    numero: int


@app.get("/")
def read_root():
    return { 'message': "root" }

@app.post("/adivinar")
def adivinar(data: FormData):
    return { 'status': "success",
             'data': data }
