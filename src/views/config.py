from functools import partial

from flask import flash, redirect, render_template, url_for

from src.blueprints import config
from src.core import api, forms
from src.core.helpers import split_hashtags_into_list


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
    render_opts["form_identifier_hashtags"].identifiers.data = "\n".join(
        hashtag.lstrip("#") for hashtag in finder_settings["identifiers"]
    )
    render_opts["form_filtered_hashtags"].filtered.data = "\n".join(
        finder_settings["additionals"]
    )
    render_opts["form_finder_timings"].timings.data = "\n".join(finder_timings)
    return render_template("config/index.html", **render_opts)


@config.route("/save", methods=["POST"])
def save():
    # Access all of the forms
    form_prompt_position = forms.FormPromptPosition()
    form_identifier_hashtags = forms.FormIdentifierHashtags()
    form_filtered_hashtags = forms.FormFilteredHashtags()
    form_finder_timings = forms.FormFinderTimings()

    # Get the form data regardless of what form was submitted
    form_data = {
        "identifiers": form_identifier_hashtags.identifiers.data,
        "additionals": form_filtered_hashtags.filtered.data,
        "word_index": form_prompt_position.position.data,
        "timings": form_finder_timings.timings.data,
    }

    # Map field specific converters to format the data correctly
    converters = {
        "word_index": lambda x: (
            int(x) - 1 if x is not None and int(x) - 1 >= 0 else None
        ),
        "identifiers": partial(split_hashtags_into_list, add_hashtag=True),
        "additionals": split_hashtags_into_list,
        "timings": lambda x: x.strip().split("\r\n") if x.strip() else None,
    }

    # Determine which form was submitted and cleanup the data
    cleaned_data = {
        key: converters[key](value)
        for key, value in form_data.items()
        if key in converters
    }

    # Update the timings only if needed
    if cleaned_data["timings"] is not None:
        api.put("settings", "timings", json={"timings": cleaned_data["timings"]})

    # Next, get the existing config
    current_config = api.get("settings")

    # We're changing something other than the timings
    if cleaned_data["timings"] is None:
        # Merge the changed config values into the existing config
        for key, value in cleaned_data.items():
            if value is not None:
                current_config[key] = value

        # Save the updated config
        api.put("settings", json=current_config)

    # Go back to the config page
    flash("Configuration successfully updated.")
    return redirect(url_for("config.index"))
