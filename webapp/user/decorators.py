from functools import wraps

from flask import current_app, flash, g, request, redirect, url_for
from flask_login import config, current_user

def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if request.method in config.EXEMPT_METHODS:
            return func(*args, **kwargs)
        elif current_app.config.get('LOGIN_DISABLED'):
            return func(*args, **kwargs)
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        elif not current_user.is_admin:
            flash('You are not admin', 'warning')
            return redirect(url_for("main.main"))
        return func(*args, **kwargs)
    return decorated_view

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        g.user = current_user
        if g.user is None:
            return redirect(url_for('user.login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function