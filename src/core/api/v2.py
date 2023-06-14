from typing import Any

import sys_vars

from src.core.api import _api


__all__ = ["delete", "get", "post", "put"]


def __create_api_url(*args: str) -> str:
    """Construct a URL to the given v2 API endpoint."""
    endpoint = "/".join(args)
    return f"{sys_vars.get('API_DOMAIN')}/v2/{endpoint}"


def delete(*args: str, user_token: bool = True, **kwargs: Any) -> dict:
    """Helper function for performing a DELETE request."""
    url = __create_api_url(*args)
    return _api.delete(url, user_token, **kwargs)


def get(*args: str, user_token: bool = True, **kwargs: Any) -> dict:
    """Helper function for performing a GET request."""
    url = __create_api_url(*args)
    return _api.get(url, user_token, **kwargs)


def post(*args: str, user_token: bool = True, **kwargs: Any) -> dict:
    """Helper function for performing a POST request."""
    url = __create_api_url(*args)
    return _api.post(url, user_token, **kwargs)


def put(*args: str, user_token: bool = True, **kwargs: Any) -> dict:
    """Helper function for performing a PUT request."""
    url = __create_api_url(*args)
    return _api.put(url, user_token, **kwargs)
