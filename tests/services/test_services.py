from app.blueprints.tests.models import UserTest
from app.blueprints.tests.services import create_user_test_service


def test_create_user_service(session):
    success, message, obj = create_user_test_service(name="Juan")

    assert success is True
    assert message == "Usuario creado"
    assert obj.name == "Juan"

    main = session.query(UserTest).filter_by(name="Juan").first()
    assert main is not None
