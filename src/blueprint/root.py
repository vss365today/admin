from datetime import datetime

from flask import flash, redirect, render_template, session, url_for

from src.blueprint import bp_root as root
from src.core.auth_helpers import authorize_route
from src.core import api
from src.core.database import users
from src.core.forms import FormUserLogin


@root.route("/")
def index() -> str:
    """Site login page."""
    render_opts = {"form": FormUserLogin()}
    return render_template("root/index.html", **render_opts)


@root.route("/login", methods=["POST"])
def login():
    """Login a user."""
    # We're already logged in. Don't attempt to do it again
    if "USER" in session:
        return redirect(url_for("root.dashboard"))

    # Attempt to validate the username/password combo
    form = FormUserLogin()
    if form.validate_on_submit():
        if not users.login(form.data["username"], form.data["password"]):
            flash("That is not a valid login.", "error")
            return redirect(url_for("root.index"))

    # Fetch their info and store it in the session
    session["USER"], session["TOKEN"] = users.get_info(form.data["username"])
    return redirect(url_for("root.dashboard"))


@root.route("/logout")
@authorize_route
def logout():
    """Logout a user."""
    # Remove the user object from the session
    if "USER" in session:
        del session["USER"]
        del session["TOKEN"]

    flash("You have been successfully logged out.", "info")
    return redirect(url_for("root.index"))


@root.route("/dashboard")
@authorize_route
def dashboard():
    """Landing page after successful login."""
    today = datetime.now()
    current_hosting_date = api.get(
        "settings",
        "hosting",
        user_token=False,
        params={"date": today.isoformat()},
    )[0]
    render_opts = {
        "prompt": api.get("prompt")[0],
        "host": api.get(
            "host",
            "date",
            user_token=False,
            params={"date": today.replace(day=current_hosting_date)},
        ),
    }
    return render_template("root/dash.html", **render_opts)
