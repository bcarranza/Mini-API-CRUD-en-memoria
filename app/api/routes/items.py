from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from app.schemas import Item, ItemCreate, ItemUpdate
from app.database.db import get_db
from app.database import crud

router = APIRouter()

@router.post("/items/", response_model=Item, status_code=201)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    """Crear un nuevo item"""
    return crud.create_item(db=db, item=item)

@router.get("/items/", response_model=List[Item])
def read_items(db: Session = Depends(get_db)):
    """Obtener todos los items"""
    return crud.get_items(db=db)

@router.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    """Obtener un item por ID"""
    item = crud.get_item_by_id(db=db, item_id=item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    """Actualizar un item por ID"""
    updated_item = crud.update_item(db=db, item_id=item_id, item=item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@router.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    """Eliminar un item por ID"""
    success = crud.delete_item(db=db, item_id=item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found") 