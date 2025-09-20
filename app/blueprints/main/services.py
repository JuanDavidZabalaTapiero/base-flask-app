from .models import Main
from app.extensions import db

def create_main_service(name):
    if not name:
        return False, "Nombre obligatorio", None
    
    try:
        main = Main(name=name)
        db.session.add(main)
        db.session.commit()
        return True, "Main creado", main
    
    except Exception as e:
        return False, "Error al intentar crear main", None