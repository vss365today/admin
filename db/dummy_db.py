import json
import sys
from os import environ
from pathlib import Path

from flask import Flask

# We have to add the app path to the path to get the db schema
APP_ROOT = Path(__file__).parent.parent
sys.path.insert(0, APP_ROOT.as_posix())

from src.core.database import models


def get_config(file: str) -> str:
    return json.loads((APP_ROOT / "configuration" / file).read_text())


def get_secret(key: str) -> str:
    if "SYS_VARS_PATH" in environ:
        f = (Path(environ["SYS_VARS_PATH"]) / key).resolve()
    else:
        f = (APP_ROOT / ".." / "secrets" / key).resolve()
    return f.read_text().strip()


def create_app() -> Flask:
    """Dummy Flask instance used for database management."""
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secret tunnel"

    with app.app_context():
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

        # NOTE: Due to some WEIRDNESS with sqlalchemy, the spaces are INTENTIONAL.
        # DO NOT REMOVE THE SPACES. EVER.
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///     database.db?uri=true"
        models.db.init_app(app)
    return app
