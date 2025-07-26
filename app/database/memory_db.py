from typing import List, Optional
from app.models.item import Item
# TODO: EJERCICIO PARA ESTUDIANTES - Importar ItemUpdate cuando lo creen
# from app.models.item import Item, ItemUpdate

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
# def update_item_by_id(item_id: int, item_update: ItemUpdate) -> Optional[Item]:
#     """Actualizar un item por ID"""
#     # PISTAS:
#     # 1. Recorrer items_db con enumerate() para obtener índice y item
#     # 2. Si item.id == item_id, crear un nuevo Item con los datos actualizados
#     # 3. Reemplazar el item en items_db[idx] = nuevo_item
#     # 4. Retornar el item actualizado
#     # 5. Si no se encuentra, retornar None
#     pass

# TODO: EJERCICIO PARA ESTUDIANTES - Implementar función DELETE
# def delete_item_by_id(item_id: int) -> bool:
#     """Eliminar un item por ID"""
#     # PISTAS:
#     # 1. Usar global items_db
#     # 2. Guardar la longitud original de items_db
#     # 3. Filtrar items_db manteniendo solo los items con id diferente a item_id
#     # 4. Retornar True si se eliminó algo (longitud cambió), False si no
#     pass 