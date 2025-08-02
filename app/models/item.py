from pydantic import BaseModel, Field
from typing import Optional

class Item(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)

class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)

      
# TODO: EJERCICIO PARA ESTUDIANTES
# Crear aquí el modelo ItemUpdate para las operaciones PUT
# Pista: Debe tener los mismos campos que ItemCreate
class ItemUpdate(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)