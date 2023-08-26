from flask import render_template

from src.blueprint import bp_keys
from src.core.api import v2


@bp_keys.route("/")
def index():
    render_opts = {"api_keys": v2.get("keys/")}
    return render_template("keys/index.html", **render_opts)
