# 🛠️ Troubleshooting - Mini API CRUD Docker

## 🔧 Problema Resuelto: Error de Conexión a Base de Datos

### ❌ Error que se presentaba:
```
psycopg2.OperationalError: connection to server at "localhost" (::1), port 5432 failed: Connection refused
```

### ✅ Solución aplicada:

1. **Actualizado `alembic/env.py`** para usar variables de entorno:
   ```python
   # Override the sqlalchemy.url with environment variable if available
   database_url = os.getenv('DATABASE_URL')
   if database_url:
       config.set_main_option('sqlalchemy.url', database_url)
   ```

2. **Mejorado `docker-entrypoint.sh`** con mejor debug y timeouts.

### 🚀 Para aplicar los cambios:

```bash
# Opción 1: Reconstruir completamente
docker-compose down -v
docker-compose up --build

# Opción 2: Con Makefile
make clean
make up

# Opción 3: Solo reconstruir la aplicación
docker-compose build web
docker-compose up
```

## 🐛 Otros Problemas Comunes

### 1. PostgreSQL no inicia
```bash
# Ver logs de la base de datos
docker-compose logs db

# Verificar puerto disponible
lsof -i :5432

# Limpiar volúmenes y reiniciar
docker-compose down -v
docker-compose up
```

### 2. Permisos de archivos
```bash
# En macOS/Linux, asegurar permisos
chmod +x docker-entrypoint.sh
chmod +x start_dev.sh
```

### 3. Variables de entorno no funcionan
```bash
# Verificar dentro del contenedor
docker-compose exec web env | grep DATABASE_URL

# Debería mostrar:
# DATABASE_URL=postgresql://postgres:password@db:5432/mini_crud_db
```

### 4. Migraciones fallan
```bash
# Ejecutar migraciones manualmente
docker-compose exec web alembic current
docker-compose exec web alembic upgrade head

# Ver historial de migraciones
docker-compose exec web alembic history
```

### 5. Aplicación no responde
```bash
# Verificar que todos los servicios están corriendo
docker-compose ps

# Ver logs en tiempo real
docker-compose logs -f web

# Probar conexión
curl http://localhost:8000/
```

## 🔍 Comandos de Debug

### Información de contenedores
```bash
# Estado de servicios
docker-compose ps

# Logs de todos los servicios
docker-compose logs

# Logs específicos
docker-compose logs web
docker-compose logs db
```

### Acceder a contenedores
```bash
# Shell de la aplicación
docker-compose exec web bash

# Shell de PostgreSQL
docker-compose exec db psql -U postgres -d mini_crud_db

# Verificar archivos
docker-compose exec web ls -la /app
```

### Testing de conectividad
```bash
# Desde el contenedor de la app, probar conexión a DB
docker-compose exec web pg_isready -h db -p 5432 -U postgres

# Probar la API
curl http://localhost:8000/docs
curl http://localhost:8000/api/v1/items/
```

## 📝 Verificación Step-by-Step

1. **Verificar Docker está corriendo:**
   ```bash
   docker --version
   docker-compose --version
   ```

2. **Limpiar estado anterior:**
   ```bash
   docker-compose down -v
   ```

3. **Construir y iniciar:**
   ```bash
   docker-compose up --build
   ```

4. **Verificar servicios:**
   ```bash
   docker-compose ps
   ```

5. **Probar la aplicación:**
   - Abrir http://localhost:8000/docs
   - Probar endpoint GET /api/v1/items/

## 🆘 Si nada funciona

### Reset completo:
```bash
# Parar todo
docker-compose down -v --rmi all

# Limpiar Docker
docker system prune -a

# Rebuild desde cero
docker-compose up --build
```

### Verificar configuración:
1. ✅ Docker y Docker Compose instalados
2. ✅ Puerto 5432 y 8000 disponibles
3. ✅ Permisos de archivos correctos
4. ✅ Variables de entorno configuradas
5. ✅ Archivos de migración presentes

### Contacto:
Si el problema persiste, proporciona:
- Logs completos: `docker-compose logs`
- Sistema operativo
- Versión de Docker
- Comando específico que falla

