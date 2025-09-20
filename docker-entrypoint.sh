#!/bin/bash

# Script de entrada para el contenedor Docker

echo "🐳 Iniciando Mini API CRUD con Docker..."

# Mostrar información de debug
echo "🔍 Variables de entorno:"
echo "DATABASE_URL: ${DATABASE_URL:-'No definida'}"

# Función para esperar a que PostgreSQL esté listo
wait_for_postgres() {
    echo "⏳ Esperando a que PostgreSQL esté listo..."
    local max_attempts=30
    local attempt=1
    
    until pg_isready -h db -p 5432 -U postgres; do
        echo "🔄 PostgreSQL no está listo - intento $attempt/$max_attempts"
        if [ $attempt -eq $max_attempts ]; then
            echo "❌ PostgreSQL no está disponible después de $max_attempts intentos"
            exit 1
        fi
        attempt=$((attempt + 1))
        sleep 2
    done
    echo "✅ PostgreSQL está listo!"
}

# Función para crear la base de datos si no existe
create_database_if_not_exists() {
    echo "🔍 Verificando si la base de datos existe..."
    
    # Extraer el nombre de la base de datos de DATABASE_URL
    DB_NAME=$(echo $DATABASE_URL | sed 's/.*\/\([^?]*\).*/\1/')
    
    # Verificar si la base de datos existe
    DB_EXISTS=$(PGPASSWORD=password psql -h db -U postgres -lqt | cut -d \| -f 1 | grep -w $DB_NAME | wc -l)
    
    if [ $DB_EXISTS -eq 0 ]; then
        echo "🔨 Creando base de datos '$DB_NAME'..."
        PGPASSWORD=password createdb -h db -U postgres $DB_NAME
        if [ $? -eq 0 ]; then
            echo "✅ Base de datos '$DB_NAME' creada correctamente"
        else
            echo "❌ Error al crear la base de datos '$DB_NAME'"
            exit 1
        fi
    else
        echo "✅ La base de datos '$DB_NAME' ya existe"
    fi
}

# Esperar a que PostgreSQL esté disponible
wait_for_postgres

# Crear la base de datos si no existe
create_database_if_not_exists

# Ejecutar migraciones
echo "🔄 Ejecutando migraciones de base de datos..."
alembic upgrade head

if [ $? -eq 0 ]; then
    echo "✅ Migraciones ejecutadas correctamente"
else
    echo "❌ Error al ejecutar migraciones"
    exit 1
fi

# Iniciar la aplicación
echo "🚀 Iniciando servidor FastAPI..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
