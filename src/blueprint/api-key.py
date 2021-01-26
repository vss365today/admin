from flask import abort

from src.blueprint import bp_api_key as api_key


@api_key.route("/")
def index():
    abort(404)
