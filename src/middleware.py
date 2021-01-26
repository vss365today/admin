from datetime import datetime
from typing import Callable, Dict, Union

from flask import current_app, render_template, session
from src.core.models.User import User
from src.core.models.Token import Token


@current_app.context_processor
def inject_current_date() -> Dict[str, datetime]:
    return {"current_date": datetime.now()}


@current_app.context_processor
def nav_cur_page() -> Dict[str, Callable]:
    return {
        "nav_cur_page": lambda title, has: (
            "active" if has.strip() in title.strip().lower() else ""
        )
    }


@current_app.context_processor
def current_user_info() -> Dict[str, Union[User, Token]]:
    return {
        "current_user": session.get("USER"),
        "current_user_token": session.get("TOKEN"),
    }


@current_app.errorhandler(404)
def page_not_found(exc) -> tuple:
    return render_template("partials/errors/404.html"), 404


@current_app.errorhandler(500)
def server_error(exc) -> tuple:
    return render_template("partials/errors/500.html"), 500
