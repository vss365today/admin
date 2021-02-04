from flask import render_template

from src.blueprint import bp_api_key as api_key
from src.core import api


@api_key.route("/")
def index():
    render_opts = {"api_keys": api.get("api-key", params={"all": True})}
    return render_template("api-key/index.html", **render_opts)
