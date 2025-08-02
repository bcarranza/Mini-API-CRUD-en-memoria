# Pruebas Automáticas - Mini API CRUD

Este directorio contiene las pruebas automáticas para la Mini API CRUD en memoria.

## Pruebas Implementadas (6 total)

### 1. `test_obtener_raiz_retorna_200`
- **Endpoint**: `GET /`
- **Descripción**: Verifica que la ruta raíz retorna un código de estado 200
- **Validaciones**:
  - Status code = 200
  - Mensaje de bienvenida correcto

### 2. `test_crear_item_con_datos_validos`
- **Endpoint**: `POST /api/v1/items/`
- **Descripción**: Prueba la creación de items con datos válidos
- **Validaciones**:
  - Status code = 201 (Created)
  - Datos retornados coinciden con los enviados
  - Se asigna un ID automáticamente

### 3. `test_crear_item_con_datos_invalidos_falla`
- **Endpoint**: `POST /api/v1/items/`
- **Descripción**: Prueba que la API rechaza datos inválidos (campo faltante)
- **Validaciones**:
  - Status code = 422 (Unprocessable Entity)
  - Se retorna información de error

### 4. `test_obtener_lista_items`
- **Endpoint**: `GET /api/v1/items/`
- **Descripción**: Verifica que se puede obtener la lista de items
- **Validaciones**:
  - Status code = 200
  - Retorna una lista

### 5. `test_obtener_item_inexistente_retorna_404`
- **Endpoint**: `GET /api/v1/items/{id}`
- **Descripción**: Prueba que obtener un item inexistente retorna 404
- **Validaciones**:
  - Status code = 404
  - Mensaje de error correcto

### 6. `test_crear_y_obtener_item`
- **Endpoints**: `POST /api/v1/items/` y `GET /api/v1/items/{id}`
- **Descripción**: Prueba completa de creación y recuperación de un item
- **Validaciones**:
  - Creación exitosa
  - Recuperación exitosa
  - Datos consistentes

## Ejecutar las Pruebas

### Instalar dependencias
```bash
pip install -r requirements.txt
```

### Ejecutar todas las pruebas
```bash
pytest
```

### Ejecutar con más detalles
```bash
pytest -v
```

### Ejecutar una prueba específica
```bash
pytest tests/test_api.py::TestAPI::test_obtener_raiz_retorna_200 -v
```

### Ejecutar con cobertura (opcional)
```bash
pip install pytest-cov
pytest --cov=app tests/
```

## Estructura de las Pruebas

Las pruebas utilizan:
- **FastAPI TestClient**: Para simular peticiones HTTP
- **pytest**: Framework de pruebas
- **assertions**: Para validar respuestas y comportamientos esperados

## Cobertura de Pruebas

✅ **Casos Exitosos:**
- GET raíz (200)
- POST con datos válidos (201)
- GET lista de items (200)
- GET item específico (200)

✅ **Casos de Error:**
- POST con datos inválidos (422)
- GET item inexistente (404)

✅ **Pruebas de Integración:**
- Crear y recuperar item

## Notas Importantes

- Las pruebas se ejecutan contra la base de datos en memoria
- Cada prueba es independiente
- Los datos se resetean entre pruebas
- Las pruebas cubren casos exitosos y de error 