"""Routes"""

from modules.system import system_bp
from modules.main import main_bp


def route(app):
    """Routes"""
    app.register_blueprint(system_bp)
    app.register_blueprint(main_bp)
