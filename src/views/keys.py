from flask import render_template

from src.blueprints import keys
from src.core.api import v2


@keys.route("/")
def index():
    render_opts = {"api_keys": v2.get("keys/")}
    return render_template("keys/index.html", **render_opts)
