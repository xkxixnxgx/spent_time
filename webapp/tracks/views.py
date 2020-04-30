from flask import abort, Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from webapp.tracks.forms import TrackForm, TrackAddForm, PointForm, PointAddForm
from webapp.tracks.models import Track, Point
from webapp.user.models import User
from datetime import datetime

from webapp import db

# в данном случае необходимо импортировать модель Track, т.к. при миграции базы данных
# migrate смотрит на подключенные blueprints, т.е. по факту на файлы views и импортирует модели для миграции

blueprint = Blueprint('tracks', __name__,  url_prefix='/tracks')


@blueprint.route('/', method=['GET'])
def tracks_points():
    tittle = 'Tracks'
    tracks_form = TrackForm()
    point_form = PointForm()
    return render_template('tracks/tracks.html', page_title=tittle, form=tracks_form, point_form=point_form)


@blueprint.route('/track_add', methods=['POST'])
def track_add():
    track_add_form = TrackAddForm()
    if track_add_form.validate_on_submit():
        date_now = datetime.now()
        date_reg = date_now.strftime('%d.%m.%Y')
        new_track = Track(date_add=date_reg,
                          track_name=track_add_form.track_name.data,
                          total_time=track_add_form.total_time.data,
                          time_sum=0,
                          )
        db.session.add(new_track)
        db.session.commit()
        flash('You added the new track.')
        return redirect(url_for('tracks.tracks_points'))
    else:
        for field, errors in track_add_form.errors.items():
            for error in errors:
                flash(f"Error in the field {getattr(track_add_form, field).label.text}: {error}")
        return redirect(url_for('tracks.tracks_points'))


@blueprint.route('/tracks_update')
def track_update():
    title = 'Tracks'
    tracks_form = TrackAddForm()
    return redirect(url_for('tracks.tracks_points'))


@blueprint.route('/tracks_del')
def track_del():
    title = 'Tracks'
    tracks_form = TrackAddForm()
    return redirect(url_for('tracks.tracks_points'))


@blueprint.route('/points_add', methods=['POST'])
def point_add():
    point_add_form = PointAddForm()
    if point_add_form.validate_on_submit():
        date_now = datetime.now()
        new_point = Point(date_add=date_now,
                          time_value=point_add_form.time_value.data,
                          comment=point_add_form.comment.data,
                          )
        db.session.add(new_point)
        db.session.commit()
        flash('You added the new point.')
        return redirect(url_for('tracks.tracks_points'))
    else:
        for field, errors in point_add_form.errors.items():
            for error in errors:
                flash(f"Error in the field {getattr(point_add_form, field).label.text}: {error}")
        return redirect(url_for('tracks.tracks_points'))


@blueprint.route('/analytics/<int:track_id>')
def analytics(track_id):
    title = 'Analytics'
    tracks_form = TrackForm()
    my_track = Track.query.filter(Track.id == track_id).first()
    if not my_track:
        abort(404)
    return render_template('tracks/analytics.html', page_title=title, form=tracks_form, track=my_track)
