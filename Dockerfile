# 베이스 이미지 선택
FROM python:3.11.9-alpine3.19

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 빌드 도구 및 라이브러리 설치
RUN apk update && apk add --no-cache \
    build-base \
    mariadb-connector-c-dev \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev

# 필요 패키지 설치를 위해 requirements.txt 복사
COPY requirements.txt .

# 의존성 설치
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드 복사
COPY . .

# 환경 변수 설정 (필요에 따라)
ENV FLASK_ENV=production

# 포트 설정 (Flask 앱에서 사용하는 포트)
EXPOSE 5000

# Flask 앱 실행 (gunicorn 사용 권장)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
