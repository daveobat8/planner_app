from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

class Note(db.Model):
    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    #allows sql to define the time at which a certain note was created
    date = db.Column(db.DateTime(timezone=True), default= func.now())
    #create a one to may relationship between user and notes
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    #the 150 sets a limit of the characters in the string
    #unique sets that two users cannot have the same email
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    #create a relationship with notes
    notes = db.relationship('Note')