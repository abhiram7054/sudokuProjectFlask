from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    
class Game(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100))
    name = db.Column(db.String(100))
    mode = db.Column(db.String(20))
    score = db.Column(db.Integer)
