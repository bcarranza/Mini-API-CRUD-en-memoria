# 🐳 Mini API CRUD con Docker

Esta es la versión dockerizada de la Mini API CRUD que utiliza PostgreSQL y Alembic para migraciones.

## 🚀 Inicio Rápido

### Prerrequisitos
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Ejecutar la aplicación

```bash
# Clonar el repositorio (si no lo has hecho)
git clone <repository-url>
cd Mini-API-CRUD-en-memoria

# Iniciar todos los servicios
docker-compose up --build

# O en modo detached (segundo plano)
docker-compose up -d --build
```

¡Eso es todo! 🎉

La aplicación estará disponible en:
- **API**: http://localhost:8000
- **Documentación**: http://localhost:8000/docs
- **PostgreSQL**: localhost:5432

## 📋 Comandos Útiles

### Gestión de contenedores
```bash
# Iniciar servicios
docker-compose up

# Iniciar en segundo plano
docker-compose up -d

# Detener servicios
docker-compose down

# Detener y eliminar volúmenes (⚠️ elimina datos)
docker-compose down -v

# Ver logs
docker-compose logs

# Ver logs en tiempo real
docker-compose logs -f

# Ver logs de un servicio específico
docker-compose logs web
docker-compose logs db
```

### Desarrollo
```bash
# Reconstruir la imagen de la aplicación
docker-compose build web

# Reiniciar solo la aplicación
docker-compose restart web

# Ejecutar comandos en el contenedor
docker-compose exec web bash
docker-compose exec web alembic current
docker-compose exec web alembic history
```

### Base de datos
```bash
# Conectar a PostgreSQL
docker-compose exec db psql -U postgres -d mini_crud_db

# Ejecutar migraciones manualmente
docker-compose exec web alembic upgrade head

# Crear nueva migración
docker-compose exec web alembic revision --autogenerate -m "Descripción"

# Hacer backup de la base de datos
docker-compose exec db pg_dump -U postgres mini_crud_db > backup.sql
```

## 🏗️ Estructura del Proyecto

```
Mini-API-CRUD-en-memoria/
├── docker-compose.yml          # Configuración de servicios
├── Dockerfile                  # Imagen de la aplicación
├── docker-entrypoint.sh        # Script de inicio
├── .dockerignore               # Archivos ignorados en el build
├── requirements.txt            # Dependencias Python
├── alembic.ini                 # Configuración Alembic
├── alembic/                    # Migraciones
│   ├── env.py
│   └── versions/
│       ├── *_create_items_table.py
│       └── *_add_sample_data.py
└── app/
    ├── main.py                 # Aplicación FastAPI
    ├── schemas.py              # Esquemas Pydantic
    ├── api/routes/items.py     # Endpoints
    └── database/
        ├── db.py               # Configuración DB
        ├── models.py           # Modelos SQLAlchemy
        └── crud.py             # Operaciones CRUD
```

## 🔧 Configuración

### Variables de entorno
El archivo `docker-compose.yml` define las siguientes variables:

**PostgreSQL:**
- `POSTGRES_DB=mini_crud_db`
- `POSTGRES_USER=postgres`
- `POSTGRES_PASSWORD=password`

**Aplicación:**
- `DATABASE_URL=postgresql://postgres:password@db:5432/mini_crud_db`

### Puertos
- **8000**: API FastAPI
- **5432**: PostgreSQL

### Volúmenes
- `postgres_data`: Datos persistentes de PostgreSQL
- `.:/app`: Código de la aplicación (para desarrollo)

## 🧪 Datos de Prueba

La aplicación incluye datos de prueba que se insertan automáticamente:
- Laptop ($999.99)
- Mouse ($29.99)
- Teclado ($79.99)
- Monitor ($299.99)
- Auriculares ($149.99)

## 🔍 Testing

```bash
# Ejecutar tests dentro del contenedor
docker-compose exec web pytest

# Ejecutar tests específicos
docker-compose exec web pytest app/test_main.py

# Ejecutar con coverage
docker-compose exec web pytest --cov=app
```

## 🐛 Troubleshooting

### La aplicación no inicia
```bash
# Ver logs detallados
docker-compose logs web

# Verificar que PostgreSQL esté ejecutándose
docker-compose logs db
```

### Error de conexión a la base de datos
```bash
# Verificar que el contenedor de DB esté funcionando
docker-compose ps

# Reiniciar servicios
docker-compose restart
```

### Migraciones fallan
```bash
# Ejecutar migraciones manualmente
docker-compose exec web alembic upgrade head

# Ver estado de migraciones
docker-compose exec web alembic current
```

### Limpiar todo y empezar de nuevo
```bash
# Detener y eliminar todo (incluyendo datos)
docker-compose down -v

# Eliminar imágenes
docker-compose down --rmi all

# Reconstruir desde cero
docker-compose up --build
```

## 🌟 Ventajas de usar Docker

1. **Sin instalación local**: No necesitas instalar PostgreSQL, Python, ni dependencias
2. **Consistencia**: Mismo ambiente en desarrollo, testing y producción
3. **Aislamiento**: No afecta tu sistema local
4. **Fácil cleanup**: `docker-compose down` elimina todo
5. **Portable**: Funciona igual en cualquier sistema con Docker

## 📚 Próximos Pasos

- Configurar Docker para producción
- Añadir nginx como reverse proxy
- Implementar monitoring con Docker
- Configurar CI/CD con Docker

¡Ahora puedes enfocarte en programar sin preocuparte por la configuración! 🎯
