from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user
from webapp.user.forms import LoginForm, StartForm, RegisterForm, AdminForm, ProfileForm
from webapp.user.models import User
from webapp.user.decorators import admin_required
from datetime import datetime
from webapp.user.utils import save_picture

from webapp import db

blueprint = Blueprint('user', __name__, url_prefix='/user')



@blueprint.route('/register')
def register():
    title = 'Register'
    if current_user.is_authenticated:
        return redirect(url_for('user.login'))
    reg_form = RegisterForm()
    return render_template('user/register.html', page_title=title, form=reg_form)


@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegisterForm()
    if form.validate_on_submit():
        date_now = datetime.now()
        date_reg = date_now.strftime('%d.%m.%Y')
        new_user = User(username=form.username.data, user_email=form.user_email.data, user_password=form.user_password.data, role='user',
                        date_reg=date_reg)
        new_user.set_password(form.user_password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('You have successfully registered.', 'success')
        return redirect(url_for('user.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in the field {getattr(form, field).label.text}: {error}", 'warning')
        return redirect(url_for('user.register'))


@blueprint.route('/login')
def login():
    title = 'Log in'
    if current_user.is_authenticated:
        return redirect(url_for('tracks.login'))
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
            return redirect(url_for('tracks.tracks_points'))
        else:
            flash('Login nsuccessful. Please check email and password', 'warning')
    return redirect(url_for('user.login'))
        


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('You have successfully logged out', 'success')
    return redirect(url_for("main.main"))


@blueprint.route('/admin')
@admin_required
def admin_index():
    if current_user.is_admin:
        title = 'Admin console'
        admin_form = AdminForm()
        return render_template('user/admin.html', page_tittle=title, form=admin_form)
    else:
        return redirect(url_for("main.main"))

@blueprint.route('/profile', methods=['GET', 'POST'])
def profile():
    if current_user.is_authenticated:
        title = 'My profile'
        form = ProfileForm()
        if form.validate_on_submit():
            if form.picture.data:
                picture_file = save_picture(form.picture.data)
                current_user.image_file = picture_file
            current_user.username = form.username.data
            current_user.user_email = form.user_email.data
            db.session.commit()
            flash('Your profile has been updated', 'success')
            return redirect(url_for('user.profile'))
        elif request.method == 'GET':
            form.username.data = current_user.username
            form.user_email.data = current_user.user_email
        image_file = url_for('static', filename='profile_pics/' + current_user.picture)
        return render_template('user/profile.html', page_title=title, image_file=image_file, form=form)
    else:
        flash('You are not authenticated. Please login.', 'warning')
        return redirect(url_for('user.login'))
