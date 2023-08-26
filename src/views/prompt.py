from flask import abort

from src.blueprints import prompts


@prompts.route("/")
def index():
    abort(404)


@prompts.route("/edit/<string:prompt_date>")
def edit(prompt_date: str):
    abort(404)
