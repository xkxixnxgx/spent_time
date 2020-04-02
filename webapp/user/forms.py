from flask_wtf import FlaskForm

from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class StartForm(FlaskForm):
    start_form = StringField('Start', render_kw={"class": "alert alert-secondary"})


class RegisterForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired(), Length(min=1, max=50)], render_kw={"class": "form-control"})
    user_email = StringField('Email', validators=[DataRequired(), Length(min=6, max=50), Email()], render_kw={"class": "form-control"})
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('confirm', message='Passwords do not match')], render_kw={"class": "form-control"})
    confirm = PasswordField('Confirm Password', render_kw={"class": "form-control"})
    submit = SubmitField('Submit', render_kw={"class": "btn btn-primary"})


class LoginForm(FlaskForm):
    # render_kw параметр в wtf, в котором можно указать то, что будет добавлено при отрисовке формы.
    # Мы добавляем класс из bootstrap из строки input class="form-control"
    user_email = StringField('Name', validators=[DataRequired()], render_kw={"class": "form-control"})
    user_password = PasswordField('Password', validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField('Remember me', default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField('Submit', render_kw={"class": "btn btn-primary"})


