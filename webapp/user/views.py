from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from webapp.user.forms import LoginForm, StartForm, RegisterForm, AdminForm, ProfileForm
from webapp.user.models import User
from webapp.user.decorators import admin_required
from datetime import datetime

from webapp import db

blueprint = Blueprint('user', __name__, url_prefix='/user')


@blueprint.route('/')
def index():
    title = 'start'
    start_form = StartForm()
    return render_template('user/index.html', page_title=title, form=start_form)


@blueprint.route('/register')
def register():
    title = 'Register'
    if current_user.is_authenticated:
        return redirect(url_for('user.index'))
    reg_form = RegisterForm()
    return render_template('user/register.html', page_title=title, form=reg_form)


@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegisterForm()
    if form.validate_on_submit():
        date_now = datetime.now()
        date_reg = date_now.strftime('%d.%m.%Y')
        new_user = User(user_email=form.user_email.data, user_password=form.user_password.data, role='user',
                        date_reg=date_reg)
        new_user.set_password(form.user_password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('You have successfully registered.')
        return redirect(url_for('user.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in the field {getattr(form, field).label.text}: {error}")
        return redirect(url_for('user.register'))


@blueprint.route('/login')
def login():
    title = 'Log in'
    if current_user.is_authenticated:
        return redirect(url_for('user.index'))
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

    flash('Incorrect data. Try again.', 'warning')

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
        admin_form = AdminForm()
        return render_template('user/admin.html', page_tittle=title, form=admin_form)
    else:
        return 'You are not admin.'


@blueprint.route('/profile')
def profile():
    if current_user.is_authenticated:
        title = 'Your profile'
        profile_form = ProfileForm()
        return render_template('user/profile.html', page_tittle=title, form=profile_form)
    else:
        flash('You are not authenticated. Please login.')
        return redirect(url_for('user.login'))
