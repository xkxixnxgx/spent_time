from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class LoginForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Submit', render_kw={"class": "btn btn-primary"})

class RegisterForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired(), Length(min=1, max=50)], render_kw={"class": "form-control"})
    user_email = StringField('Email', validators=[DataRequired(), Length(min=6, max=50), Email()], render_kw={"class": "form-control"})
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords do not match')], render_kw={"class": "form-control"})
    confirm = PasswordField('Confirm Password', render_kw={"class": "form-control"})
    submit = SubmitField('Submit', render_kw={"class": "btn btn-primary"})