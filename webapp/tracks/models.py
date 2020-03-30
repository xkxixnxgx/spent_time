from webapp.db import db


class Tracks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # users_id = id.users (db.Integer, foreign_key=True)
    # тут необходимо уточнить, что для конкретного пользователя имена треков уникальны, в то время как для общей
    # базы они могут повторятся у нескольких пользователей
    track_name = db.Column(db.String, unique=True, nullable=False)
    track_value = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<Track {}>'.format(self.track_name)