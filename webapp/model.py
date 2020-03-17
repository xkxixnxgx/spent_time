from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String, unique=True, nullable=False)
    user_password = db.Column(db.String, nullable=False)
    user_rank = db.Column(db.String, nullable=False)
    date_reg = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.user_email)


class about_user(db.Model):
    users_id = id.users(db.Integer, foreign_key=True)
    picture_user = db.Column(db.String, nullable=True)
    login_users = db.Column(db.String, nullable=True)

    def __repr__(self):
        return '<User {}>'.format(self.user_email)


class tracks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    users_id = id.users (db.Integer, foreign_key=True)
    # тут необходимо уточнить, что для конкретного пользователя имена треков уникальны, в то время как для общей
    # базы они могут повторятся у нескольких пользователей
    track_name = db.Column(db.String, unique=True, nullable=False)
    track_value = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Track {}>'.format(self.tracks_name)


