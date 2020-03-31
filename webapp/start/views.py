from flask import Blueprint, render_template
from webapp.start.forms import StartForm

blueprint = Blueprint('start', __name__, url_prefix='/start')


@blueprint.route('/')
def login():
    title = 'start'
    start_form = StartForm()
    return render_template('start.html', page_title=title, form=start_form)