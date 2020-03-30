from flask import Flask, render_template
from flask_login import LoginManager

from webapp.db import db
from webapp.user.models import User
from webapp.config import SECRET_KEY
from webapp.user.forms import LoginForm
from webapp.register.forms import RegisterForm

from webapp.user.views import blueprint as user_blueprint
from webapp.admin.views import blueprint as admin_blueprint
from webapp.register.views import blueprint as register_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(register_blueprint)


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def index():
        return render_template('base.html')

    @app.route('/profile')
    def profile():
        return render_template('profile.html')

    @app.route('/about')
    def about():
        return render_template('about.html')


    if __name__ == '__main__':
        app.run(debug=True)

    return app
