from typing import Literal

from passlib.hash import pbkdf2_sha256

from src.core import api
from src.core.database.core import connect_to_db, convert_int_to_bool, get_sql
from src.core.models.User import User
from src.core.models.Token import Token


__all__ = ["get_info", "login", "set_last_login"]


def get_info(username: str) -> User:
    """Get the user's information."""
    sql = get_sql("user-fetch-info")

    # Start by getting the user's account info
    with connect_to_db() as db:
        db.execute(sql, {"username": username})
        user_info = convert_int_to_bool(dict(db.fetchone()))

    # Get the user's token permissions
    token_perms: dict = api.get(
        "api-key", user_token=False, params={"token": user_info["api_token"]}
    )

    # Store the permissions in a dataclass too
    token_perms = {k: v for k, v in token_perms.items() if k.startswith("has_")}
    token = Token(user_info["api_token"], **token_perms)
    return User(username, **user_info), token


def login(username: str, password: str) -> bool:
    """Atempt to login a user."""
    # Query the database for this username
    sql = get_sql("user-login")
    with connect_to_db() as db:
        db.execute(sql, {"username": username.strip()})
        user_pass = db.fetchone()

    # That username can't be found
    if user_pass is None:
        return False

    # Confirm this is a correct password
    return pbkdf2_sha256.verify(password.strip(), user_pass["password"])


def set_last_login(username: str) -> Literal[True]:
    """Update this user's last login datetime."""
    sql = get_sql("user-login-update")
    with connect_to_db() as db:
        db.execute(sql, {"username": username.strip()})
    return True
