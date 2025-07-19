from fastapi import FastAPI
from app.api.routes import items

app = FastAPI(
    title="Mini API CRUD",
    description="Una API CRUD simple para gestionar items en memoria",
    version="1.0.0"
)

# Incluir las rutas
app.include_router(items.router, prefix="/api/v1", tags=["items"])

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la Mini API CRUD en memoria"} 