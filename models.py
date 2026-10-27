from db import db

class User(db.Model):
    login=db.Column(db.String(50),unique=True,nullable=False)
    password=db.Column(db.String(200),nullable=False)
    id=db.Column(db.Integer,primary_key=True)
class Chat(db.Model):
    room_id=db.Column(db.Integer,primary_key=True)
    room_name=db.Column(db.String(50))
class Chat_users(db.Model):
    room_id=db.Column(db.Integer)
    id=db.Column(db.Integer,primary_key=True)
    user_login=db.Column(db.Text)