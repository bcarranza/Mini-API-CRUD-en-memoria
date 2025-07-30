from pydantic import BaseModel, Field
from typing import Optional

class Item(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)

class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)

class ItemUpdate(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)

