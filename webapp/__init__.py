from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user

from webapp.model import db, User, Tracks
from webapp.config import SECRET_KEY
from webapp.forms import LoginForm


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/profile')
    def profile():
        return render_template('profile.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        title = 'Sign in'
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter(User.user_email == form.user_email.data).first()
            if user and user.check_password(form.user_password.data):
                login_user(user)
                flash('You have successfully logged in.')
                return redirect(url_for('index'))

        flash('The password is incorrect')
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        flash('You have successfully logged out.')
        return redirect(url_for('index'))

    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Hello admin!'
        else:
            return 'You are not admin!'

    if __name__ == '__main__':
        app.run(debug=True)

    return app
