from flask import Flask
from flask_login import LoginManager

from webapp.db import db
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

from webapp.user.models import User
from webapp.config import SECRET_KEY, WTF_CSRF_TIME_LIMIT
from webapp.user.forms import LoginForm

from webapp.user.views import blueprint as user_blueprint
from webapp.tracks.views import blueprint as tracks_blueprint
from webapp.about.views import blueprint as about_blueprint
from webapp.main.views import blueprint as main_blueprint

def create_app():
    app = Flask(__name__)
    csrf = CSRFProtect(app)
    csrf.init_app(app)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(about_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(tracks_blueprint)
    app.register_blueprint(main_blueprint)


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    if __name__ == '__main__':
        app.run(debug=True)

    return app
