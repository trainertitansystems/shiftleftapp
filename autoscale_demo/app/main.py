from fastapi import FastAPI
from .db import get_data

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"data": get_data()}

