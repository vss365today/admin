import sqlite3
from pathlib import Path

from passlib import pwd
from passlib.hash import pbkdf2_sha256

from src.core import api


def main() -> None:
    """Create the initial admin superuser."""
    # TODO: This whole thing is broken atm
    print("This script is broken. Fix it to use sqlalchemy and API v2.")
    return None

    # Ask for the username
    username = input("Enter the desired username: ").strip()
    if not username:
        input("A username must be provided.")
        return None

    # Generate a random password and hash it
    password = pwd.genword("secure", length=20)
    password_hashed = pbkdf2_sha256.hash(password)

    # Create an API token for this user, giving it all permissions
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
    created_token = api.post("api-key", user_token=False, json=request_body)["token"]

    # Connect to the database
    db = sqlite3.connect((Path() / "db" / "database.db"))
    cursor = db.cursor()

    # Check if the schema exists already
    sql_schema_exists = (Path() / "db" / "5-check-if-schema-exists.sql").read_text()
    cursor.execute(
        sql_schema_exists,
        {"table_name": "users"},
    )

    # The schema doesn't exist, create it
    if cursor.fetchone() is None:
        cursor.execute((Path() / "db" / "0-schema.sql").read_text())

    # Record this user and API token in the local db
    sql_create_user = (Path() / "db" / "1-user-create.sql").read_text()
    sql_create_token = (Path() / "db" / "4-user-update-api-token.sql").read_text()
    cursor.execute(
        sql_create_user,
        {"username": username, "password": password_hashed, "is_superuser": 1},
    )
    cursor.execute(
        sql_create_token,
        {"username": username, "api_token": created_token},
    )
    db.commit()
    db.close()

    # Report the creation results
    print(f"Superuser {username} created with password {password}")
    input("Press enter to close.")
    return None


if __name__ == "__main__":
    main()
