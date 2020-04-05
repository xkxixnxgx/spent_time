from flask import Flask, render_template
from flask_login import LoginManager

from webapp.db import db
from flask_migrate import Migrate

from webapp.user.models import User
from webapp.config import SECRET_KEY
from webapp.user.forms import LoginForm

from webapp.user.views import blueprint as user_blueprint
from webapp.tracks.views import blueprint as tracks_blueprint
from webapp.about.views import blueprint as about_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(about_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(tracks_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    if __name__ == '__main__':
        app.run(debug=True)

    return app
