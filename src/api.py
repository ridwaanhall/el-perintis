"""
API sederhana untuk generate narasi perjuangan
"""
from fastapi import FastAPI
from pydantic import BaseModel
from src.perjuangan import narasi_perjuangan

app = FastAPI()

class NarasiRequest(BaseModel):
    nama: str
    tipe: str

@app.post("/narasi")
def generate_narasi(req: NarasiRequest):
    return {"narasi": narasi_perjuangan(req.nama, req.tipe)}
