from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from webapp.db import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, index=True, primary_key=True)
    user_email = db.Column(db.String(50), nullable=False, unique=True)
    user_password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(10), index=True, nullable=True)
    date_reg = db.Column(db.Text, nullable=True)
    picture_user = db.Column(db.String, nullable=True)
    username = db.Column(db.String(50),  nullable=True, index=True)

    def set_password(self, user_password):
        self.user_password = generate_password_hash(user_password)

    def check_password(self, user_password):
        return check_password_hash(self.user_password, user_password)

    def __repr__(self):
        return '<User {}>'.format(self.user_email)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return '<User {}>'.format(self.user_email)