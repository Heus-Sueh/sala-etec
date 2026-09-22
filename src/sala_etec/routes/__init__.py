# sala_etec/routes/__init__.py
from sala_etec.routes.auth import auth_bp
from sala_etec.routes.main import main_bp
from sala_etec.routes.materiais import materiais_bp
from sala_etec.routes.paineis import paineis_bp


def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(materiais_bp)
    app.register_blueprint(paineis_bp)
