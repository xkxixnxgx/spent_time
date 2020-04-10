from flask_wtf import FlaskForm
from wtforms import StringField


class AboutForm(FlaskForm):
    about_form = StringField('About', render_kw={"class": "alert alert-secondary"})
