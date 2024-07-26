from sqlalchemy.orm import sessionmaker
from app import Session
from models import Message


def get_all_user():
    session = Session()
    messages = session.query(Message).all()
    session.close()
    return f"{messages[0].message_id}: {messages[0].question}, {messages[0].reply}"



