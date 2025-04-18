from fastapi import FastAPI
from .core.config import settings

app = FastAPI(title="Ledgrithm")

@app.get("/health")
async def health_check():
    return {"status": "ok", "db": settings.DATABASE_URL}
