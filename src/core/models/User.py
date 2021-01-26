from dataclasses import dataclass


__all__ = ["User"]


@dataclass
class User:
    username: str
    api_token: str
    is_superuser: bool
    date_last_login: str
