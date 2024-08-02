from fastapi import FastAPI
from pydantic import BaseModel, ValidationError

app = FastAPI()

@app.get("/")
def read_root():
    return { message: "root" }


