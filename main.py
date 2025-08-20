from fastapi import FastAPI, Query

PERSONAS = [
    {"nombre": "Ana", "documento": "123"},
    {"nombre": "Carlos", "documento": "456"},
    {"nombre": "Lucía", "documento": "789"}
]


app = FastAPI()


@app.get("/search")
async def search(term: str = Query("", alias="term")):
    resultados = [
        p for p in PERSONAS
        if term in p["nombre"] or term in p["documento"]
    ]
    return resultados
