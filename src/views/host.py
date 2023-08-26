from flask import abort

from src.blueprints import hosts


@hosts.route("/")
def index():
    abort(404)


@hosts.route("/edit/<string:host_id>")
def edit(host_id: str):
    abort(404)
