# 공식 Python 런타임 이미지를 기반으로 사용
FROM python:3.9-slim


RUN python -m pip install --upgrade pip
RUN apt-get clean && apt-get update && apt-get install -y \
    libmariadb-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


# 컨테이너 내 작업 디렉토리 설정
WORKDIR /app

# requirements.txt 파일을 컨테이너로 복사
COPY requirements.txt /app/

# requirements.txt에 명시된 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 현재 디렉토리의 모든 파일을 컨테이너의 /app 디렉토리로 복사
COPY . /app/

# Django 개발 서버를 위한 포트 8000 열기
EXPOSE 8000

# Django 개발 서버를 실행하는 명령어
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
