from flask_wtf import FlaskForm
from wtforms.fields.html5 import IntegerField
from wtforms.fields.simple import PasswordField, SubmitField, TextField
from wtforms.validators import DataRequired, Length


__all__ = ["FormUserLogin", "FormPromptPosition"]


class FormUserLogin(FlaskForm):
    """User login form."""

    username = TextField(
        "Username",
        id="form-login-username",
        validators=[DataRequired()],
        render_kw={"placeholder": "vss365Writer"},
    )

    password = PasswordField(
        "Password",
        id="form-login-password",
        validators=[DataRequired()],
    )
    submit = SubmitField("Login")


class FormPromptPosition(FlaskForm):
    """Word prompt hashtag position form."""

    position = IntegerField(
        "Hashtag position",
        id="form-prompt-position",
        validators=[DataRequired(), Length(min=1)],
        render_kw={"step": "1", "placeholder": "1"},
    )
    submit = SubmitField("Save")
