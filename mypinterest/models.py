from mypinterest import db, login_manager
from datetime import datetime, timezone
from flask_login import UserMixin


@login_manager.user_loader
def load_user(id_user):
    return User.query.get(id_user)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    pictures = db.relationship("Picture", backref="user", lazy=True)


class Picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(100), default="default.png")
    load_date = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
