from importlib import import_module
from os import getenv

from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

import src.core.configuration as config
from src.blueprint import all_blueprints
from src.core.filters import ALL_FILTERS
from src.extensions import init_extensions
from src.core.database import models

def create_app() -> Flask:
    """Create an instance of the app."""
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

    # Load the app configuration
    app.config.update(config.get_app_config("default"))
    app.config.update(config.get_app_config(getenv("FLASK_ENV")))

    # Put the app secret key into the expected key
    app.config["SECRET_KEY"] = app.config["SECRET_KEY_ADMIN"]
    del app.config["SECRET_KEY_ADMIN"]

    # Load the extensions
    init_extensions(app)

    # Load any injection/special app handler methods
    with app.app_context():
        import_module("src.middleware")

        # Create a database connection
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database/database.db?uri=true"
        models.db.init_app(app)


    # Register all of the blueprints
    for bp in all_blueprints:
        import_module(bp.import_name)
        app.register_blueprint(bp)

    # Register the filters
    for name, method in ALL_FILTERS.items():
        app.add_template_filter(method, name=name)

    return app
