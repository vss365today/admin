from flask_wtf import FlaskForm
from wtforms.fields.simple import PasswordField, SubmitField, TextField
from wtforms.validators import DataRequired


__all__ = ["FormUserLogin"]


class FormUserLogin(FlaskForm):
    username = TextField(
        "Username",
        id="form-login-username",
        validators=[DataRequired()],
        render_kw={"placeholder": "IAmAWriter"},
    )

    password = PasswordField(
        "Password",
        id="form-login-password",
        validators=[DataRequired()],
    )
    submit = SubmitField("Login")
