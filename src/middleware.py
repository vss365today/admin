from datetime import date

from flask import current_app, render_template, session

from src.core.helpers import get_static_url
from src.core.models.Token import Token
from src.core.models.User import User


@current_app.context_processor
def inject_context() -> dict:
    return {
        "current_date": date.today(),
        "current_user": session.get("USER"),
        "current_user_token": session.get("TOKEN"),
        "get_static_url": get_static_url,
        "nav_cur_page": lambda title, has: (
            "active" if has.strip() in title.strip().lower() else ""
        ),
    }

@current_app.errorhandler(404)
def page_not_found(exc) -> tuple:
    return render_template("partials/errors/404.html"), 404


@current_app.errorhandler(500)
def server_error(exc) -> tuple:
    return render_template("partials/errors/500.html"), 500
