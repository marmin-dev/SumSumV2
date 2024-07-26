from langchain_community.chat_models import ChatOpenAI
from langchain_core.messages import SystemMessage
from langchain_core.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from app import Session
from models import Message
import os

GPT_KEY = os.environ.get('CHAT_KEY')
os.environ["OPENAI_API_KEY"] = GPT_KEY


def get_all_user():
    session = Session()
    messages = session.query(Message).all()
    session.close()
    return f"{messages[0].message_id}: {messages[0].question}, {messages[0].reply}"


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
        temperature=1
    )
    reply = llm(template.format_messages(text=message))
    # todo: 모델 매핑, 데이터 베이스 인입
    return reply.content
