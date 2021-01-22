from flask import abort

from src.blueprint import bp_prompt as prompt


@prompt.route("/")
def index():
    abort(404)


@prompt.route("/edit/<string:prompt_date>")
def edit(prompt_date: str):
    abort(404)
