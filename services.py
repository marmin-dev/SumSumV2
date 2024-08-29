from langchain_community.chat_models import ChatOpenAI
from langchain_core.messages import SystemMessage
from langchain_core.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from app import db
from models import Message, User
import os


GPT_KEY = os.environ.get('CHAT_KEY')
os.environ["OPENAI_API_KEY"] = GPT_KEY


# 메시지 보냈을 시
def post_message(message: str, username: str, client_ip):
    user = create_user(user_ip=client_ip, username=username)
    # 템플릿 시스템 프롬프트 추가
    template = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content= "너의 이름은 수희 이고 나이는 22살이야. 반말로 대답해."),
            HumanMessagePromptTemplate.from_template("{text}")
        ]
    )
    # 언어 모델 선택
    llm = ChatOpenAI(
        model="ft:gpt-3.5-turbo-0125:personal:suheezebal:9lHopkNl",
        temperature=0.4
    )
    # 답장 리턴
    reply = llm(template.format_messages(text=message))
    # 감정 분석 템플릿 생성
    emotion_template = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content='너는 "일반", "기쁨", "슬픔", "화남" 중에 하나로 대답할 수 있고,'
                                  '메시지를 분석해서 앞 예시 중 하나로 대답해줘'),
            HumanMessagePromptTemplate.from_template("{reply}")
        ]
    )
    emotion_llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.2
    )
    emotion = emotion_llm(emotion_template.format_messages(reply=reply))
    print(emotion.content)
    message_model = Message(question=message, reply=reply.content, user_id=user.get('user_id'), emotion=emotion.content)
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
def get_message_by_user(user_ip, username, page):
    messages_query = (
        Message.query
        .join(User, Message.user_id == User.user_id)
        .filter(User.connect_ip == user_ip)
        .filter(User.username == username)
        .order_by(Message.message_id.desc())
    )

    total_messages = messages_query.count()

    # if page.isnumeric():
    #     page = int(page)

    messages = (
        messages_query
        .limit(20)
        .offset((page - 1) * 20)
        .all()
    )
    return messages
