# Mini API CRUD con PostgreSQL

Una API REST usando FastAPI para realizar operaciones CRUD sobre items con PostgreSQL y Alembic para migraciones.

## 🐳 Inicio Rápido con Docker (Recomendado)

```bash
# Clonar el repositorio
git clone <repository-url>
cd Mini-API-CRUD-en-memoria

# Iniciar con Docker (incluye PostgreSQL automáticamente)
docker-compose up --build

# O usar el Makefile
make up
```

**¡Eso es todo!** La API estará en http://localhost:8000

📚 **Para más detalles sobre Docker, ver [README_DOCKER.md](README_DOCKER.md)**

## Estructura del Proyecto

```
Mini-API-CRUD-en-memoria/
├── 🐳 Docker
│   ├── docker-compose.yml      # Servicios Docker
│   ├── Dockerfile             # Imagen de la aplicación
│   ├── docker-entrypoint.sh   # Script de inicio
│   └── .dockerignore          # Archivos ignorados
├── 📊 Base de Datos
│   ├── alembic.ini            # Configuración Alembic
│   └── alembic/               # Migraciones
│       ├── env.py
│       └── versions/
├── 🚀 Aplicación
│   └── app/
│       ├── main.py            # FastAPI principal
│       ├── schemas.py         # Esquemas Pydantic
│       ├── api/routes/items.py # Endpoints CRUD
│       └── database/
│           ├── db.py          # Configuración PostgreSQL
│           ├── models.py      # Modelos SQLAlchemy
│           └── crud.py        # Operaciones CRUD
├── 📚 Documentación
│   ├── README_DOCKER.md       # Guía completa Docker
│   ├── DATABASE_SETUP.md      # Setup manual PostgreSQL
│   └── Makefile              # Comandos útiles
└── requirements.txt           # Dependencias Python
```

## 🔧 Instalación Manual (Alternativa)

Si prefieres no usar Docker:

1. **Instalar PostgreSQL** y crear base de datos `mini_crud_db`
2. **Instalar dependencias Python:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Ejecutar migraciones:**
   ```bash
   alembic upgrade head
   ```
4. **Iniciar servidor:**
   ```bash
   uvicorn app.main:app --reload
   ```

📖 **Guía detallada en [DATABASE_SETUP.md](DATABASE_SETUP.md)**

## Documentación

FastAPI genera automáticamente documentación interactiva:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpoints

### Endpoints Disponibles ✅

- `POST /api/v1/items/` - Crear un nuevo item
- `GET /api/v1/items/` - Obtener todos los items
- `GET /api/v1/items/{item_id}` - Obtener un item específico
- `PUT /api/v1/items/{item_id}` - Actualizar un item
- `DELETE /api/v1/items/{item_id}` - Eliminar un item

## 📊 Datos de Prueba

La aplicación incluye datos de muestra que se cargan automáticamente:
- Laptop ($999.99)
- Mouse ($29.99)
- Teclado ($79.99)
- Monitor ($299.99)
- Auriculares ($149.99)

## 🧪 Para Estudiantes

Este proyecto es perfecto para aprender:
- **FastAPI** y desarrollo de APIs REST
- **PostgreSQL** con SQLAlchemy ORM
- **Migraciones** de base de datos con Alembic
- **Docker** y containerización
- **Arquitectura** de aplicaciones web modernas

### Extensiones sugeridas:
- Añadir autenticación JWT
- Implementar paginación
- Agregar filtros y búsqueda
- Añadir validaciones avanzadas
- Implementar cache con Redis

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