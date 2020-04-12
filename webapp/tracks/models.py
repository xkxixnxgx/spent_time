from webapp.db import db


class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # users_id = id.users (db.Integer, foreign_key=True)
    # тут необходимо уточнить, что для конкретного пользователя имена треков уникальны, в то время как для общей
    # базы они могут повторятся у нескольких пользователей
    date_add = db.Column(db.String, nullable=False)
    track_name = db.Column(db.String, unique=True, nullable=False)
    total_time = db.Column(db.Integer, nullable=True)
    time_sum = db.Column(db.Integer, nullable=True)


    def __repr__(self):
        return '<Track {}, id = {}>'.format(self.track_name, self.id)


class Point(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_add = db.Column(db.String, nullable=False)
    date_point = db.Column(db.String, nullable=False)
    time_value = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<id = {}>'.format(self.id)
