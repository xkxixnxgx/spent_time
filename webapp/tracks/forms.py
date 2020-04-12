from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, validators
from wtforms.validators import DataRequired, Length


class TrackForm(FlaskForm):
    # render_kw параметр в wtf, в котором можно указать то, что будет добавлено при отрисовке формы.
    # Мы добавляем класс из bootstrap из строки input class="form-control"
    track_name = StringField('Your track', render_kw={"class": "form-control"})
    total_time = StringField('Time, hours', render_kw={"class": "form-control"})
    size_time = IntegerField('Time, hours',
                             validators=[DataRequired()],
                             render_kw={"class": "progress-bar"}
                             )
    def validate_size_time(self, user_email):
        size_now = Track.query.filter_by(track_name=track_name.data).sum()
        if  100 < size_now < 0:
            raise ValidationError('Error is the accumulated time.')

class TrackAddForm(FlaskForm):
    # render_kw параметр в wtf, в котором можно указать то, что будет добавлено при отрисовке формы.
    # Мы добавляем класс из bootstrap из строки input class="form-control"
    track_name = StringField('Your track', render_kw={"class": "form-control"})
    total_time = StringField('Time, hours', render_kw={"class": "form-control"})
    track_add = SubmitField('Add track', render_kw={"class": "btn btn-success"})


class TrackEditForm(FlaskForm):
    track_name = StringField('Your track', render_kw={"class": "form-control"})
    total_time = StringField('Time, hours', render_kw={"class": "form-control"})
    save_edit = SubmitField('Save', render_kw={"class": "btn btn-success"})


class PointForm(FlaskForm):
    date_reg = StringField('Date', render_kw={"class": "table"})
    track_name = StringField('Track name', render_kw={"class": "table"})
    spent_time = StringField('Spent time', render_kw={"class": "table"})
    comment = StringField('Comment', render_kw={"class": "overflow-auto"})



class PointAddForm(FlaskForm):
    # render_kw параметр в wtf, в котором можно указать то, что будет добавлено при отрисовке формы.
    # Мы добавляем класс из bootstrap из строки input class="form-control"
    point = StringField('The point', render_kw={"class": "form-control"})
    time_value = StringField('Time, hours', render_kw={"class": "form-control"})
    point_add = SubmitField('Add point', render_kw={"class": "btn btn-success"})

