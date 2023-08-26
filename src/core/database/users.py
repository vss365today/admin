from datetime import datetime, timezone
from typing import Any
from passlib.hash import pbkdf2_sha256

from src.core.api import v2
from src.core.database.core import connect_to_db, convert_int_to_bool, get_sql
from sqlalchemy.exc import NoResultFound

# from src.core.models import User

from src.core.database.models import User, db


__all__ = ["get_info", "login", "set_last_login"]


def get_info(username: str) -> tuple[dict[str, Any], dict[str, Any]]:
    """Get the user's information."""
    # Get some account information
    account = (
        db.session.execute(
            db.select(
                User.username, User.api_token, User.is_superuser, User.date_last_login
            ).filter_by(username=username.strip())
        )
        .first()
        ._asdict()
    )

    # Get the account's token permissions
    token_perms: dict = v2.get("keys", account["api_token"], user_token=False)
    return account, token_perms


def login(username: str, password: str) -> bool:
    """Attempt to login a user."""
    # Try to pull an active account with the specified username
    try:
        account = db.session.execute(
            db.select(User).filter_by(username=username.strip(), is_active=True)
        ).scalar_one()

    # No account with that username exists
    except NoResultFound:
        return False

    # The specified password doesn't match what we have on file
    if not pbkdf2_sha256.verify(password.strip(), account.password):
        return False

    # We can successfully log in! Record the last login time and get out of here
    account.date_last_login = datetime.now(tz=timezone.utc)
    db.session.commit()
    del account
    return True
