import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator


__all__ = ["connect_to_db", "get_sql"]


@contextmanager
def connect_to_db() -> Iterator[sqlite3.Cursor]:
    """Context manager to connect to the local database."""
    db = sqlite3.connect((Path() / "db" / "database.db"))
    cursor = db.cursor()
    try:
        yield cursor
    finally:
        db.close()


def get_sql(filename: str) -> str:
    """Get the contents of a SQL script."""
    return (Path() / "db" / f"{filename}.sql").read_text()
