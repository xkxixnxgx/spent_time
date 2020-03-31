from flask import Blueprint, render_template
from webapp.about.forms import AboutForm

blueprint = Blueprint('about', __name__, url_prefix='/about')


@blueprint.route('/about')
def login():
    title = 'about'
    about_form = AboutForm()
    return render_template('about.html', page_title=title, form=about_form)