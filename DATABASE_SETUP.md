# Configuración de Base de Datos PostgreSQL

Esta aplicación ahora usa PostgreSQL como base de datos en lugar de una base de datos en memoria.

## Requisitos Previos

1. **PostgreSQL instalado y ejecutándose**
   ```bash
   # En macOS con Homebrew
   brew install postgresql
   brew services start postgresql
   
   # En Ubuntu/Debian
   sudo apt-get install postgresql postgresql-contrib
   sudo systemctl start postgresql
   ```

2. **Crear la base de datos**
   ```bash
   # Conectar como usuario postgres
   psql -U postgres
   
   # Crear la base de datos
   CREATE DATABASE mini_crud_db;
   
   # Crear usuario (opcional)
   CREATE USER mini_crud_user WITH PASSWORD 'password';
   GRANT ALL PRIVILEGES ON DATABASE mini_crud_db TO mini_crud_user;
   ```

## Configuración del Entorno

1. **Variables de entorno** (opcional)
   Puedes configurar la URL de la base de datos mediante la variable de entorno:
   ```bash
   export DATABASE_URL="postgresql://usuario:password@localhost:5432/mini_crud_db"
   ```

2. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

## Migraciones con Alembic

### Ejecutar migraciones

```bash
# Activar entorno virtual
source venv/bin/activate

# Ejecutar todas las migraciones pendientes
alembic upgrade head

# Ver historial de migraciones
alembic history

# Ver migración actual
alembic current
```

### Crear nuevas migraciones

```bash
# Generar migración automática (requiere conexión a BD)
alembic revision --autogenerate -m "Descripción del cambio"

# Crear migración manual
alembic revision -m "Descripción del cambio"
```

### Rollback de migraciones

```bash
# Volver a migración anterior
alembic downgrade -1

# Volver a migración específica
alembic downgrade revision_id
```

## Estructura de Archivos

- `app/database/db.py` - Configuración de SQLAlchemy y conexión a PostgreSQL
- `app/database/models.py` - Modelos de SQLAlchemy (tablas)
- `app/schemas.py` - Esquemas de Pydantic para validación
- `app/database/crud.py` - Operaciones CRUD con SQLAlchemy
- `alembic/` - Directorio de configuración y migraciones de Alembic

## Datos de Prueba

La aplicación incluye una migración que inserta datos de prueba:
- Laptop ($999.99)
- Mouse ($29.99)
- Teclado ($79.99)
- Monitor ($299.99)
- Auriculares ($149.99)

## Ejecutar la Aplicación

```bash
# Activar entorno virtual
source venv/bin/activate

# Ejecutar migraciones
alembic upgrade head

# Iniciar servidor
uvicorn app.main:app --reload
```

## Verificar la Instalación

1. Ejecuta las migraciones: `alembic upgrade head`
2. Inicia la aplicación: `uvicorn app.main:app --reload`
3. Visita: http://localhost:8000/docs
4. Prueba el endpoint GET /api/v1/items/ para ver los datos de prueba
