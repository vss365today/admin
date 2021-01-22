from flask import abort

from src.blueprint import bp_host as host


@host.route("/")
def index():
    abort(404)


@host.route("/edit/<string:host_id>")
def edit(host_id: str):
    abort(404)
