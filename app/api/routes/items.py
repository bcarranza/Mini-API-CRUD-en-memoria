from fastapi import APIRouter, HTTPException
from typing import List
from app.models.item import Item, ItemCreate
# TODO: EJERCICIO PARA ESTUDIANTES - Importar ItemUpdate cuando lo creen
from app.models.item import Item, ItemCreate, ItemUpdate

from app.database.memory_db import get_items_db, add_item, get_item_by_id
# TODO: EJERCICIO PARA ESTUDIANTES - Importar las funciones cuando las implementen
from app.database.memory_db import get_items_db, add_item, get_item_by_id, update_item_by_id, delete_item_by_id

router = APIRouter()

@router.post("/items/", response_model=Item, status_code=201)
def create_item(item: ItemCreate):
    """Crear un nuevo item"""
    new_item = Item(name=item.name, price=item.price)
    created_item = add_item(new_item)
    return created_item

@router.get("/items/", response_model=List[Item])
def read_items():
    """Obtener todos los items"""
    return get_items_db()

@router.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    """Obtener un item por ID"""
    item = get_item_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# TODO: EJERCICIO PARA ESTUDIANTES - Implementar endpoint PUT
@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemUpdate):
    """Actualizar un item por ID"""
    updated_item = update_item_by_id(item_id, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

# TODO: EJERCICIO PARA ESTUDIANTES - Implementar endpoint DELETE
@router.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    """Eliminar un item por ID"""
    success = delete_item_by_id(item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found") 