from flask import render_template

from src.blueprint import bp_root as root
from src.core.forms import FormUserLogin


@root.route("/")
def index():
    render_opts = {"form": FormUserLogin()}
    return render_template("root.html", **render_opts)
