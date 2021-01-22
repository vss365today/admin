from src.blueprint import bp_root as root


@root.route("/")
def index():
    return ""
