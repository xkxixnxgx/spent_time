from webapp.db import db

from datetime import datetime
from sqlalchemy.orm import relationship


class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_add = db.Column(db.String, nullable=False)
    track_name = db.Column(db.String, unique=True, nullable=False)
    total_time = db.Column(db.Integer, nullable=True)
    time_sum = db.Column(db.Integer, nullable=False, default=0)

    def points_count(self):
        return Point.query.filter(Point.track_id == self.id).count()

    def __repr__(self):
        return '<Track {}, id = {}>'.format(self.track_name, self.id)


class Point(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_add = db.Column(db.DateTime, nullable=False, default=datetime.now())
    time_value = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)
    track_id = db.Column(db.Integer, db.ForeignKey('track.id'), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)
    track = relationship('Track', backref='points')
    user = relationship('User', backref='points')

    def __repr__(self):
        return '<Point = {}>'.format(self.id)
