from app.extensions import db

from .models import UserTest


def create_user_test_service(name, commit=True):
    if not name:
        return False, "El nombre es obligatorio", None

    try:
        user = UserTest(name=name)
        db.session.add(user)

        if commit:
            db.session.commit()
        else:
            # USER CON ID (SIN COMMIT)
            db.session.flush()

        return True, "Usuario creado", user

    except Exception as e:
        db.session.rollback()
        print(f"Error en create_user_test_service: {e}")
        return False, "Error al intentar crear el usuario", None
