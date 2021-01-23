from sqlite3 import Row
from typing import Optional

from src.core.database.core import connect_to_db, get_sql


__all__ = ["get_info", "login"]


def get_info(username: str) -> Optional[Row]:
    """Get the user's information."""
    sql = get_sql("user-fetch-info")
    with connect_to_db() as db:
        db.execute(sql, {"username": username})
        return db.fetchone()


def login(username: str, password: str) -> Optional[Row]:
    """Atempt to login a user."""
    sql = get_sql("user-login")
    with connect_to_db() as db:
        db.execute(sql, {"username": username, "password": password})
        return db.fetchone()
