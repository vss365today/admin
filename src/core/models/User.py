from dataclasses import InitVar, dataclass


__all__ = ["User"]


@dataclass
class User:
    username: str
    is_superuser: bool
    date_last_login: str

    # Do not store the token. We'll do that in the other model
    api_token: InitVar[str] = None
