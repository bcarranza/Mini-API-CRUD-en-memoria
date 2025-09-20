#!/bin/bash

# Script para iniciar el entorno de desarrollo

echo "🚀 Iniciando Mini API CRUD con PostgreSQL..."

# Activar entorno virtual
echo "📦 Activando entorno virtual..."
source venv/bin/activate

# Ejecutar migraciones
echo "🔄 Ejecutando migraciones de base de datos..."
alembic upgrade head

if [ $? -eq 0 ]; then
    echo "✅ Migraciones ejecutadas correctamente"
    echo "🌟 Iniciando servidor de desarrollo..."
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
else
    echo "❌ Error al ejecutar migraciones"
    echo "💡 Asegúrate de que PostgreSQL esté ejecutándose y la base de datos 'mini_crud_db' exista"
    echo "📚 Consulta DATABASE_SETUP.md para más información"
fi
