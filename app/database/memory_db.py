from typing import List, Optional
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

def update_item_by_id(item_id: int, item_update: ItemUpdate) -> Optional[Item]:
    """Actualizar un item por ID"""
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            # Crear un nuevo Item con los datos actualizados
            updated_item = Item(
                id=item_id,
                name=item_update.name,
                price=item_update.price
            )
            # Reemplazar el item en la base de datos
            items_db[idx] = updated_item
            return updated_item
    return None

def delete_item_by_id(item_id: int) -> bool:
    """Eliminar un item por ID"""
    global items_db
    # Guardar la longitud original de items_db
    original_length = len(items_db)
    # Filtrar items_db manteniendo solo los items con id diferente a item_id
    items_db = [item for item in items_db if item.id != item_id]
    # Retornar True si se eliminó algo (longitud cambió), False si no
    return len(items_db) < original_length 