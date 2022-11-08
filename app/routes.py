"""Routes"""

from modules.system import system_bp


def route(app):
    """Routes"""
    app.register_blueprint(system_bp)
