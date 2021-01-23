from flask import flash, redirect, render_template, url_for
from flask import session

from src.blueprint import bp_root as root
from src.core.database import users
from src.core.forms import FormUserLogin


@root.route("/")
def index() -> str:
    """Site login page."""
    render_opts = {"form": FormUserLogin()}
    return render_template("root.html", **render_opts)


@root.route("/login", methods=["POST"])
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

    # Update their last login datetime
    users.set_last_login(form.data["username"])

    # Fetch their info and store it in the session
    session["USER_USERNAME"] = form.data["username"]
    for k, v in users.get_info(form.data["username"]).items():
        session[f"USER_{k.upper()}"] = v

    # TODO Redirect to the landing page
    return "Hello, world"


@root.route("/logout")
def logout():
    """Logout a user."""
    flash("You have been successfully logged out.", "info")
    return redirect(url_for("root.index"))
