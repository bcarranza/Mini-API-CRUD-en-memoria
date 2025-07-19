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

### Items

- `POST /api/v1/items/` - Crear un nuevo item
- `GET /api/v1/items/` - Obtener todos los items
- `GET /api/v1/items/{item_id}` - Obtener un item específico
- `PUT /api/v1/items/{item_id}` - Actualizar un item
- `DELETE /api/v1/items/{item_id}` - Eliminar un item

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