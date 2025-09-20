from .tests.routes import tests_bp


def register_blueprints(app):
    app.register_blueprint(tests_bp)
