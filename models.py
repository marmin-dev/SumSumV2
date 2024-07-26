from datetime import datetime
from app import db


class Message(db.Model):
    __tablename__ = 'message'
    message_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    question = db.Column(db.String(1000), nullable=False)
    reply = db.Column(db.Text, unique=True, nullable=False)
    regdate = db.Column(db.DateTime, default=datetime.utcnow)

    # Constructor
    def __init__(self, question, reply):
        self.user_id = 1
        self.question = question
        self.reply = reply

    def to_dict(self):
        return {
            'question': self.question,
            'reply': self.reply
        }
    def __repr__(self):
        return f'<Message {self.user_id}>'


# ip, username 으로 로그인하는 예제 (대역으로 할지)
class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=False)
    connect_ip = db.Column(db.String(100), nullable=False)
    regdate = db.Column(db.DateTime, default=datetime.utcnow)

    # Constructor
    def __init__(self, username, connectip):
        self.username = username
        self.connect_ip = connectip

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username' : self.username,
            'connect_ip': self.connect_ip
        }

    def __repr__(self):
        return f'<Message {self.user_id}>'





