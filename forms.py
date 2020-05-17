from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    """
    Registration form
    """
    head