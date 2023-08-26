import sys
from pathlib import Path

from passlib import pwd
from passlib.hash import pbkdf2_sha256

# We have to add the app path to the path to get the db
APP_ROOT = Path(__file__).parent.parent
sys.path.insert(0, APP_ROOT.as_posix())

from db.dummy_db import create_app
from src.core.api import v2
from src.core.database.models import User, db


def main() -> None:
    """Create the initial admin superuser."""
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
        "has_archive": True,
        "has_notifications": True,
        "has_hosts": True,
        "has_keys": True,
        "has_prompts": True,
        "has_emails": True,
    }
    created_token = v2.post("keys/", user_token=False, json=request_body)["token"]

    # Record this user and API token in the local db
    app = create_app()
    with app.app_context():
        u = User(
            username=username,
            password=password_hashed,
            api_token=created_token,
            is_active=True,
            is_superuser=True,
        )
        db.session.add(u)
        db.session.commit()

    # Report the creation results
    print(f"Superuser {username!r} created with password {password!r}")
    input("Press enter to close.")
    return None


if __name__ == "__main__":
    main()
