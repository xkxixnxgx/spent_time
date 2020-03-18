from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False, index=True)
    user_password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(10), index=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class About_user(db.Model):
    id = db.Column(db.Integer, nullable=False) # тут необходимо сделать ссылку по внешнему ключу на таблицу users
    picture_user = db.Column(db.String, nullable=True)
    user_email = db.Column(db.String, nullable=True)
    user_rank = db.Column(db.String, nullable=False)
    date_reg = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.user_email)


class Tracks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    users_id = id.users (db.Integer, foreign_key=True)
    # тут необходимо уточнить, что для конкретного пользователя имена треков уникальны, в то время как для общей
    # базы они могут повторятся у нескольких пользователей
    track_name = db.Column(db.String, unique=True, nullable=False)
    track_value = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Track {}>'.format(self.tracks_name)


