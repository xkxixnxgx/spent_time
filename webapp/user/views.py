from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from webapp.user.forms import LoginForm
from webapp.user.models import User

blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = 'Log in'
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.user_email == form.user_email.data).first()
        if user and user.check_password(form.user_password.data):
            login_user(user, remember=form.remember_me.data)
            flash('You have successfully logged in', 'success')
            return redirect(url_for('user.login'))

    flash('The password is incorrect', 'warning')
    return redirect(url_for('login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged out', 'success')
    return redirect(url_for('index'))
