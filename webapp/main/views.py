from flask import Blueprint, render_template
from webapp.main.forms import AboutForm

blueprint = Blueprint('main', __name__)


@blueprint.route('/')
def main():
    title = '10,000-Hour Rule'
    return render_template('main/main.html', page_title=title)

