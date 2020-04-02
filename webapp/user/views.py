from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from webapp.user.forms import LoginForm, StartForm, RegisterForm
from webapp.user.models import User
from webapp.user.decorators import admin_required

blueprint = Blueprint('user', __name__, url_prefix='/user')


@blueprint.route('/')
def index():
    title = 'start'
    start_form = StartForm()
    return render_template('user/index.html', page_title=title, form=start_form)


@blueprint.route('/register', methods=['GET', 'POST'])
def register():
    title = 'Register'
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user_email = form.user_email.data

        flash('You are now registered and can log in', 'success')

        return redirect(url_for('login'))

    return render_template('user/register.html', page_title=title, form=form)


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
            return redirect(url_for('user.index'))

    flash('The password is incorrect', 'warning')
    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged out', 'success')
    return redirect(url_for("user.index"))


@blueprint.route('/admin')
@admin_required
def admin_index():
    if current_user.is_admin:
        title = 'admin console'
        return render_template('user/admin.html', page_tittle=title)
    else:
        return 'You is not admin.'