from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_login import LoginManager, current_user, login_required, login_user, logout_user

from webapp.model import db, User, Tracks
from webapp.config import SECRET_KEY
from webapp.forms import LoginForm, RegisterForm


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

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        title = 'Register'
        form = RegisterForm(request.form)
        if request.method == 'POST' and form.validate():
            username = form.username.data
            user_email = form.user_email.data
            password = form.password.data

            flash('You are now registered and can log in', 'success')

            return redirect(url_for('login'))

        return render_template('register.html', page_title=title, form=form)

    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        title = 'Log in'
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter(User.user_email == form.user_email.data).first()
            if user and user.check_password(form.user_password.data):
                login_user(user)
                flash('You have successfully logged in', 'success')
                return redirect(url_for('index'))

        flash('The password is incorrect', 'warning')
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        flash('You have successfully logged out', 'success')
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
