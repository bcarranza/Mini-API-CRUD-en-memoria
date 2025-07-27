from typing import List, Optional
from app.models.item import Item
from app.models.item import Item, ItemUpdate

# Base de datos en memoria
items_db: List[Item] = []

def get_items_db() -> List[Item]:
    """Obtener todos los items de la base de datos en memoria"""
    return items_db

def add_item(item: Item) -> Item:
    """Agregar un nuevo item a la base de datos en memoria"""
    item.id = len(items_db) + 1
    items_db.append(item)
    return item

def get_item_by_id(item_id: int) -> Optional[Item]:
    """Obtener un item por ID"""
    for item in items_db:
        if item.id == item_id:
            return item
    return None

# TODO: EJERCICIO PARA ESTUDIANTES - Implementar función UPDATE
def update_item_by_id(item_id: int, item_update: ItemUpdate) -> Optional[Item]:
    """Actualizar un item por ID"""
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            updated_item = Item(id=item.id, name=item_update.name, price=item_update.price)
            items_db[idx] = updated_item
            return updated_item 
    return None

# TODO: EJERCICIO PARA ESTUDIANTES - Implementar función DELETE
def delete_item_by_id(item_id: int) -> bool:
    """Eliminar un item por ID"""
    global items_db
    original_len = len(items_db)
    items_db = [item for item in items_db if item.id != item_id]
    return len(items_db) < original_len  