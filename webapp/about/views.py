from flask import Blueprint, render_template
from webapp.about.forms import AboutForm

blueprint = Blueprint('about', __name__)


@blueprint.route('/about')
def about():
    title = 'about'
    about_form = AboutForm()
    return render_template('about/about.html', page_title=title, form=about_form)
