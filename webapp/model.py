from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String, unique=True, nullable=False)
    user_password = db.Column(db.String, nullable=False)
    date_reg = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.user_email)


