from pydantic import BaseModel, Field
from typing import Optional

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    price: float = Field(..., gt=0) # gt=0 asegura que el precio sea mayor que 0

class ItemCreate(BaseModel):
    name: str
    price: float = Field(..., gt=0)

# TODO: EJERCICIO PARA ESTUDIANTES
# Crear aquí el modelo ItemUpdate para las operaciones PUT
# Pista: Debe tener los mismos campos que ItemCreate
class ItemUpdate(BaseModel):
    name: str
    price: float = Field(..., gt=0)