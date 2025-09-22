# Base flask App

## Crear entorno virtual

```bash
python -m venv .venv

# Activación (Windows)
.venv\Scripts\activate

# Activación (Linux/Mac)
source .venv/bin/activate
```

## Instalar dependencias

```bash
pip install -r requirements.txt # producción
pip install -r requirements-dev.txt # desarrollo
```

## Crear variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
SECRET_KEY=tu_clave_secreta
DATABASE_URL=mysql://usuario:contraseña@host:3306/nombre_bd
UPLOAD_FOLDER=C:/Users/MyUser/Images
```

## Base de datos (migraciones)

Inicializar por primera vez (crear carpeta migrations):
```bash
flask db init
```

Si hay cambios en los modelos:
```bash
flask db migrate -m "mensaje describiendo el cambio"
```

Actualizar la BD
```bash
flask db upgrade
```

## Ejecutar la app
```bash
python run.py
```

## Ejecutar tests
```bash
pytest
```

## Inicializar pre-commit
```bash
pre-commit install
```

## Babel
generar mensajes:
```bash
pybabel extract -F babel.cfg -o messages.pot app/
```

inicializar idioma:
```bash
# ejemplo
pybabel init -i messages.pot -d app/translations -l en
```
actualizar el .po:
```bash
pybabel extract -F babel.cfg -o messages.pot app/
pybabel update -i messages.pot -d app/translations
```

compilar:
```bash
# ejemplo
pybabel compile -d app/translations
```