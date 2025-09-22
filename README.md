# Base Flask App

Proyecto base para construir aplicaciones con Flask, organizado en módulos (blueprints), con soporte para base de datos, formularios, migraciones, testing y compilación de estilos con Gulp.

## Tecnologías utilizadas

* Flask (framework principal)
* Flask-SQLAlchemy (ORM para la base de datos)
* Flask-Migrate (migraciones de base de datos con Alembic)
* Flask-WTF (formularios y validación)
* pytest (testing)
* Bootstrap (CSS y JS)
* Bootstrap Icons (iconos SVG y fuente)
* Gulp (compilación y minificación de SCSS → CSS)

## Estructura del proyecto
```csharp
raíz/
│── app/                 # Aplicación principal
│   ├── blueprints/      # Módulos (ej: users, tests, etc.)
│   ├── static/          # Archivos estáticos (css, js, vendor)
│   ├── templates/       # Plantillas HTML
│   ├── __init__.py      # create_app()
│   ├── config.py        # Configuraciones (Config, TestConfig...)
│   ├── extensions.py    # Extensiones (db, migrate, csrf)
│   ├── forms.py         # Formularios globales
│   └── models.py        # Modelos globales
│
│── frontend/            # SCSS + Gulp
│── migrations/          # Migraciones de base de datos
│── tests/               # Pruebas unitarias e integración
│── run.py               # Punto de entrada de la app
│── requirements.txt     # Dependencias de producción
│── requirements-dev.txt # Dependencias de desarrollo
│── pytest.ini           # Configuración de pytest
│── .pre-commit-config.yaml
│── .gitignore
│── README.md
```

## Instalación

### 1. Crear entorno virtual
```bash
python -m venv .venv

# Activación (Windows)
.venv\Scripts\activate

# Activación (Linux/Mac)
source .venv/bin/activate
```

### 2. Instalar dependencias
```bash
# Producción
pip install -r requirements.txt

# Desarrollo
pip install -r requirements-dev.txt 
```

### 3. Variables de entorno
Crear un archivo .env en la raíz del proyecto:
```env
SECRET_KEY=tu_clave_secreta
DATABASE_URL=mysql://usuario:contraseña@host:3306/nombre_bd
```

## Base de datos (migraciones)
Inicializar por primera vez (crear carpeta migrations):
```bash
flask db init
```

Generar migraciones cuando haya cambios en los modelos:
```bash
flask db migrate -m "mensaje describiendo el cambio"
```

Actualizar la base de datos:
```bash
flask db upgrade
```

## Ejecutar la aplicación
```bash
python run.py
```
La aplicación quedará disponible en http://127.0.0.1:5000/

## Testing
Ejecutar todos los tests con pytest:
```bash
pytest
```

Los tests están organizados en:
* `tests/blueprints/` → pruebas de rutas (endpoints)
* `tests/services/` → pruebas de lógica de negocio (consultas)

El archivo tests/conftest.py configura la app y la base de datos en memoria para las pruebas.

## Estilos (Frontend con Gulp)
El proyecto usa Gulp para compilar SCSS → CSS minificado y guardarlo en `app/static/css`

### 1. Instalar dependencias de Node.js
```bash
cd frontend
npm install
```

### 2. Compilar SCSS y vigilar cambios
```bash
npx gulp
```
Esto compilará todos los `.scss` en `frontend/scss/` hacia `app/static/css/`

## Organización de Blueprints
En `app/blueprints/` se debe crear una carpeta por cada módulo.
Cada módulo puede incluir:

* `routes.py` → rutas y vistas
* `models.py` → modelos propios del módulo
* `services.py` → lógica de negocio (consultas, validaciones, etc.)
* `forms.py` → formularios
* `api.py` (opcional) → endpoints de API REST

El registro de todos los blueprints se hace en `app/blueprints/__init__.py`, llamado desde `app/__init__.py`.

## Plantillas
En `app/templates/` se recomienda:
* Crear una carpeta por cada módulo (ej: `tests/`, `users/`)
* Utilizar base.html como plantilla base con bloques extendibles
* Guardar errores comunes en `templates/errors/` (ej: `404.html`)

## Pre-commit
Este proyecto incluye hooks configurados en `.pre-commit-config.yaml`.
Para activarlos:
```bash
pre-commit install
```
Esto ejecutará linters y chequeos automáticos antes de cada commit.