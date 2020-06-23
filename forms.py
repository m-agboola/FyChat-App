from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError

from models import User

class RegistrationForm(FlaskForm):
    """
    Registration form
    """
    username = StringField('username_label', 
            validators=[InputRequired(message="Username required"), Length(min=4, max=25, 
            message="Usernane must be between 4 and 25 characters")])
    
    password = PasswordField('password_label', 
            validators=[InputRequired(message="Password required"), Length(min=4, max=25, 
            message="Password must be between 4 and 25 characters")])
    
    confirm_password = PasswordField('confirm_password_label',
            validators=[InputRequired(message="Username required"), EqualTo('password', message="Password must match")])
    
    submit_button = SubmitField('Create')
    
    def validate_username(self, username):
        user_object = User.query.filter_by(username=username.data).first()
        if user_object:
            raise ValidationError("Username already exists. Select a different username.")