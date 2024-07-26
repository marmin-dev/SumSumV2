from langchain_community.chat_models import ChatOpenAI
from langchain_core.messages import SystemMessage
from langchain_core.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from app import db
from models import Message, User
import os


GPT_KEY = os.environ.get('CHAT_KEY')
os.environ["OPENAI_API_KEY"] = GPT_KEY


# 메시지 보냈을 시
def post_message(message: str):
    # 템플릿 시스템 프롬프트 추가
    template = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content= "너의 이름은 수희 야. 반말로 대답해."),
            HumanMessagePromptTemplate.from_template("{text}")
        ]
    )
    # 언어 모델 선택
    llm = ChatOpenAI(
        model="ft:gpt-3.5-turbo-0125:personal:suheezebal:9lHopkNl",
        temperature=0.4
    )
    reply = llm(template.format_messages(text=message))
    message_model = Message(question=message, reply=reply.content)
    db.session.add(message_model)
    db.session.commit()
    return message_model.to_dict()

# 유저 찾거나 저장 찾아보고 -> 없을 시 저장
def create_user(user_ip, username):
    existed_user = User.query.filter_by(connect_ip=user_ip).filter_by(username=username).first()
    if not existed_user:
        new_user = User(username=username, connectip=user_ip)
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict()
    else:
        return existed_user.to_dict()

# 해당 유저가 보낸 메시지 확인
def get_message_by_user(user_ip, username):
    messages = (Message.query
                .join(User, Message.user_id == User.user_id)
                .filter(User.connect_ip == user_ip)
                .filter(User.username == username)
                .order_by(Message.message_id.desc())
                .all()
                )
    return messages
