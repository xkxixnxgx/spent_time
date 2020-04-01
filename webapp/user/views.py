from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
from webapp.user.forms import LoginForm, StartForm, RegisterForm
from webapp.user.models import User
from webapp.user.decorators import admin_required

blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/')
def login():
    title = 'start'
    start_form = StartForm()
    return render_template('login.html', page_title=title, form=start_form)


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    title = 'Register'
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        user_email = form.user_email.data
        password = form.user_password.data

        flash('You are now registered and can log in', 'success')

        return redirect(url_for('login'))

    return render_template('register.html', page_title=title, form=form)


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


@blueprint.route('/admin')
@admin_required
def admin_index():
    title = "Панель управления"
    return render_template('admin/admin.html', page_title=title)


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged out', 'success')
    return redirect(url_for('/'))