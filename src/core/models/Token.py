from dataclasses import dataclass


__all__ = ["Token"]


@dataclass
class Token:
    """Dataclass to hold API Token permissions."""

    token: str
    has_api_key: bool
    has_archive: bool
    has_broadcast: bool
    has_host: bool
    has_prompt: bool
    has_settings: bool
    has_subscription: bool
