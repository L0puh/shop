from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import DataRequired, Length

class UserForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=5, max=10) ])
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    repeat_password = PasswordField('repear_password', validators=[DataRequired()])
