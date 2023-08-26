from datetime import datetime

from flask import flash, redirect, render_template, session, url_for

from src.blueprints import root
from src.core import database as db
from src.core.api import v2
from src.core.auth_helpers import authorize_route, is_logged_in
from src.core.forms import FormUserLogin


@root.route("/")
def index() -> str:
    """Site login page."""
    # We're already logged in. Don't attempt to do it again
    if is_logged_in():
        return redirect(url_for("root.dashboard"))

    render_opts = {"form": FormUserLogin()}
    return render_template("root/index.html", **render_opts)


@root.route("/login", methods=["POST"])
def login():
    """Login a user."""
    # We're already logged in. Don't attempt to do it again
    if is_logged_in():
        return redirect(url_for("root.dashboard"))

    # Attempt to validate the username/password combo
    form = FormUserLogin()
    if form.validate_on_submit():
        if not db.users.login(form.data["username"], form.data["password"]):
            flash("That is not a valid login.", "error")
            return redirect(url_for("root.index"))

    # Fetch their info and store it in the session
    session["USER"], session["TOKEN"] = db.users.get_info(form.data["username"])
    return redirect(url_for("root.dashboard"))


@root.route("/logout")
@authorize_route
def logout():
    """Logout a user."""
    # Remove the user object from the session
    if is_logged_in():
        del session["USER"]
        del session["TOKEN"]

    flash("You have been successfully logged out.", "info")
    return redirect(url_for("root.index"))


@root.route("/dashboard")
@authorize_route
def dashboard():
    """Landing page after successful login."""
    render_opts = {
        "prompt": v2.get("prompts/", user_token=False)[0],
        "host": v2.get("hosts", "current", user_token=False),
    }
    return render_template("root/dashboard.html", **render_opts)
