from flask_wtf import FlaskForm
from wtforms.fields import (
    IntegerField,
    PasswordField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import InputRequired, Length

__all__ = ["FormUserLogin", "FormPromptPosition"]


class FormUserLogin(FlaskForm):
    """User login form."""

    username = StringField(
        "Username",
        id="form-login-username",
        validators=[InputRequired()],
        render_kw={"placeholder": "vss365Writer"},
    )

    password = PasswordField(
        "Password",
        id="form-login-password",
        validators=[InputRequired()],
    )
    submit = SubmitField("Login")


class FormPromptPosition(FlaskForm):
    """Word prompt hashtag position form."""

    position = IntegerField(
        "Hashtag position",
        id="form-prompt-position",
        validators=[InputRequired(), Length(min=1)],
        render_kw={"step": "1", "placeholder": "1", "inputmode": "numeric"},
    )
    submit = SubmitField("Save")


class FormIdentifierHashtags(FlaskForm):
    identifiers = TextAreaField(
        id="form-identifier-hashtags",
        render_kw={
            "cols": "20",
            "rows": "10",
            "spellcheck": "false",
            "autocapitalize": "none",
        },
    )
    submit = SubmitField("Save")


class FormFilteredHashtags(FlaskForm):
    filtered = TextAreaField(
        id="form-filtered-hashtags",
        render_kw={
            "cols": "20",
            "rows": "10",
            "spellcheck": "false",
            "autocapitalize": "none",
        },
    )
    submit = SubmitField("Save")


class FormFinderTimings(FlaskForm):
    timings = TextAreaField(
        id="form-finder-timings",
        render_kw={"cols": "20", "rows": "10", "spellcheck": "off"},
    )
    submit = SubmitField("Save")
