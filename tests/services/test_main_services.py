from app.blueprints.main.services import create_main_service
from app.blueprints.main.models import Main

def test_create_user_service(session):
    success, message, obj = create_main_service(
        name="Juan"
    )

    assert success is True
    assert message == "Main creado"
    assert obj.name == "Juan"

    main = session.query(Main).filter_by(name="Juan").first()
    assert main is not None