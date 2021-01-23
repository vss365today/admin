import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator


__all__ = ["connect_to_db", "convert_int_to_bool", "convert_bool_to_int", "get_sql"]


@contextmanager
def connect_to_db() -> Iterator[sqlite3.Cursor]:
    """Context manager to connect to the local database."""
    db = sqlite3.connect((Path() / "db" / "database.db"))
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    try:
        yield cursor
    finally:
        db.close()


def convert_int_to_bool(data: dict) -> dict:
    """Convert all integer values into a Boolean."""
    for k, v in data.items():
        if type(v) == int:
            data[k] = bool(v)
    return data


def convert_bool_to_int(data: dict) -> dict:
    """Convert all Boolean values into a integer."""
    for k, v in data.items():
        if type(v) == bool:
            data[k] = int(v)
    return data


def get_sql(script_name: str) -> str:
    """Get the contents of a SQL script."""
    return (Path() / "db" / f"{script_name}.sql").read_text()
