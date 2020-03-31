from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class TrackForm(FlaskForm):
    # render_kw параметр в wtf, в котором можно указать то, что будет добавлено при отрисовке формы.
    # Мы добавляем класс из bootstrap из строки input class="form-control"
    track = StringField('Your track', render_kw={"class": "form-control"})
    time_all = StringField('Time in hours', render_kw={"class": "form-control"})
    submit = SubmitField('Add', render_kw={"class": "btn btn-success"})


