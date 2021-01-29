from flask import abort, flash, redirect, render_template, request, url_for
from src.blueprint import bp_config as config
from src.core import api, forms
from src.core.helpers import split_hashtags_into_list


def save_json_config(config):
    ...


@config.route("/")
def index():
    # Get the finder settings from the API
    finder_settings = api.get("settings")
    finder_timings = api.get("settings", "timings")
    render_opts = {
        "form_prompt_position": forms.FormPromptPosition(),
        "form_identifier_hashtags": forms.FormIdentifierHashtags(),
        "form_filtered_hashtags": forms.FormFilteredHashtags(),
        "form_finder_timings": forms.FormFinderTimings(),
        "finder_settings": finder_settings,
    }

    # Because wtforms doesn't permit setting a default <textarea> body
    # in Jinja2, we must set it here, in code :\
    render_opts["form_identifier_hashtags"].hashtags.data = "\n".join(
        finder_settings["identifiers"]
    )
    render_opts["form_filtered_hashtags"].hashtags.data = "\n".join(
        finder_settings["additionals"]
    )
    render_opts["form_finder_timings"].timings.data = "\n".join(finder_timings)
    return render_template("config/index.html", **render_opts)


@config.route("/save", methods=["POST"])
def save():
    abort(404)

    # Get the submitted form data and current config
    form_data = request.form
    current_config = api.get("settings")

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
