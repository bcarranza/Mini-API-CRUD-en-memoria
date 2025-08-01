from pydantic import BaseModel, Field
from typing import Optional

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    price: float = Field(..., gt=0)  # gt=0 significa "greater than 0"

class ItemCreate(BaseModel):
    name: str
    price: float = Field(..., gt=0)

# TODO: EJERCICIO PARA ESTUDIANTES
# Crear aquí el modelo ItemUpdate para las operaciones PUT
# Pista: Debe tener los mismos campos que ItemCreate
class ItemUpdate(BaseModel):
    name: str
feature/test-homework
    price: float = Field(..., gt=0)
    price: float 
 
