from flask import Blueprint, render_template, flash, redirect, url_for, request
from webapp.register.forms import RegisterForm


blueprint = Blueprint('register', __name__, url_prefix='/register')


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
