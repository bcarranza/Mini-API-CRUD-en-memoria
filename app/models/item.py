from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    price: float

class ItemCreate(BaseModel):
    name: str
    price: float

# TODO: EJERCICIO PARA ESTUDIANTES
# Crear aquí el modelo ItemUpdate para las operaciones PUT
# Pista: Debe tener los mismos campos que ItemCreate
class ItemUpdate(BaseModel):
    name: str
    price: float 