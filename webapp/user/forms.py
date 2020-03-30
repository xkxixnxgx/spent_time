from flask_wtf import FlaskForm

from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    # render_kw параметр в wtf, в котором можно указать то, что будет добавлено при отрисовке формы.
    # Мы добавляем класс из bootstrap из строки input class="form-control"
    user_email = StringField('Name', validators=[DataRequired()], render_kw={"class": "form-control"})
    user_password = PasswordField('Password', validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField('Remember me', default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField('Submit', render_kw={"class": "btn btn-primary"})


