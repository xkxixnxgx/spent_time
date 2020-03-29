from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


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



class Tracks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # users_id = id.users (db.Integer, foreign_key=True)
    # тут необходимо уточнить, что для конкретного пользователя имена треков уникальны, в то время как для общей
    # базы они могут повторятся у нескольких пользователей
    track_name = db.Column(db.String, unique=True, nullable=False)
    track_value = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Track {}>'.format(self.track_name)


