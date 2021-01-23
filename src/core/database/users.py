from sqlite3 import Row
from typing import Optional

from passlib.hash import pbkdf2_sha256

from src.core.database.core import connect_to_db, get_sql


__all__ = ["get_info", "login"]


def get_info(username: str) -> Optional[Row]:
    """Get the user's information."""
    sql = get_sql("user-fetch-info")
    with connect_to_db() as db:
        db.execute(sql, {"username": username})
        return db.fetchone()


def login(username: str, password: str) -> bool:
    """Atempt to login a user."""
    # Query the  database for this username
    sql = get_sql("user-login")
    with connect_to_db() as db:
        db.execute(sql, {"username": username.strip()})
        user_pass = db.fetchone()

    # That username can't be found
    if user_pass is None:
        return False

    # Confirm this is a correct password
    return pbkdf2_sha256.verify(password.strip(), user_pass["password"])
