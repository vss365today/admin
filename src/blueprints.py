from flask import Blueprint

from src.core.auth_helpers import authorize_blueprint


def _factory(
    partial_module_string: str, url_prefix: str, protected: bool = False
) -> Blueprint:
    # Create the blueprint
    blueprint = Blueprint(
        partial_module_string,
        f"src.views.{partial_module_string}",
        url_prefix=url_prefix,
    )

    # This endpoint is not to be publicly used,
    # protect the endpoint with an authorization routine
    if protected:
        blueprint.before_request(authorize_blueprint)
    return blueprint


root = _factory("root", "/")
keys = _factory("keys", "/keys", True)
config = _factory("config", "/config", True)
hosts = _factory("hosts", "/hosts", True)
prompts = _factory("prompts", "/prompts", True)

all_blueprints = (keys, root, config, hosts, prompts)
