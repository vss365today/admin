from flask import flash, redirect, render_template, url_for

from src.blueprint import bp_root as root
from src.core.database import users
from src.core.forms import FormUserLogin


@root.route("/")
def index() -> str:
    """Site login page."""
    render_opts = {"form": FormUserLogin()}
    return render_template("root.html", **render_opts)


@root.route("login", methods=["POST"])
def login():
    """Login a user."""
    # Confirm we have form data
    form = FormUserLogin()
    if form.validate_on_submit():

        # Validate the username/password combo
        valid_login = users.login(form.data["username"], form.data["password"])

        # That didn't work
        if not valid_login:
            flash("That is not a valid login.", "error")
            return redirect(url_for("root.index"))

    # TODO Redirect to the landing page
    return "Hello, world"
