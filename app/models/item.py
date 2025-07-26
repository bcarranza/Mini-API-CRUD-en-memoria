from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    price: float

class ItemCreate(BaseModel):
    name: str
    price: float

# Ejercicio para estudiantes - Implementar el modelo ItemUpdate para operaciones PUT
class ItemUpdate(BaseModel):
    name: str
    price: float