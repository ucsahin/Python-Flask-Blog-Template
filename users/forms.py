# users --> forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed, FileRequired # for image png files

from flask_login import current_user
from setup import app
from models import User

# WTF-Forms that are used for user views: Login, Register, Update

class LoginForm(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords must match!')])
    pass_confirm = PasswordField('Password again: ', validators=[DataRequired()])
    username = StringField('Username: ', validators=[DataRequired()])
    submit = SubmitField('Register')

    with app.app_context():
        def validate_email(self, email):
            if User.query.filter_by(email=email.data).first():
                raise ValidationError('Email has already been registered')
        def validate_username(self, username):
            if User.query.filter_by(username=username.data).first():
                raise ValidationError('Username has already been taken')


class UpdateUserForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()])
    about_text = TextAreaField('About: ', validators=[DataRequired()])
    picture = FileField('Select image: ', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')
