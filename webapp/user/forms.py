from flask_wtf import FlaskForm
from flask_login import current_user

from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from flask_wtf.file import FileField, FileAllowed

from webapp.user.models import User


class StartForm(FlaskForm):
    start_form = StringField('Start', render_kw={"class": "alert alert-secondary"})


class RegisterForm(FlaskForm):
    username = StringField('Name',
                           validators=[DataRequired(), Length(min=1, max=30)],
                           render_kw={"class": "form-control"})
    user_email = StringField('Email',
                             validators=[DataRequired(), Length(min=6, max=50), Email()],
                             render_kw={"class": "form-control"})
    user_password = PasswordField('Password', validators=[DataRequired()], render_kw={"class": "form-control"})
    confirm = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('user_password', message='Passwords do not match')],
                            render_kw={"class": "form-control"})
    submit = SubmitField('Create account',
                         render_kw={"class": "btn btn-success"})

    def validate_user_email(self, user_email):
        user_count = User.query.filter_by(user_email=user_email.data).count()
        if user_count > 0:
            raise ValidationError('A user with this email address already exists.')



class LoginForm(FlaskForm):
    # render_kw параметр в wtf, в котором можно указать то, что будет добавлено при отрисовке формы.
    # Мы добавляем класс из bootstrap из строки input class="form-control"
    user_email = StringField('Email', validators=[DataRequired()], render_kw={"class": "form-control"})
    user_password = PasswordField('Password', validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField('Remember me', default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField('Log in', render_kw={"class": "btn btn-success"})


class AdminForm(FlaskForm):
    admin_form = StringField('Admin', render_kw={"class": "alert alert-secondary"})


class ProfileForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired(), Length(min=1, max=50)],
                           render_kw={"class": "form-control"})
    user_email = StringField('Email', validators=[DataRequired(), Length(min=6, max=50), Email()],
                             render_kw={"class": "form-control"})
    user_password = PasswordField('Password',
                                  validators=[DataRequired(), EqualTo('confirm', message='Passwords do not match')],
                                  render_kw={"class": "form-control"})
    picture = FileField('Update Profile Picture',  validators=[FileAllowed(['jpg', 'png'])], render_kw={"class": "form-control"})
    submit = SubmitField('Update', render_kw={"class": "btn btn-success"})

    def validate_email(self, user_email):
        if user_email.data != current_user.user_email:
            user = User.query.filter_by(user_email=user_email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')