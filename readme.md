## 미연시 백엔드

해당 내용은 수희와 대화할 수 있는 프로그램의 백엔드 입니다.

db 스키마 생성
.env 파일에 .env.example 내용을 복사 붙여넣기 후 DB 주소 등 내용을 채워주세요
sumsum_init2.sql 쿼리를 실행해주세요.

### 변경해야 하는 내용
```
# services.py
llm = ChatOpenAI(  
    model="ft:gpt-3.5-turbo-0125:personal:suheezebal:9lHopkNl",  
    temperature=0.4  
)
```
해당 내용의 모델명을 변경 해주셔야 합니다.

### 실행
1. 파이썬 가상환경 생성
2. pip install -r requirements.txt
3. flask run