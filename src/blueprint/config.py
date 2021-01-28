from flask import request
from flask import abort, flash, redirect, render_template, url_for

from src.blueprint import bp_config as config
from src.core.helpers import split_hashtags_into_list


def load_json_config() -> dict:
    return {}


def save_json_config(config):
    ...


@config.route("/")
def index():
    render_opts = {}
    return render_template("config/index.html", **render_opts)


@config.route("/save", methods=["POST"])
def save():
    # Get the submitted form data and current config
    form_data = request.form
    current_config = load_json_config()

    # Map the form field names to their config names
    mapping = {
        "input-hashtags-identifier": "identifiers",
        "input-hashtags-filter": "additionals",
        "input-hashtag-posi": "word_index",
    }

    # Map field specific converters to format the data correctly
    converters = {
        "word_index": lambda x: int(x) - 1 if int(x) - 1 >= 0 else 0,
        "identifiers": split_hashtags_into_list,
        "additionals": split_hashtags_into_list,
    }

    # Determine which form was submitted and cleanup the data
    found_key = {
        mapping[key]: converters[mapping[key]](value)
        for key, value in form_data.items()
        if key in mapping
    }

    # Update the config with the new value,
    # clobbering whatever value we previously had
    current_config.update(found_key)

    # Save the updated config
    save_json_config(current_config)

    # Go back to the config page
    flash("Configuration successfully updated.")
    return redirect(url_for("admin.config"))
