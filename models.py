from datetime import datetime
from app import db


class Message(db.Model):
    __tablename__ = 'message'
    message_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    question = db.Column(db.String(1000), unique=True, nullable=False)
    reply = db.Column(db.Text, unique=True, nullable=False)
    regdate = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Message {self.user_id}>'