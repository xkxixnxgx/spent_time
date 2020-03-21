from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(50), nullable=False, unique=True)
    user_password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(10), index=True, nullable=False)
    date_reg = db.Column(db.Text, nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return '<User {}>'.format(self.username)


class About_user(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    picture_user = db.Column(db.String, nullable=True)
    username = db.Column(db.String(50),  nullable=True, index=True)

    def __repr__(self):
        return '<User {}>'.format(self.user_email)


class Tracks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # users_id = id.users (db.Integer, foreign_key=True)
    # тут необходимо уточнить, что для конкретного пользователя имена треков уникальны, в то время как для общей
    # базы они могут повторятся у нескольких пользователей
    track_name = db.Column(db.String, unique=True, nullable=False)
    track_value = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Track {}>'.format(self.track_name)


