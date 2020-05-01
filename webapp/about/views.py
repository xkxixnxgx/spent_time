from flask import Blueprint, render_template

blueprint = Blueprint('about', __name__)


@blueprint.route('/about')
def about():
    title = 'About us'
    return render_template('about/about.html', page_title=title)
