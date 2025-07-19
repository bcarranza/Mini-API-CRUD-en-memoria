# 🎯 Ejercicio para Estudiantes: Implementar PUT y DELETE

## 📋 Objetivo
Completar la API CRUD implementando las operaciones **UPDATE (PUT)** y **DELETE** que actualmente están comentadas.

## 🔍 Estado Actual
La API tiene implementados:
- ✅ POST `/api/v1/items/` (Crear)
- ✅ GET `/api/v1/items/` (Leer todos)
- ✅ GET `/api/v1/items/{item_id}` (Leer uno)

Faltan por implementar:
- ❌ PUT `/api/v1/items/{item_id}` (Actualizar)
- ❌ DELETE `/api/v1/items/{item_id}` (Eliminar)

## 📚 Pasos a Seguir

### Paso 1: Modelo ItemUpdate
📁 **Archivo:** `app/models/item.py`

```python
# Busca esta sección y descomenta/completa:
class ItemUpdate(BaseModel):
    name: str
    price: float
```

**¿Por qué?** Necesitamos un modelo para validar los datos que llegan en las peticiones PUT.

### Paso 2: Función update_item_by_id
📁 **Archivo:** `app/database/memory_db.py`

```python
# 1. Primero actualiza el import al inicio del archivo:
from app.models.item import Item, ItemUpdate

# 2. Luego implementa esta función:
def update_item_by_id(item_id: int, item_update: ItemUpdate) -> Optional[Item]:
    """Actualizar un item por ID"""
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            updated_item = Item(id=item_id, name=item_update.name, price=item_update.price)
            items_db[idx] = updated_item
            return updated_item
    return None
```

**Explicación paso a paso:**
1. Recorremos la lista con `enumerate()` para obtener índice y item
2. Comparamos si el `item.id` coincide con el `item_id` buscado
3. Si coincide, creamos un nuevo `Item` con los datos actualizados
4. Reemplazamos el item en la posición `idx`
5. Retornamos el item actualizado
6. Si no lo encontramos, retornamos `None`

### Paso 3: Función delete_item_by_id
📁 **Archivo:** `app/database/memory_db.py`

```python
def delete_item_by_id(item_id: int) -> bool:
    """Eliminar un item por ID"""
    global items_db
    original_length = len(items_db)
    items_db = [item for item in items_db if item.id != item_id]
    return len(items_db) < original_length
```

**Explicación paso a paso:**
1. Usamos `global items_db` para modificar la variable global
2. Guardamos la longitud original de la lista
3. Filtramos la lista manteniendo solo items con ID diferente
4. Retornamos `True` si se eliminó algo (cambió la longitud), `False` si no

### Paso 4: Endpoint PUT
📁 **Archivo:** `app/api/routes/items.py`

```python
# 1. Actualiza los imports al inicio:
from app.models.item import Item, ItemCreate, ItemUpdate
from app.database.memory_db import get_items_db, add_item, get_item_by_id, update_item_by_id, delete_item_by_id

# 2. Implementa el endpoint:
@router.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemUpdate):
    """Actualizar un item por ID"""
    updated_item = update_item_by_id(item_id, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item
```

### Paso 5: Endpoint DELETE
📁 **Archivo:** `app/api/routes/items.py`

```python
@router.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    """Eliminar un item por ID"""
    success = delete_item_by_id(item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
```

**Nota:** El endpoint DELETE usa `status_code=204` (No Content) y no retorna nada cuando es exitoso.

## 🧪 Cómo Probar tu Implementación

### 1. Ejecutar la aplicación:
```bash
uvicorn app.main:app --reload
```

### 2. Ir a la documentación automática:
Abrir en el navegador: `http://localhost:8000/docs`

### 3. Probar los endpoints:

**Crear un item (POST):**
```json
POST /api/v1/items/
{
  "name": "Laptop",
  "price": 999.99
}
```

**Actualizar el item (PUT):**
```json
PUT /api/v1/items/1
{
  "name": "Laptop Gaming",
  "price": 1299.99
}
```

**Eliminar el item (DELETE):**
```
DELETE /api/v1/items/1
```

## ❗ Errores Comunes

1. **ImportError:** Verificar que todos los imports estén actualizados
2. **NameError:** Asegurarse de que las funciones estén implementadas antes de usarlas
3. **404 Not Found:** Verificar que el ID del item exista antes de actualizar/eliminar

## ✅ Lista de Verificación

- [ ] Modelo `ItemUpdate` creado en `app/models/item.py`
- [ ] Import de `ItemUpdate` actualizado en `app/database/memory_db.py`
- [ ] Función `update_item_by_id()` implementada
- [ ] Función `delete_item_by_id()` implementada
- [ ] Imports actualizados en `app/api/routes/items.py`
- [ ] Endpoint PUT implementado
- [ ] Endpoint DELETE implementado
- [ ] Aplicación ejecuta sin errores
- [ ] Todos los endpoints funcionan en `/docs`

## 🎉 ¡Felicitaciones!
Una vez completados todos los pasos, tendrás una API CRUD completa con las cuatro operaciones básicas: CREATE, READ, UPDATE y DELETE. 