from typing import Callable, Optional

from flask import Blueprint

from src.core.auth_helpers import authorize_blueprint


def _factory(
    partial_module_string: str, url_prefix: str, protected: bool = False
) -> Blueprint:
    # Create the blueprint
    blueprint = Blueprint(
        partial_module_string,
        f"src.blueprint.{partial_module_string}",
        url_prefix=url_prefix,
    )

    # This endpoint is not to be publicly used,
    # protect the endpoint with an authorization routine
    if protected:
        blueprint.before_request(authorize_blueprint)
    return blueprint


bp_root = _factory("root", "/")
bp_config = _factory("config", "/config", True)
bp_host = _factory("host", "/host", True)
bp_prompt = _factory("prompt", "/prompt", True)

all_blueprints = (bp_root, bp_config, bp_host, bp_prompt)
