from flask_wtf import FlaskForm
from wtforms import StringField


class StartForm(FlaskForm):
    start_form = StringField('Start', render_kw={"class": "alert alert-secondary"})
