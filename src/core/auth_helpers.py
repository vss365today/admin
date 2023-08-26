import functools
from typing import NoReturn

from flask import abort, session

__all__ = ["authorize_blueprint", "authorize_route", "is_logged_in"]


def authorize_blueprint() -> None | NoReturn:
    """Determine if the request to a blueprint has been properly authorized."""
    if not is_logged_in():
        abort(403)


def authorize_route(func):
    """Protect a single route.

    This decorator is useful when a single endpoint
    needs to be protected but not the entire blueprint.
    """

    @functools.wraps(func)
    def wrap(*args, **kwargs):
        authorize_blueprint()
        return func(*args, **kwargs)

    return wrap


def is_logged_in() -> bool:
    """Determine if an admin is logged in."""
    return "USER" in session and "TOKEN" in session
