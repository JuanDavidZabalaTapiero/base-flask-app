from flask import Flask
from .blueprints import register_blueprints
from .extensions import db, migrate
from .config import Config

def create_app(config_class=Config):
    app = Flask(__name__)

    # == CONFIGURACIÓN ==
    app.config.from_object(config_class)
    
    # == INICIALIZAR EXTENSIONES ==
    db.init_app(app)
    migrate.init_app(app, db)

    # == IMPORTAR MODELOS ==
    from . import models # noqa: F401-
    
    # == REGISTRAR BLUEPRINTS ==
    register_blueprints(app)

    return app