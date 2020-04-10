from flask import Blueprint, render_template
from webapp.tracks.forms import TrackForm

# в данном случае необходимо импортировать модель Track, т.к. при миграции базы данных
# migrate смотрит на подключенные blueprints, т.е. по факту на файлы views и импортирует модели для миграции
from webapp.tracks.models import Track

blueprint = Blueprint('tracks', __name__)


@blueprint.route('/tracks')
def login():
    title = 'Tracks'
    tracks_form = TrackForm()
    return render_template('tracks/tracks.html', page_title=title, form=tracks_form)