import pytest
from app import create_app
from app.config import TestConfig
from app.extensions import db as _db
from sqlalchemy.orm import sessionmaker, scoped_session


@pytest.fixture(scope="session")
def app():
    """Crea una única app Flask para toda la sesión de tests"""
    app = create_app(TestConfig)
    return app

@pytest.fixture
def client(app):
    """Cliente de pruebas para simular requests HTTP"""
    return app.test_client()

@pytest.fixture(scope="session")
def db(app):
    """Crea la BD en memoria una vez y mantiene la conexión activa"""
    with app.app_context():
        _db.create_all()
        yield _db
        _db.drop_all()

@pytest.fixture(scope="function", autouse=True)
def session(db):
    # Abre una conexión directa a la base de datos
    connection = db.engine.connect()
    # Inicia una transacción.
    transaction = connection.begin()

    # Crea una fábrica de sesiones
    Session = scoped_session(sessionmaker(bind=connection))
    # Creamos una instancia de sesión.
    session = Session()

    # Sobrescribir db.session con el scoped_session
    db.session = Session

    yield session

    # Todos los cambios de ese test desaparecen
    transaction.rollback()
    # Cierra la conexión a la BD
    connection.close()
    # Elimina cualquier sesión activa
    Session.remove()