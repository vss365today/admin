import functools

from flask import abort, session


__all__ = ["authorize_blueprint", "authorize_route"]


def authorize_blueprint():
    """Determine if the request to a blueprint has been properly authorized."""
    if "USER" not in session:
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
