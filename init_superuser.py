import sqlite3
from os import fspath
from pathlib import Path

import sys_vars
from passlib import pwd
from passlib.hash import pbkdf2_sha256

from src.core import api


def main():
    """Create the initial admin superuser."""
    # Ask for the username
    username = input("Enter the desired username: ").strip()
    if not username:
        input("Please provide a username!")
        raise SystemExit(1)

    # Generate a random password and hash it
    password = pwd.genword("strong")
    password_hashed = pbkdf2_sha256.hash(password)

    # Create an API token for this user, giving it all permissions
    # TODO Use app token
    request_body = {
        "desc": f"Admin superuser {username} API key",
        "has_api_key": True,
        "has_archive": True,
        "has_broadcast": True,
        "has_host": True,
        "has_prompt": True,
        "has_settings": True,
        "has_subscription": True,
    }
    created_token = api.post("api-key", data=request_body)["token"]

    # Connect to the database
    # TODO Handle creating the schema if needed
    db = sqlite3.connect((Path() / "db" / "database.db"))
    cursor = db.cursor()

    # Record this user in the local db
    sql_create_user = (Path() / "db" / "1-user-create.sql").read_text()
    sql_create_token = (Path() / "db" / "4-user-update-api-token.sql").read_text()
    cursor.execute(
        sql_create_user,
        {"username": username, "password": password_hashed, "is_superuser": 1},
    )

    # Record the API token created for the user
    cursor.execute(
        sql_create_token,
        {"username": username, "api_token": created_token},
    )
    db.close()

    # Report the creation results
    print(f"Superuser {username} created with password {password}")
    input("Press enter to close.")
    raise SystemExit(0)


if __name__ == "__main__":
    main()
