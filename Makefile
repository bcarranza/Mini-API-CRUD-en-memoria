# Makefile para Mini API CRUD

.PHONY: help build up down restart logs shell db-shell clean test

# Mostrar ayuda por defecto
help:
	@echo "🐳 Mini API CRUD - Comandos disponibles:"
	@echo ""
	@echo "  make up          - Iniciar servicios (build automático)"
	@echo "  make down        - Detener servicios"
	@echo "  make restart     - Reiniciar servicios"
	@echo "  make build       - Reconstruir imágenes"
	@echo "  make logs        - Ver logs en tiempo real"
	@echo "  make shell       - Acceder al contenedor de la aplicación"
	@echo "  make db-shell    - Acceder a PostgreSQL"
	@echo "  make test        - Ejecutar tests"
	@echo "  make clean       - Limpiar todo (⚠️  elimina datos)"
	@echo "  make status      - Ver estado de servicios"
	@echo ""

# Iniciar servicios
up:
	@echo "🚀 Iniciando servicios..."
	docker-compose up --build

# Iniciar en segundo plano
up-d:
	@echo "🚀 Iniciando servicios en segundo plano..."
	docker-compose up -d --build

# Detener servicios
down:
	@echo "🛑 Deteniendo servicios..."
	docker-compose down

# Reiniciar servicios
restart:
	@echo "🔄 Reiniciando servicios..."
	docker-compose restart

# Reconstruir imágenes
build:
	@echo "🔨 Reconstruyendo imágenes..."
	docker-compose build

# Ver logs
logs:
	@echo "📋 Mostrando logs..."
	docker-compose logs -f

# Acceder al shell de la aplicación
shell:
	@echo "🐚 Accediendo al contenedor de la aplicación..."
	docker-compose exec web bash

# Acceder a PostgreSQL
db-shell:
	@echo "🐘 Accediendo a PostgreSQL..."
	docker-compose exec db psql -U postgres -d mini_crud_db

# Ejecutar tests
test:
	@echo "🧪 Ejecutando tests..."
	docker-compose exec web pytest

# Ver estado de servicios
status:
	@echo "📊 Estado de servicios:"
	docker-compose ps

# Limpiar todo
clean:
	@echo "🧹 Limpiando todo (esto eliminará todos los datos)..."
	@echo "¿Estás seguro? (Ctrl+C para cancelar)"
	@read -r dummy
	docker-compose down -v --rmi all

# Migraciones
migrate:
	@echo "🔄 Ejecutando migraciones..."
	docker-compose exec web alembic upgrade head

# Ver historial de migraciones
migrate-history:
	@echo "📚 Historial de migraciones:"
	docker-compose exec web alembic history

# Crear nueva migración
migrate-create:
	@echo "📝 Creando nueva migración..."
	@read -p "Descripción de la migración: " desc; \
	docker-compose exec web alembic revision --autogenerate -m "$$desc"

# Troubleshooting
debug:
	@echo "🔍 Información de debug:"
	@echo ""
	@echo "📊 Estado de servicios:"
	docker-compose ps
	@echo ""
	@echo "🌐 Variables de entorno en web:"
	docker-compose exec web env | grep DATABASE_URL || echo "❌ DATABASE_URL no encontrada"
	@echo ""
	@echo "🐘 Conectividad a PostgreSQL:"
	docker-compose exec web pg_isready -h db -p 5432 -U postgres || echo "❌ PostgreSQL no disponible"

# Fix completo
fix:
	@echo "🛠️  Aplicando fix completo..."
	@echo "⏹️  Deteniendo servicios..."
	docker-compose down
	@echo "🔨 Reconstruyendo imagen..."
	docker-compose build web
	@echo "🚀 Iniciando servicios..."
	docker-compose up

# Reset completo (⚠️  elimina datos)
reset:
	@echo "🧹 Reset completo del proyecto..."
	@echo "⚠️  Esto eliminará todos los datos. ¿Continuar? (Ctrl+C para cancelar)"
	@read -r dummy
	docker-compose down -v --rmi local
	docker-compose up --build
