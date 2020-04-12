from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from webapp.tracks.forms import TrackForm, TrackAddForm, PointAddForm
from webapp.tracks.models import Track, Point
from datetime import datetime

from webapp import db

# в данном случае необходимо импортировать модель Track, т.к. при миграции базы данных
# migrate смотрит на подключенные blueprints, т.е. по факту на файлы views и импортирует модели для миграции
from webapp.tracks.models import Track

blueprint = Blueprint('tracks', __name__,  url_prefix='/tracks')


@blueprint.route('/')
def tracks_points():
    tittle = 'Tracks'
    tracks_form = TrackForm()
    return render_template('tracks/tracks.html', page_title=tittle, form=tracks_form)


@blueprint.route('/track_add', methods=['POST'])
def track_add():
    tracks_form = TrackAddForm()
    if tracks_form.validate_on_submit():
        date_now = datetime.now()
        date_reg = date_now.strftime('%d.%m.%Y')
        new_track = Track(date_add=date_reg,
                          track_name=tracks_form.track_name.data,
                          total_time=tracks_form.total_time.data,
                          time_sum=0,
                          )
        db.session.add(new_track)
        db.session.commit()
        flash('You added the new track.')
        return redirect(url_for('tracks.tracks_points'))
    else:
        for field, errors in tracks_form.errors.items():
            for error in errors:
                flash(f"Error in the field {getattr(tracks_form, field).label.text}: {error}")
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


@blueprint.route('/analytics')
def analytics():
    title = 'Analytics'
    tracks_form = TrackForm()
    points_form = Point
    return render_template('tracks/analytics.html', page_title=title, form=tracks_form)