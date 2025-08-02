# Mini API CRUD en Memoria

Una API REST simple usando FastAPI para realizar operaciones CRUD sobre items almacenados en memoria.

## Estructura del Proyecto

```
Mini-API-CRUD-en-memoria/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Aplicación principal FastAPI
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       └── items.py        # Rutas para CRUD de items
│   ├── models/
│   │   ├── __init__.py
│   │   └── item.py            # Modelos Pydantic
│   └── database/
│       ├── __init__.py
│       └── memory_db.py       # Lógica de base de datos en memoria
├── requirements.txt           # Dependencias del proyecto
├── test_main.py              # Pruebas unitarias con pytest
├── pytest.ini               # Configuración de pytest
├── run_tests.py             # Script para ejecutar pruebas
└── README.md                 # Este archivo
```

## Instalación

1. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

## Ejecución

Para ejecutar el servidor de desarrollo:

```bash
uvicorn app.main:app --reload
```

La API estará disponible en: `http://localhost:8000`

## Documentación

FastAPI genera automáticamente documentación interactiva:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpoints

### Items Implementados ✅

- `POST /api/v1/items/` - Crear un nuevo item
- `GET /api/v1/items/` - Obtener todos los items
- `GET /api/v1/items/{item_id}` - Obtener un item específico

### Items por Implementar (Ejercicio para Estudiantes) 📝

- `PUT /api/v1/items/{item_id}` - Actualizar un item
- `DELETE /api/v1/items/{item_id}` - Eliminar un item

## 🎯 Ejercicio para Estudiantes

Este proyecto está parcialmente implementado. Los estudiantes deben completar las operaciones **UPDATE (PUT)** y **DELETE**.

### Tareas a realizar:

#### 1. Modelo ItemUpdate (`app/models/item.py`)
- [ ] Descomentar y completar la clase `ItemUpdate`
- [ ] Debe tener los mismos campos que `ItemCreate`

#### 2. Funciones de Base de Datos (`app/database/memory_db.py`)
- [ ] Implementar `update_item_by_id()`
- [ ] Implementar `delete_item_by_id()`
- [ ] Descomentar el import de `ItemUpdate`

#### 3. Endpoints de API (`app/api/routes/items.py`)
- [ ] Implementar endpoint PUT `/items/{item_id}`
- [ ] Implementar endpoint DELETE `/items/{item_id}`
- [ ] Descomentar los imports necesarios

### 💡 Pistas y Guías

Todos los archivos contienen comentarios `TODO:` con pistas específicas sobre cómo implementar cada función.

### Ejemplo de uso

```json
// POST /api/v1/items/
{
  "name": "Laptop",
  "price": 999.99
}

// Respuesta
{
  "id": 1,
  "name": "Laptop",
  "price": 999.99
}
```

## 🧪 Pruebas

### Ejecutar las pruebas

```bash
# Opción 1: Usar el script personalizado
python run_tests.py

# Opción 2: Usar pytest directamente
pytest test_main.py -v

# Opción 3: Ejecutar con más detalles
pytest test_main.py -v --tb=long
```

### Pruebas implementadas

El archivo `test_main.py` incluye **7 pruebas** que cubren:

1. **test_create_item_success** - Crear item exitosamente
2. **test_get_all_items_empty** - Obtener lista vacía de items
3. **test_get_item_by_id_not_found** - Error 404 al buscar item inexistente
4. **test_create_item_missing_fields** - Error 422 con datos faltantes
5. **test_update_item_success** - Actualizar item exitosamente
6. **test_delete_item_success** - Eliminar item exitosamente
7. **test_create_item_invalid_price** - Crear item con precio negativo

### Casos de error probados

- ✅ **Datos faltantes**: Campo `price` faltante (código 422)
- ✅ **Item no encontrado**: Buscar item con ID inexistente (código 404)
- ✅ **Validación de datos**: Precios negativos (aceptado por defecto) 