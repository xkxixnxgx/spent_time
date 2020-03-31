from flask import Blueprint, render_template
from webapp.tracks.forms import TrackForm

blueprint = Blueprint('tracks', __name__, url_prefix='/tracks')


@blueprint.route('/tracks')
def login():
    title = 'tracks'
    tracks_form = TrackForm()
    return render_template('tracks.html', page_title=title, form=tracks_form)